import gatehandler


class Tests:
    def test_nand(self):
        gates = gatehandler.GateHandler()
        assert gates.nand(0, 0) is True
        assert gates.nand(0, 1) is True
        assert gates.nand(1, 0) is True
        assert gates.nand(1, 1) is False

    def test_nor(self):
        gates = gatehandler.GateHandler()
        assert gates.nor(0, 0) is True
        assert gates.nor(0, 1) is False
        assert gates.nor(1, 0) is False
        assert gates.nor(1, 1) is False

    def test_xor(self):
        gates = gatehandler.GateHandler()
        assert gates.xor(0, 0) is False
        assert gates.xor(0, 1) is True
        assert gates.xor(1, 0) is True
        assert gates.xor(1, 1) is False
