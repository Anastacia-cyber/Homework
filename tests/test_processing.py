from src.processing import filter_by_state, sort_by_date
import pytest


def test_filter_by_state(dic_list):
    assert filter_by_state(dic_list)


def test_sort_by_date(sorted_list):
    assert sort_by_date(sorted_list)
