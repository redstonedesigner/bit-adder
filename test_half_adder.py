from lib import adderhandler


class Tests:
    def test_00(self):
        adder = adderhandler.HalfAdder(0, 0)
        assert adder.s == 0
        assert adder.c == 0

    def test_01(self):
        adder = adderhandler.HalfAdder(0, 1)
        assert adder.s == 1
        assert adder.c == 0

    def test_10(self):
        adder = adderhandler.HalfAdder(1, 0)
        assert adder.s == 1
        assert adder.c == 0

    def test_11(self):
        adder = adderhandler.HalfAdder(1, 1)
        assert adder.s == 0
        assert adder.c == 1
