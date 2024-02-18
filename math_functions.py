"""Enum class of Mathematics functions"""
from enum import Enum


class MathOperators(Enum):
    """Enum class which store the expression of operators in difference use as a list,
    index 0 is shown on the button,
    index 1 is shown in the label
    and index 2 is use for evaluation.
    """
    # OPERATOR = [for button, in label, for eval]
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
        """Return a list of index 1 and to if item is index 0"""
        for _function in MathOperators:
            if _function.value[0] == item:
                return _function.value[1:]
        return None


class MathFunctions(Enum):
    """Enum class which store the expression of operators in difference use as a list,
    index 0 is shown in the combobox,
    index 1 is shown in the label
    and index 2 is use for evaluation.
    """
    # FUNCTION = [for combobox, in label, for eval]
    EXP = ['exp', 'exp(', 'exp(']
    LN = ['ln', 'ln(', 'log(']
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
        """Return a list of index 1 and to if item is index 0"""
        for _function in MathFunctions:
            if _function.value[0] == item:
                return _function.value[1:]
        return None
