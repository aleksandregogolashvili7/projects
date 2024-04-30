import bank

def test_h():
    assert bank.value("h") == 20
    assert bank.value("H") == 20
    assert bank.value("hey") == 20

def test_hello():
    assert bank.value("hello") == 0
    assert bank.value("Hello") == 0
    assert bank.value("hey") != 0

def test_else():
    assert bank.value("bonjour") == 100
    assert bank.value("joni") == 100