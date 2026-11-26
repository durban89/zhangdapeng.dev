+++
title = "Implementing Weighted Random Selection in PHP and Laravel"
description = "Learn how to implement weighted random selection in PHP and Laravel, configure traffic distribution, test probability ratios, and protect testing endpoints with environment-aware middleware."
date = 2026-11-26T10:00:00+08:00
lastmod = 2026-11-26T10:00:00+08:00
slug = "weighted-random-selection-php-laravel"
tags = ["PHP", "Laravel", "Algorithms", "Backend Development", "API Testing"]
categories = ["Development"]
keywords = ["Weighted Random Algorithm", "PHP Weighted Random", "Laravel Traffic Distribution", "Laravel Middleware", "A/B Testing"]

toc = true

image = "cover.png"
image_alt = "Weighted random selection in PHP and Laravel, illustrating an 80/20 traffic distribution between two ad platforms"
+++

## Introduction

In application development, we sometimes need to distribute traffic among multiple services, advertising platforms, or other resources according to predefined percentages.

For example, suppose an application integrates two advertising platforms:

- **ToBid**: 80% of traffic.
- **Gromore**: 20% of traffic.

Whenever the client requests an advertising configuration, the backend needs to select one of these platforms according to the configured ratio.

Although this requirement sounds straightforward, implementing it correctly involves several concepts, including weighted random algorithms, probability distribution, environment isolation, and API testing.

This article documents a practical implementation using PHP and Laravel 5.x.

The approach is not limited to advertising platforms. It can also be applied to:

- Distributing requests across multiple services.
- Gradually introducing a new implementation.
- Allocating traffic between different API providers.
- Running simple A/B experiments.
- Distributing tasks among multiple processing nodes.

## 1. Understanding the Weighted Random Algorithm

A straightforward solution is to use a random number to determine which option should be selected.

However, ordinary random selection gives every option an equal probability. That does not satisfy requirements such as 80% versus 20%.

This is where the **Weighted Random Algorithm** becomes useful.

### 1.1 How It Works

Suppose we have two advertising platforms:

| Platform | Weight | Expected Probability |
|---|---:|---:|
| ToBid | 80 | 80% |
| Gromore | 20 | 20% |

The total weight is:

\[
TotalWeight = 80 + 20 = 100
\]

Generate a random integer between 1 and 100:

- If the number is between 1 and 80, select ToBid.
- If the number is between 81 and 100, select Gromore.

This gives each platform its corresponding probability.

The important point is that the algorithm does not need to explicitly calculate percentages. It only needs to calculate the total weight and determine which interval contains the generated random number.

### 1.2 General Algorithm

The process can be summarized as follows:

1. Define a list of options and their corresponding weights.
2. Calculate the sum of all weights.
3. Generate a random number within the total weight range.
4. Iterate through the options and accumulate their weights.
5. Return the option whose cumulative weight contains the random number.

For example, if we have three options:

| Option | Weight | Random Number Range |
|---|---:|---|
| A | 50 | 1–50 |
| B | 30 | 51–80 |
| C | 20 | 81–100 |

The same algorithm works regardless of the number of options.

## 2. Implementing Weighted Random Selection in PHP

Before integrating the algorithm into Laravel, we can implement it as a standalone PHP function.

```php
<?php

function weightedRandom(array $items)
{
    if (empty($items)) {
        return null;
    }

    $totalWeight = array_sum(array_column($items, 'weight'));

    if ($totalWeight <= 0) {
        return null;
    }

    $random = random_int(1, $totalWeight);

    $currentWeight = 0;

    foreach ($items as $item) {
        $currentWeight += $item['weight'];

        if ($random <= $currentWeight) {
            return $item;
        }
    }

    return null;
}

$items = [
    ['name' => 'A', 'weight' => 80],
    ['name' => 'B', 'weight' => 20],
];

$result = weightedRandom($items);

print_r($result);
```

### 2.1 Why Use random_int()?

PHP provides several random number functions, including `rand()`, `mt_rand()`, and `random_int()`.

For this implementation, `random_int()` is a good choice because it generates cryptographically secure random integers and avoids the predictability associated with weaker random number generators.

For ordinary traffic distribution, cryptographic security is not necessarily required, but `random_int()` provides a reliable and straightforward implementation.

### 2.2 Why Use a Weight Array?

One advantage of this implementation is that the algorithm is independent of the actual business configuration.

If we later introduce another platform, we only need to add another item:

```php
$items = [
    ['name' => 'A', 'weight' => 70],
    ['name' => 'B', 'weight' => 20],
    ['name' => 'C', 'weight' => 10],
];
```

