# Новый виджет
## Описание
Новый виджет - это новая фича для личного кабинет клиента,которая показывает несколько последних успешных банковских операций клиента.
## Установка

* Клонируйте репозиторий:
```
git clone https://github.com/Anastacia-cyber/Homework
```
* Установите зависимости:
```
pip install -r requirements.txt
```
## Тестирование
Было проведено тестирование программ на выявление ошибок.

* Установка зависимости:
```
poetry add --group dev pytest
```

* Запуск тестов:
```
pytest
```
* Покрытие тестами:
```
src\__init__.py                0      0   100%
src\generators.py             20      0   100%
src\masks.py                  11      4    64%
src\processing.py             14      2    86%
src\widget.py                 14      3    79%
tests\__init__.py              0      0   100%
tests\conftest.py             10      0   100%
tests\test_generators.py      23      0   100%
tests\test_masks.py            8      0   100%
tests\test_processing.py       6      0   100%
tests\test_widget.py           7      0   100%
----------------------------------------------
TOTAL                        113      9    92%

```
## Новый функционал(24.06.2024)
* Функция `filter_by_currency` - возвращает итератор, который выдает по очереди операции с заданной валютой
* Генератор `transaction_descriptions` - возвращает описание каждой операции по очереди
* Генератор `card_number_generator` - генерирует номера карт в формате XXXX XXXX XXXX XXXX