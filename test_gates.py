import gatehandler

class Tests:
    def __init__(self):
        self.gates = gatehandler.GateHandler()

    def test_nand(self):
        assert self.gates.nand(0, 0) is True
        assert self.gates.nand(0, 1) is True
        assert self.gates.nand(1, 0) is True
        assert self.gates.nand(1, 1) is False

    def test_nor(self):
        assert self.gates.nor(0, 0) is True
        assert self.gates.nor(0, 1) is False
        assert self.gates.nor(1, 0) is False
        assert self.gates.nor(1, 1) is False

    def test_xor(self):
        assert self.gates.xor(0, 0) is False
        assert self.gates.xor(0, 1) is True
        assert self.gates.xor(1, 0) is True
        assert self.gates.xor(1, 1) is False
