# libpng-build

`libpng` を以下のターゲット向けに生成します。

- Windows: `x86`, `x64`
- Linux: `x86_64`, `aarch64`
- Android: `x86_64`, `arm64-v8a`

## ビルド

`ibpng` のソース一式を以下からダウンロードします。
`.tar.gz` 形式を選択してください。`zip` は改行コードの問題で `Linux` ビルドが通りません。

- <http://www.libpng.org/pub/png/libpng.html>

`zlib` は以下を参考にして事前にインストールしておきます。

- <https://github.com/kota-kota/zlib-build>

### Windows

```bash
$ python build_window.py
```

### Linux

```bash
$ python build_linux.py
```

### Android

```bash
$ python build_android.py
```
