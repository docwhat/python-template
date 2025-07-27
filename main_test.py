from main import main_text


def test_main_text():
    assert main_text() == "Hello from app!"


def test_is_string():
    assert isinstance(main_text(), str)


# EOF
