import importlib
from enum import Enum
from math import *


class HistorySystem:
    def __init__(self):
        self.name = 'History'
        self.history = []


class CalculatingSystem:
    def __init__(self, history_sys: HistorySystem):
        self.name = 'Calculator'
        self.equation = ''
        self.for_eval = []
        self.result = ''
        self.history_sys = history_sys

    def eval(self) -> str:
        if not self.for_eval:
            return '0'
        try:
            result = eval(''.join(self.for_eval))
        except SyntaxError:
            return ''
        else:
            self.result = f'{result}'
            self.history_sys.history.append([self.equation, self.result])
            self.for_eval = list(f'{result}')
            return f'{result}'

    def clear(self):
        self.for_eval = []
        self.equation = ''
        self.result = ''
