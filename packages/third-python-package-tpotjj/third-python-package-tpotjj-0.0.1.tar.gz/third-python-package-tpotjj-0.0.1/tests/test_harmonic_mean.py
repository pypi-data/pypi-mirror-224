import sys
from typing import Union

import pytest
from pytest import CaptureFixture, MonkeyPatch
from termcolor import colored

from third_python_package.harmony import main


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (["3", "3", "3"], "3.0"),
        ([], "0.0"),
        (["foo", "bar"], "0.0"),
    ],
)
def test_harmony_parametrized(
    inputs: list[Union[str | int | float]],
    monkeypatch: MonkeyPatch,
    capsys: CaptureFixture[str],
    expected: str,
) -> None:
    monkeypatch.setattr(sys, "argv", ["harmony"] + inputs)
    main()
    assert capsys.readouterr().out.strip() == colored(
        expected, "red", "on_cyan", attrs=["bold"]
    )

# FRUITS = ["apple"]


# def test_len():
#     assert len(FRUITS) == 1


# def test_append():
#     FRUITS.append("banana")
#     assert FRUITS == ["apple", "banana"]
