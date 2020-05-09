import hello

def test_hello():
    hello.inp = []
    hello.greet("Karole")
    assert hello.inp == ['Hello','Karole']


def test_hello_elena():
    hello.inp = []
    hello.greet("Elena")
    assert hello.inp == ['Hello','Elena']