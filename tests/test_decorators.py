import pytest
from src.decorators import log, my_function


def test_log(capsys):
    @log(filename="test_log.txt")
    def function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert "my_function called with args: (1, 2), kwargs:{}. Result: 3\n" in captured.out

    try:
        my_function(0, 2)
    except TypeError as e:
        captured = capsys.readouterr()
        assert "my function error: " in captured.out
