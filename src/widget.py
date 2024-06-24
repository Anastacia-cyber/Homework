from src import masks


def mask_account_card(number: str) -> str:
    """Функция, которая маскирует номер карты или счета"""
    if "Счет" in number:
        account = masks.get_mask_account(number[-20:])
        return number.replace(number[-20:], account)
    else:
        card = masks.get_mask_card_number(number[-16:])
        return number.replace(number[-16:], card)


if __name__ == "__main__":
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 64686473678894779589"))


def get_data(date: str) -> str:
    """Функция, пеобразующая формат даты"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


if __name__ == "__main__":
    print(get_data("2018-07-11T02:26:18.671407"))
