from typing import Generator


def transaction_descriptions(transactions: list) -> Generator:
    """Возвращает описание операции"""
    for transaction in transactions:
        yield transaction["description"]


def filter_by_currency(transactions: list, currency: str) -> Generator:
    """Возвращает id операции по заданной валюте"""
    for transaction in transactions:
        operation_amount_dic = transaction["operationAmount"]
        currency_dic = operation_amount_dic["currency"]
        if currency_dic["code"] == currency:
            yield transaction["id"]


def card_number_generator(start: int, stop: int) -> Generator:
    """Генератор номеров бансковских карт в формате 0123 4567 8901 2345"""
    card_number_int = 10000000000000000 + start
    while True:
        card_number_list = []
        card_number_str = str(card_number_int)[1:]
        card_number_list.extend(
            [
                card_number_str[:4],
                card_number_str[4:8],
                card_number_str[8:12],
                card_number_str[12:],
            ]
        )
        if start <= stop:
            yield " ".join(card_number_list)
            card_number_int += 1
            start += 1
