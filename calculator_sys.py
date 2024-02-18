"""Calculator model for calculating and others"""
from math import *
import warnings


class HistorySystem:
    """CLass for storing the calculating history"""
    def __init__(self):
        self.name = 'History'
        self.history = []

    def clear(self):
        """Clear history."""
        self.history = []

    def __getitem__(self, index):
        return self.history[index]


class CalculatingSystem:
    """CLass for calculating."""
    def __init__(self, history_sys: HistorySystem):
        self.name = 'Calculator'
        self.equation = ''
        self.for_eval = []
        self.result = ''
        self.history_sys = history_sys

    def evaluate(self) -> str:
        """Evaluate for_eval attribute and returns a result as a string.

        :returns: str of evaluation result
        """
        if not self.for_eval:
            self.history_sys.history.append(['0', '0'])
            return '0'
        try:
            result = eval(''.join(self.for_eval))
        except Exception:
            return ''
        self.result = f'{result:.12g}'
        self.history_sys.history.append([self.equation, self.result])
        self.for_eval = list(f'{result:.12g}')
        return f'{result:.12g}'

    def clear(self):
        """Clear all attributes."""
        self.for_eval = []
        self.equation = ''
        self.result = ''


warnings.simplefilter('ignore')
