# Nahida

#### _Read this in [other translations](translation/translations.md)._

<kbd>[<img title="Русский язык" alt="Русский язык" src="https://cdn.staticaly.com/gh/hjnilsson/country-flags/master/svg/ru.svg" width="22">](translation/README.ru.md)</kbd>
<kbd>[<img title="Українська" alt="Українська" src="https://cdn.staticaly.com/gh/hjnilsson/country-flags/master/svg/ua.svg" width="22">](translation/README.uk.md)</kbd>

> This is part of `Pudgeland 💖 Open Source` ecosystems

An unofficial **[Waifu.pics](https://waifu.pics)** API wrapper for Python

## 📦 Packages

### 🐍 PyPI

```sh
pip install nahida
```

## 🔎 Examples

```py
import nahida

client = nahida.Client()

print(client.nsfw.search("neko"))

print(client.sfw.search("awoo"))
print(client.sfw.search("bite"))
```
