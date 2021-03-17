"""
Gate handler package, includes AND, NOT, OR, XOR, NAND, NOR
"""


class GateHandler:
    def __init__(self):
        pass

    @staticmethod
    def _and(a, b):
        return a and b

    @staticmethod
    def _or(a, b):
        return a or b

    @staticmethod
    def _not(a):
        return not a

    def nor(self, a, b):
        return self._not(self._or(a, b))

    def nand(self, a, b):
        return self._not(self._or(a, b))

    def xor(self, a, b):
        return True if (a and self._not(b)) or (self._not(a) and b) else False
