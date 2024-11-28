from zkouska1 import pozpatku

def test_pozpatku():
    assert pozpatku("ahoj") == "joha"
    assert pozpatku("jak se máš?") == "?šám es kaj"