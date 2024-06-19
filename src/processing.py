from typing import Any


def filter_by_state(dic_list: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция, которая принимает список словарей и возвращает новый список,
    где state содержит переданное в функцию значение"""
    new_list = []

    for dic in dic_list:
        if dic.get("state") == state:
            new_list.append(dic)
    return new_list


if __name__ == "__main__":
    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )


def sort_by_date(original_list: list[dict[str, Any]], reverse_list: bool = True) -> list[dict[str, Any]]:
    """Функция, которая принимает на вход список словарей и возвращает новый список,
    в котором исходные словари отсортированы по убыванию даты"""
    sorted_list = sorted(original_list, key=lambda d: d["date"], reverse=reverse_list)
    return sorted_list


if __name__ == "__main__":
    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )
