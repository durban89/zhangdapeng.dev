---
title: "Nodejs 之 分享加密算法"
date: "2025-07-03 11:08:24"
slug: "nodejs-zhi-fen-xiang-jia-mi-suan-fa"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/07/03/Nodejs-之-分享加密算法/"
  - "/2025/07/03/Nodejs-之-分享加密算法.html"
  - "/Nodejs-之-分享加密算法/"
  - "/Nodejs-之-分享加密算法.html"
  - "/2025/07/03/nodejs-zhi-fen-xiang-jia-mi-suan-fa/"
  - "/2025/07/03/nodejs-zhi-fen-xiang-jia-mi-suan-fa.html"
  - "/nodejs-zhi-fen-xiang-jia-mi-suan-fa.html"
---
这里分享一个node实现的加解密算法，对接了至少三家的接口但是没加的算法都不一样。看着做为程序员的辛苦，我这里分享了。

```js
/**
 * @author zhandapeng <xx@xx>
 * @date 7/12/2016
 *
 * openssl pkcs12 -in 9f_KDJZ_private.pfx -out 9f_KDJZ_private.pem -nodes   
 * openssl x509 -in 9fwlc_public.crt -outform der -out 9fwlc_public.der
 * openssl x509 -in 9fwlc_public.crt -inform der -outform pem -out 9fwlc_public.pem
 *
 * 玖富加密解密
 */
'use strict';

const crypto = require('crypto');
const constants = require('constants');
const _padding = constants.RSA_PKCS1_PADDING;
const _encoding = 'base64';
const _signatureAlgorithm = 'RSA-SHA1';


class XxxxRSA {
  constructor(options) {
    this.options = Object.assign({}, options);
  }

  /**
   * 签名
   * @param  {String} data [加密的数据]
   * @return {String}      [签名的数据]
   */
  _sign(data) {
    const sign = crypto.createSign(_signatureAlgorithm);
    sign.update(data, 'utf8');
    return sign.sign(this.options.privateKey, _encoding);
  }

  /**
   * 验签
   * @param  {String} sign [签名数据]
   * @param  {String} data [加密数据]
   * @return {Boolean}      [description]
   */
  _verify(sign, data) {
    const verifier = crypto.createVerify(_signatureAlgorithm);
    verifier.update(new Buffer(data, _encoding), 'utf8');
    return verifier.verify(this.options.publicKey, new Buffer(sign, _encoding));
  }

  /**
   * 加密
   * @param  {String} msg [要加密的数据]
   * @return {Object}     [签名的数据和加密的数据]
   */
  encrypt(msg) {
    const blockSize = 128;
    const padding = 11;

    let buffer = new Buffer(msg);

    const chunkSize = blockSize - padding;
    const nbBlocks = Math.ceil(buffer.length / (chunkSize));

    let outputBuffer = new Buffer(nbBlocks * blockSize);
    for (let i = 0; i < nbBlocks; i++) {
      let currentBlock = buffer.slice(chunkSize * i, chunkSize * (i + 1));
      let encryptedChunk = crypto.publicEncrypt({
        key: this.options.publicKey,
        padding: _padding
      }, currentBlock);

      encryptedChunk.copy(outputBuffer, i * blockSize);
    }

    return {
      data: outputBuffer.toString(_encoding),
      sign: this._sign(outputBuffer)
    };
  };

  /**
   * 解密
   * @param  {Object} obj [签名数据和加密数据]
   * @return {String}     [解密的数据]
   */
  decrypt(obj) {
    if (!this._verify(obj.sign, obj.data)) {
      throw new Error('Sign verify field.');
    }

    const blockSize = 128;
    let buffer = new Buffer(obj.data, _encoding);
    const nbBlocks = Math.ceil(buffer.length / (blockSize));
    let outputBuffer = new Buffer(nbBlocks * blockSize);

    let totalLength = 0;
    for (var i = 0; i < nbBlocks; i++) {
      let currentBlock = buffer.slice(blockSize * i, Math.min(blockSize * (i + 1), buffer.length));
      let decryptedBuf = crypto.privateDecrypt({
        key: this.options.privateKey,
        padding: _padding
      }, currentBlock);

      decryptedBuf.copy(outputBuffer, totalLength);
      totalLength += decryptedBuf.length;
    }

    let data = outputBuffer.slice(0, totalLength);

    return data.toString();
  };
}

export default XxxxRSA;
```

事实上简单的不得了，只是我不会而已，对不起献丑了。