The selection logic does not need to change.

This separation makes the implementation easier to maintain and extend.

## 3. Integrating Weighted Random Selection into Laravel 5.x

Now let's apply the algorithm to an actual Laravel application.

Suppose we have an existing controller:

`app/Http/Controllers/Demo/User/GDRandomController.php`

The requirement is to distribute advertising requests between ToBid and Gromore.

### 3.1 Controller Implementation

```php
<?php

namespace App\Http\Controllers\Demo\User;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;

class GDRandomController extends Controller
{
    /**
     * Get the advertising platform configuration.
     */
    public function v1(Request $request)
    {
        $ads = [
            [
                'id'       => 1,
                'platform' => 'ToBid',
                'weight'   => 80,
            ],
            [
                'id'       => 2,
                'platform' => 'Gromore',
                'weight'   => 20,
            ],
        ];

        $selectedAd = $this->pickAdByWeight($ads);

        if ($selectedAd) {
            unset($selectedAd['weight']);
        }

        return response()->json([
            'code' => 200,
            'msg'  => 'success',
            'data' => $selectedAd,
        ]);
    }

    /**
     * Select an advertising platform based on its weight.
     */
    private function pickAdByWeight(array $ads)
    {
        if (empty($ads)) {
            return null;
        }

        $totalWeight = array_sum(array_column($ads, 'weight'));

        if ($totalWeight <= 0) {
            return null;
        }

        $random = random_int(1, $totalWeight);

        $currentWeight = 0;

        foreach ($ads as $ad) {
            $currentWeight += $ad['weight'];

            if ($random <= $currentWeight) {
                return $ad;
            }
        }

        return null;
    }

    /**
     * Test the weighted random distribution.
     */
    public function testV1(Request $request)
    {
        $stats = [
            'ToBid'   => 0,
            'Gromore' => 0,
        ];

        $total = 10000;

        for ($i = 0; $i < $total; $i++) {
            $response = $this->v1($request)->getData(true);

            $platform = $response['data']['platform'];

            $stats[$platform]++;
        }

        return response()->json([
            'env'           => app()->environment(),
            'total'         => $total,
            'ToBid_count'   => $stats['ToBid'],
            'ToBid_ratio'   => round(($stats['ToBid'] / $total) * 100, 2) . '%',
            'Gromore_count' => $stats['Gromore'],
            'Gromore_ratio' => round(($stats['Gromore'] / $total) * 100, 2) . '%',
        ]);
    }
}
```

### 3.2 API Response

```json
{
    "code": 200,
    "msg": "success",
    "data": {
        "id": 1,
        "platform": "ToBid"
    }
}
```

The `weight` field is removed before returning the response because it is an internal backend configuration.

## 4. Testing the Distribution Ratio

To verify the algorithm, we can simulate 10,000 selections and calculate the actual distribution.

The `testV1()` method above performs this test.

A possible result is:

```json
{
    "env": "local",
    "total": 10000,
    "ToBid_count": 8014,
    "ToBid_ratio": "80.14%",
    "Gromore_count": 1986,
    "Gromore_ratio": "19.86%"
}
```

The actual result varies between executions. This is expected because weighted random selection is probabilistic rather than deterministic.

## 5. Restricting Testing Endpoints to Non-Production Environments

Testing endpoints should never be publicly accessible in production.

A reusable solution is to implement a dedicated middleware.

### 5.1 Create Middleware

```bash
php artisan make:middleware CheckTestingEnv
```

Edit `app/Http/Middleware/CheckTestingEnv.php`:

```php
<?php

namespace App\Http\Middleware;

use Closure;

class CheckTestingEnv
{
    public function handle($request, Closure $next)
    {
        if (app()->environment('production')) {
            abort(404);
        }

        return $next($request);
    }
}
```

For stricter control, use an environment whitelist:

```php
if (!app()->environment([
    'local',
    'testing',
    'staging',
])) {
    abort(404);
}
```

### 5.2 Register the Middleware

Open `app/Http/Kernel.php` and register the middleware in `$routeMiddleware`:

```php
protected $routeMiddleware = [
    // Existing middleware...

    'testing.env' => \App\Http\Middleware\CheckTestingEnv::class,
];
```

## 6. Organizing Production and Testing Routes

### 6.1 Production Routes

```php
Route::group([
    'prefix'     => '/api/user',
    'namespace'  => 'Demo\User',
    'middleware' => [
        'api.sign',
    ],
], function () {

    Route::group([
        'middleware' => [
            // 'api.token',
        ],
    ], function () {

        Route::get(
            '/gdrandom/v1',
            'GDRandomController@v1'
        );

    });

});
```

