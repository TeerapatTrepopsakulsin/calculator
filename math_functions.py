from enum import Enum
from math import *


class MathOperators(Enum):
    # FUNCTION = [for button, in label, for eval]
    O_PAREN = ['(', '(', '(']
    C_PAREN = [')', ')', ')']
    MUL = ['*', '*', '*']
    DIV = ['/', '/', '/']
    ADD = ['+', '+', '+']
    SUB = ['-', '-', '-']
    POWER = ['^', '^', '**']
    MOD = ['mod', 'mod(', '%(']

    @property
    def expression(self):
        return self.value

    def __str__(self):
        return self.name

    @staticmethod
    def get(item):
        for _function in MathOperators:
            if _function.value[0] == item:
                return _function.value[1:]


class MathFunctions(Enum):
    # FUNCTION = [for button, in label, for eval]
    EXP = ['exp', 'exp(', 'exp(']
    LN = ['ln', 'log(', 'log(']
    LOG10 = ['log10', 'log10(', 'log10(']
    LOG2 = ['log2', 'log2(', 'log2(']
    SQRT = ['sqrt', 'sqrt(', 'sqrt(']

    @property
    def expression(self):
        return self.value

    def __str__(self):
        return self.name

    @staticmethod
    def get(item):
        for _function in MathFunctions:
            if _function.value[0] == item:
                return _function.value[1:]