这里针对java和php版本做个参考。主要是是说encrypt和decrypt部分。

encrypt->java实现

```java
public static String encrypt(Key key, String dataStr)
        throws RuntimeException {
    try {
        byte[] data = dataStr.getBytes("UTF-8");
        Cipher cipher = Cipher.getInstance(transformation);
        cipher.init(Cipher.ENCRYPT_MODE, key);

        int outputSize = cipher.getOutputSize(data.length);// 获得加密块加密后块大小
        int leavedSize = data.length % MAX_ENCRYPT_BLOCK;
        int blocksSize = leavedSize != 0 ? data.length / MAX_ENCRYPT_BLOCK
                + 1 : data.length / MAX_ENCRYPT_BLOCK;
        byte[] raw = new byte[outputSize * blocksSize];
        int i = 0;
        while (data.length - i * MAX_ENCRYPT_BLOCK > 0) {
            if (data.length - i * MAX_ENCRYPT_BLOCK > MAX_ENCRYPT_BLOCK)
                cipher.doFinal(data, i * MAX_ENCRYPT_BLOCK,
                        MAX_ENCRYPT_BLOCK, raw, i * outputSize);
            else
                cipher.doFinal(data, i * MAX_ENCRYPT_BLOCK, data.length - i
                        * MAX_ENCRYPT_BLOCK, raw, i * outputSize);
            i++;
        }
        return Base64.encodeBase64String(raw);

    } catch (NoSuchAlgorithmException e) {
        throw new RuntimeException(e);
    } catch (NoSuchPaddingException e) {
        throw new RuntimeException(e);
    } catch (IllegalBlockSizeException e) {
        throw new RuntimeException(e);
    } catch (BadPaddingException e) {
        throw new RuntimeException(e);
    } catch (InvalidKeyException e) {
        throw new RuntimeException(e);
    } catch (ShortBufferException e) {
        e.printStackTrace();
    } catch (UnsupportedEncodingException e) {
        // TODO Auto-generated catch block
        e.printStackTrace();
    }
    return null;
}
```

decrypt->java实现

```java
public static String decrypt(Key key, String dataStr)
        throws RuntimeException {
    try {
        byte[] data = Base64.decodeBase64(dataStr);
        Cipher cipher = Cipher.getInstance(transformation);
        cipher.init(Cipher.DECRYPT_MODE, key);
        ByteArrayOutputStream bout = new ByteArrayOutputStream(64);
        int j = 0;

        while (data.length - j * MAX_DECRYPT_BLOCK > 0) {
            bout.write(cipher.doFinal(data, j * MAX_DECRYPT_BLOCK,
                    MAX_DECRYPT_BLOCK));
            j++;
        }
        return new String(bout.toByteArray(), "UTF-8");
    } catch (NoSuchAlgorithmException e) {
        throw new RuntimeException(e);
    } catch (NoSuchPaddingException e) {
        throw new RuntimeException(e);
    } catch (InvalidKeyException e) {
        throw new RuntimeException(e);
    } catch (IllegalBlockSizeException e) {
        throw new RuntimeException(e);
    } catch (BadPaddingException e) {
        throw new RuntimeException(e);
    } catch (IOException e) {
        e.printStackTrace();
    }
    return null;
}
```

encrypt->php实现

```php
public function encrypt($content, $public_key) {
    $priKey = file_get_contents($public_key);
    $res = openssl_get_publickey($priKey);
    //把需要加密的内容，按128位拆开加密
    $result  = '';
    for($i = 0; $i < ((strlen($content) - strlen($content)%117)/117+1); $i++  ) {
        $data = mb_strcut($content, $i*117, 117, 'utf-8');
        openssl_public_encrypt($data, $encrypted, $res);
        $result .= $encrypted;
    }
    openssl_free_key($res);
    //用base64将二进制编码
    $result = base64_encode($result);
    return $result;
}
```

decrypt->php实现

```php
public function rsaDecrypt($content, $private_key) {
    $priKey = file_get_contents($private_key);
    $res = openssl_get_privatekey($priKey);
    // var_dump($priKey);
    // var_dump($res);exit();
    //用base64将内容还原成二进制
    $content = base64_decode($content);
    //把需要解密的内容，按128位拆开解密
    $result  = '';
    for($i = 0; $i < strlen($content)/128; $i++  ) {
        $data = substr($content, $i * 128, 128);
        openssl_private_decrypt($data, $decrypt, $res);
        $result .= $decrypt;
    }
    openssl_free_key($res);
    return $result;
}
```



