# yandex_realty_parser
Library that parses yandex realty website

## Installation
`pip install yandex-realty-parser`

## Usage
```python
import yandex_realty_parser
data = yandex_realty_parser.parse('https://realty.ya.ru/moskva/snyat/kvartira/odnokomnatnaya/?priceMax=42500',
                                   fields=('address', 'link'))
print(data)
# [{'address': 'ул. Пушкина, 19', 'link': 'https://realty.ya.ru/offer/124012401240'},
#  {'address': 'ул. Менелая, 24', 'link': 'https://realty.ya.ru/offer/160516051605'}]
```