### 6.2 Testing Routes

```php
Route::group([
    'prefix'     => '/api/user/test',
    'namespace'  => 'Demo\User',
    'middleware' => [
        'testing.env',
    ],
], function () {

    Route::get(
        '/gdrandom/v1',
        'GDRandomController@testV1'
    );

});
```

The resulting endpoints are:

| Purpose | Endpoint |
|---|---|
| Production API | `/api/user/gdrandom/v1` |
| Testing API | `/api/user/test/gdrandom/v1` |

The testing endpoint bypasses `api.sign` and `api.token`, but is protected by the environment-checking middleware.

For publicly accessible staging environments, additional authentication or IP restrictions are recommended.

## 7. Automatically Generating API Signatures for Testing

If we need to test the production API, which requires signature verification, we can create a standalone PHP script to generate signatures and send requests automatically.

The following is a common MD5-based signing template. The actual implementation must match the application's `api.sign` middleware.

### 7.1 Create test_sign.php

```php
<?php

$baseUrl = 'http://your-test-domain/api/user/gdrandom/v1';

$appKey = 'your_app_key';
$appSecret = 'your_app_secret';

$userToken = 'your_user_token';

/**
 * Generate API signature.
 */
function generateSign(array $params, string $secret)
{
    $params = array_filter(
        $params,
        function ($value, $key) {
            return $key !== 'sign'
                && $value !== ''
                && $value !== null;
        },
        ARRAY_FILTER_USE_BOTH
    );

    ksort($params);

    $queryString = urldecode(
        http_build_query($params)
    );

    return strtoupper(
        md5($queryString . '&key=' . $secret)
    );
}

$params = [
    'app_key'   => $appKey,
    'timestamp' => time(),
    'nonce'     => bin2hex(random_bytes(8)),
];

$params['sign'] = generateSign($params, $appSecret);

$requestUrl = $baseUrl . '?' . http_build_query($params);

$headers = [
    'Accept: application/json',

    // 'Authorization: Bearer ' . $userToken,
    // 'token: ' . $userToken,
];

$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, $requestUrl);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_TIMEOUT, 10);

$response = curl_exec($ch);

$httpCode = curl_getinfo(
    $ch,
    CURLINFO_HTTP_CODE
);

if ($response === false) {
    echo 'cURL Error: ' . curl_error($ch) . PHP_EOL;
}

curl_close($ch);

echo "HTTP Status: {$httpCode}\n";
echo "Response:\n{$response}\n";
```

### 7.2 Execute the Script

```bash
php test_sign.php
```

The script automatically generates the timestamp, nonce, signature, and HTTP request.

Before using it, make sure the signature generation rules match your actual middleware implementation.

## 8. Important Considerations

### 8.1 Weighted Random Does Not Guarantee an Exact Short-Term Ratio

An 80:20 configuration means each independent selection has an 80% probability of selecting A and a 20% probability of selecting B.

It does not guarantee exactly four A selections and one B selection in every five requests.

If strict short-term distribution is required, consider a counter-based or weighted round-robin algorithm.

### 8.2 Random Selection and User-Based Allocation Are Different

For persistent user allocation, a stable identifier such as `user_id` can be used:

```php
$bucket = crc32($userId) % 100;

$platform = $bucket < 80
    ? 'ToBid'
    : 'Gromore';
```

This ensures that the same user consistently receives the same platform, provided the identifier and allocation configuration remain unchanged.

### 8.3 Route Caching Considerations

Laravel 5.x does not support caching routes defined using Closure callbacks.

Using controller methods for testing endpoints is preferable when route caching is required.

```bash
php artisan route:clear
php artisan route:cache
```

Generate route caches using the target server's actual configuration rather than copying a development environment's route cache into production.

### 8.4 Validate Weight Configuration

Production implementations should validate that every item has a valid, non-negative weight.

If all weights are zero, there is no valid selection. Handle this situation according to the application's business requirements.

## Conclusion

Weighted random selection is a relatively simple algorithm, but it solves a common problem in application development.

By converting probability percentages into weight intervals, generating a random number, and selecting the corresponding item, we can implement flexible traffic distribution without complicated logic.

Combining this algorithm with Laravel controllers and middleware also allows us to separate production functionality from testing functionality.

The most valuable part of this implementation is not just selecting between ToBid and Gromore. It is understanding how a general-purpose algorithm can be applied to a real business requirement, tested statistically, and integrated safely into an existing application.

Even if you have never implemented this kind of logic before, understanding the underlying algorithm makes it much easier to recognize and solve similar problems in future projects.