from lib import gatehandler


class HalfAdder:
    def __init__(self, a, b):
        gates = gatehandler.GateHandler()
        self.s = int(gates.xor(a, b))
        self.c = int(gates.and_gate(a, b))


class FullAdder:
    def __init__(self, a, b, c):
        gates = gatehandler.GateHandler()
        adder1 = HalfAdder(a, b)
        d = adder1.s
        f = adder1.c
        adder2 = HalfAdder(d, c)
        e = adder2.c
        self.c = int(gates.or_gate(f, e))
        self.s = int(adder2.s)
