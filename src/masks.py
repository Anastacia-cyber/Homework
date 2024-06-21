def get_mask_card_number(card_number: str) -> str | None:
    """Функция маскировки номера карты"""
    if not card_number.isdigit() or len(card_number) != 16:
        return None
    else:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(mask_account: str) -> str | None:
    """Функция маскировки номера счета"""
    if mask_account.isdigit() and len(mask_account) != 20:
        return None
    else:
        return f"**{mask_account[-4::]}"


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
