+++
title = "Unix Timestamp in Seconds vs Milliseconds: What's the Difference?"
description = "Learn the difference between Unix timestamps in seconds and milliseconds, how to identify 10-digit and 13-digit timestamps, and how to convert them correctly."
slug = "unix-timestamp-seconds-vs-milliseconds"
date = "2026-08-25T10:00:00+08:00"
lastmod = "2026-08-25T10:00:00+08:00"
draft = false

tags = ["Unix Timestamp", "Timestamp", "Milliseconds", "Seconds"]
categories = ["Development"]

keywords = [
  "unix timestamp milliseconds",
  "unix timestamp seconds",
  "unix timestamp milliseconds vs seconds",
  "10 digit unix timestamp",
  "13 digit unix timestamp",
  "unix timestamp 10 digits",
  "unix timestamp 13 digits"
]
+++

# Unix Timestamp in Seconds vs Milliseconds: What's the Difference?

If you work with APIs, databases, logs, or backend systems, you have probably encountered Unix timestamps.

Sometimes a timestamp looks like this:

```text
1756080000
```

Other times, you may see:

```text
1756080000000
```

They may look similar, but they use different units.

The first timestamp is measured in **seconds**, while the second is measured in **milliseconds**.

Understanding the difference between Unix timestamps in seconds and milliseconds is important because using the wrong unit can produce a completely incorrect date.

In this guide, you'll learn:

* What a Unix timestamp is
* The difference between seconds and milliseconds
* Why Unix timestamps usually have 10 or 13 digits
* How to tell which unit a timestamp uses
* How to convert between seconds and milliseconds
* Common timestamp conversion mistakes

## What Is a Unix Timestamp?

A Unix timestamp represents the number of seconds that have elapsed since the Unix epoch:

```text
1970-01-01 00:00:00 UTC
```

For example:

```text
0
```

represents:

```text
1970-01-01 00:00:00 UTC
```

A timestamp such as:

```text
1756080000
```

represents a point in time after the Unix epoch.

Unix timestamps are widely used because they provide a simple numerical representation of time that is easy for computers to store, compare, and transmit.

However, Unix timestamps are not always represented using seconds.

Some systems use **milliseconds** instead.

That's where the difference between 10-digit and 13-digit timestamps becomes important.

## Unix Timestamp in Seconds

The traditional Unix timestamp uses **seconds** as its unit.

For example:

```text
1756080000
```

means that 1,756,080,000 seconds have elapsed since:

```text
1970-01-01 00:00:00 UTC
```

Most Unix timestamps representing dates around the current era are approximately **10 digits long** when measured in seconds.

For example:

```text
1756080000
```

### Why are Unix timestamps in seconds usually 10 digits?

The Unix timestamp increases by one every second.

As time moves forward, the number gets larger:

```text
1970 → 0
2000 → approximately 9 digits
2020 → approximately 10 digits
2025 → approximately 10 digits
```

This is why timestamps in seconds are commonly referred to as **10-digit Unix timestamps**.

However, digit count alone should not be treated as a strict rule for every possible date.

The important thing is the **unit**: seconds.

## Unix Timestamp in Milliseconds

A millisecond is one thousandth of a second.

Therefore:

```text
1 second = 1,000 milliseconds
```

A Unix timestamp represented in milliseconds counts the number of milliseconds since the Unix epoch.

For example:

```text
1756080000000
```

is the millisecond representation of:

```text
1756080000
```

seconds.

Because there are 1,000 milliseconds in every second, the millisecond timestamp is usually three digits longer.

Current timestamps in milliseconds are commonly **13 digits long**.

For example:

```text
Seconds:      1756080000
Milliseconds: 1756080000000
```

## Unix Timestamp Seconds vs Milliseconds

The simplest way to understand the difference is:

| Unit         | Example         | Common length |
| ------------ | --------------- | ------------- |
| Seconds      | `1756080000`    | 10 digits     |
| Milliseconds | `1756080000000` | 13 digits     |

The relationship is:

```text
milliseconds = seconds × 1000
```

And:

```text
seconds = milliseconds ÷ 1000
```

For example:

```text
1756080000 × 1000
= 1756080000000
```

So these two timestamps represent the same moment:

```text
1756080000 seconds
```

and:

```text
1756080000000 milliseconds
```

The only difference is the unit used to represent the time.

## How to Tell If a Timestamp Is in Seconds or Milliseconds

When you encounter an unknown Unix timestamp, the number of digits can provide a useful first clue.

### 10-digit timestamp

A timestamp such as:

```text
1756080000
```

is likely to be in **seconds**.

### 13-digit timestamp

A timestamp such as:

```text
1756080000000
```

is likely to be in **milliseconds**.

This works well for timestamps representing dates around the present day.

However, you should not rely exclusively on the number of digits.

The safest approach is to understand the API, database, programming language, or system that produced the timestamp.

For example, different programming environments may use different timestamp units.

## Why Do Some Systems Use Milliseconds?

Seconds provide enough precision for many applications.

For example, an event log might only need to record:

```text
1756080000
```

But applications that need more precise timing may require milliseconds:

```text
1756080000123
```

Milliseconds are useful for things such as:

* Web applications
* API responses
* Event tracking
* Performance measurements
* Database records
* JavaScript applications
* Logs where multiple events can happen within the same second

With milliseconds, two events that happen during the same second can still be distinguished.

For example:

```text
1756080000123
1756080000789
```

Both timestamps occur within the same second, but they represent different points in time.

## How to Convert Seconds to Milliseconds

Converting a Unix timestamp from seconds to milliseconds is simple.

Multiply the timestamp by 1,000:

```text
milliseconds = seconds × 1000
```

For example:

```text
1756080000 × 1000
```

results in:

```text
1756080000000
```

### JavaScript example

In JavaScript, you can convert seconds to milliseconds like this:

```javascript
const seconds = 1756080000;
const milliseconds = seconds * 1000;

console.log(milliseconds);
```

The result is:

```text
1756080000000
```

## How to Convert Milliseconds to Seconds

To convert milliseconds back to seconds, divide by 1,000:

```text
seconds = milliseconds ÷ 1000
```

For example:

```text
1756080000000 ÷ 1000
```

results in:

```text
1756080000
```

In JavaScript:

```javascript
const milliseconds = 1756080000000;
const seconds = milliseconds / 1000;

console.log(seconds);
```

If the millisecond timestamp contains a fractional remainder, you may need to decide whether to keep or discard the fractional part depending on your application's requirements.

## Common Unix Timestamp Conversion Mistakes

The most common timestamp problem is using the correct number with the wrong unit.

### Mistake 1: Treating seconds as milliseconds

Suppose you have:

```text
1756080000
```

and pass it directly to a JavaScript function that expects milliseconds:

```javascript
new Date(1756080000);
```

The result will represent a date very close to the Unix epoch rather than the intended modern date.

The correct conversion is:

```javascript
new Date(1756080000 * 1000);
```

### Mistake 2: Treating milliseconds as seconds

The opposite problem can be even more obvious.

If you take:

```text
1756080000000
```

and treat it as seconds, the resulting value is far outside the expected date range.

You need to divide by 1,000 first:

```text
1756080000000 ÷ 1000
= 1756080000
```

### Mistake 3: Assuming every timestamp has exactly 10 or 13 digits

10 and 13 digits are useful rules of thumb for modern Unix timestamps, but they are not universal rules.

Historical dates, future dates, and timestamps with different precision can have different lengths.

Always consider the source and unit of the timestamp.

## Unix Timestamp in JavaScript

JavaScript is a common source of confusion because the built-in `Date` object uses **milliseconds** for Unix-style timestamps.

For example:

```javascript
const timestamp = 1756080000000;

const date = new Date(timestamp);

console.log(date);
```

Here:

```text
1756080000000
```

is interpreted as milliseconds.

If your Unix timestamp is in seconds:

