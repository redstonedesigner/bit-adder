from lib import adderhandler


class Tests:
    def test_000(self):
        adder = adderhandler.FullAdder(0, 0, 0)
        assert adder.s is 0
        assert adder.c is 0

    def test_001(self):
        adder = adderhandler.FullAdder(0, 0, 1)
        assert adder.s is 1
        assert adder.c is 0

    def test_010(self):
        adder = adderhandler.FullAdder(0, 1, 0)
        assert adder.s is 1
        assert adder.c is 0

    def test_011(self):
        adder = adderhandler.FullAdder(0, 1, 1)
        assert adder.s is 0
        assert adder.c is 1

    def test_100(self):
        adder = adderhandler.FullAdder(1, 0, 0)
        assert adder.s is 1
        assert adder.c is 0

    def test_101(self):
        adder = adderhandler.FullAdder(1, 0, 1)
        assert adder.s is 0
        assert adder.c is 1

    def test_110(self):
        adder = adderhandler.FullAdder(1, 1, 0)
        assert adder.s is 0
        assert adder.c is 1

    def test_111(self):
        adder = adderhandler.FullAdder(1, 1, 1)
        assert adder.s is 1
        assert adder.c is 1
