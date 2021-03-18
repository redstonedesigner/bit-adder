from lib import gatehandler


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

    def test_and(self):
        gates = gatehandler.GateHandler()
        assert gates.and_gate(0, 0) is False
        assert gates.and_gate(0, 1) is False
        assert gates.and_gate(1, 0) is False
        assert gates.and_gate(1, 1) is True

    def test_not(self):
        gates = gatehandler.GateHandler()
        assert gates.not_gate(0) is True
        assert gates.not_gate(1) is False

    def test_or(self):
        gates = gatehandler.GateHandler()
        assert gates.or_gate(0, 0) is False
        assert gates.or_gate(0, 1) is True
        assert gates.or_gate(1, 0) is True
        assert gates.or_gate(1, 1) is True
