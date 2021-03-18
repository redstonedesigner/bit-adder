"""
Gate handler package, includes AND, NOT, OR, XOR, NAND, NOR
"""


class GateHandler:
    def __init__(self):
        pass

    @staticmethod
    def and_gate(a, b):
        return bool(a and b)

    @staticmethod
    def or_gate(a, b):
        return bool(a or b)

    @staticmethod
    def not_gate(a):
        return bool(not a)

    def nor(self, a, b):
        return self.not_gate(self.or_gate(a, b))

    def nand(self, a, b):
        return self.not_gate(self.and_gate(a, b))

    def xor(self, a, b):
        return True if (a and self.not_gate(b)) or (self.not_gate(a) and b) else False
