from typing import Any
from datetime import datetime

import masks


def mask_account_card(number: str) -> str:
    """Функция, которая маскирует номер карты или счета"""
    if "Счет" in number:

        return masks.get_mask_account(number)
    else:
        card = masks.get_mask_card_number(number[-16:])
        return number.replace(number[-16:],card)


if __name__ == "__main__":
    print(mask_account_card("Maestro 1596837868705199"))
