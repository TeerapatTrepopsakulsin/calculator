import importlib
from enum import Enum
from math import *


class HistorySystem:
    def __init__(self):
        self.name = 'History'
        self.history = []

    def clear(self):
        self.history = []


class CalculatingSystem:
    def __init__(self, history_sys: HistorySystem):
        self.name = 'Calculator'
        self.equation = ''
        self.result = ''
        self.history_sys = history_sys

    def eval(self) -> str:
        try:
            result = eval(self.equation)
        except TypeError:
            return ''
        else:
            self.result = f'{result}'
            self.history_sys.history.append([self.equation, self.result])
            return f'{result}'

    def clear(self):
        self.equation = ''
        self.result = ''
        self.history_sys.clear()


if __name__ == '__main__':
    text = "log8(8)"
    print(eval(text))
    print('Hello, world!')
