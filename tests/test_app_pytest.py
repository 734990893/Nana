from src.api.app import welcome


def test_welcome():
    assert welcome() == 'Nana welcomes you!'