```javascript
const timestamp = 1756080000;

const date = new Date(timestamp * 1000);

console.log(date);
```

The multiplication by `1000` converts seconds into milliseconds before passing the value to `Date`.

## Unix Timestamp in APIs and Databases

When working with APIs or databases, always check the documentation before assuming the timestamp unit.

An API might return:

```json
{
  "created_at": 1756080000
}
```

or:

```json
{
  "created_at": 1756080000000
}
```

Both can represent the same point in time.

The difference is simply whether the value is expressed in seconds or milliseconds.

If you're integrating multiple systems, clearly documenting the timestamp unit can prevent subtle bugs.

For example, instead of naming a variable:

```text
timestamp
```

you can make the unit explicit:

```text
timestampSeconds
```

or:

```text
timestampMilliseconds
```

This makes the code easier to understand and reduces the chance of accidentally mixing units.

## Quick Reference

Here is a simple reference for the most common cases:

| Timestamp type                 | Unit         | Example         | Conversion            |
| ------------------------------ | ------------ | --------------- | --------------------- |
| Unix timestamp in seconds      | Seconds      | `1756080000`    | `seconds × 1000`      |
| Unix timestamp in milliseconds | Milliseconds | `1756080000000` | `milliseconds ÷ 1000` |

Remember:

```text
1 second = 1,000 milliseconds
```

So:

```text
Seconds → Milliseconds
× 1000

Milliseconds → Seconds
÷ 1000
```

## Convert Unix Timestamps Easily

If you frequently work with Unix timestamps, manually determining whether a value is in seconds or milliseconds can become inconvenient.

A timestamp converter can automatically detect common timestamp formats and convert them into human-readable dates.

For example, **[Unix Timestamp Converter & Epoch Pro](/products/timestamp-pro)** can detect common 10-digit and 13-digit timestamps and show the corresponding date and time.

You can use it when working with:

* API responses
* Server logs
* Database timestamps
* Developer tools
* Debugging
* Event data

The goal is to make timestamp conversion quick without manually calculating the difference between seconds and milliseconds.

## Frequently Asked Questions

### What is the difference between Unix timestamps in seconds and milliseconds?

The difference is the unit of measurement.

A timestamp in seconds counts seconds since the Unix epoch, while a timestamp in milliseconds counts milliseconds since the Unix epoch.

Since one second contains 1,000 milliseconds:

```text
milliseconds = seconds × 1000
```

### Is a 10-digit Unix timestamp in seconds?

For modern dates, a 10-digit Unix timestamp is usually measured in seconds.

However, digit count is only a useful indication. You should verify the timestamp unit from the system or API that generated it.

### Is a 13-digit Unix timestamp in milliseconds?

For modern dates, a 13-digit Unix timestamp is usually measured in milliseconds.

Again, this is a common convention rather than an absolute rule.

### How do I convert a Unix timestamp from seconds to milliseconds?

Multiply the timestamp by 1,000:

```text
milliseconds = seconds × 1000
```

For example:

```text
1756080000 × 1000 = 1756080000000
```

### How do I convert milliseconds to seconds?

Divide the timestamp by 1,000:

```text
seconds = milliseconds ÷ 1000
```

For example:

```text
1756080000000 ÷ 1000 = 1756080000
```

### Does JavaScript use seconds or milliseconds?

JavaScript's `Date` object uses milliseconds when working with Unix-style timestamps.

If you have a Unix timestamp in seconds, multiply it by 1,000 before passing it to `new Date()`.

## Conclusion

Unix timestamps can be represented using different units, but the two most common are **seconds** and **milliseconds**.

For modern timestamps:

```text
10 digits → usually seconds
13 digits → usually milliseconds
```

The conversion is straightforward:

```text
seconds × 1000 = milliseconds

milliseconds ÷ 1000 = seconds
```

The important thing is to always verify the unit before converting or storing a timestamp. Using seconds where milliseconds are expected, or milliseconds where seconds are expected, can produce completely incorrect dates.

Once you understand the difference, working with Unix timestamps becomes much easier.

```