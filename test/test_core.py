
import pytest
from ..velox_telegram_bot.main import add


def test_add():
    print("runnin")
    assert add(2,3)==5