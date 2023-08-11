import pytest


@pytest.mark.parametrize("name", ["哈利波特", "赫敏"])
def test_mm(name):
    print(f"name:{name}")
