FRUITS = ["apple"]


def test_len() -> None:
    assert len(FRUITS) == 1


def test_append() -> None:
    FRUITS.append("banana")
    assert FRUITS == ["apple", "banana"]
