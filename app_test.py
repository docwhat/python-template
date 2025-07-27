from app import simple


def test_simple():
    assert simple() == "Hello, World!"


def test_is_string():
    assert isinstance(simple(), str)


# EOF
