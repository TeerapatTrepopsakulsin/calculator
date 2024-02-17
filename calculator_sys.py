import importlib
from enum import Enum
from math import *
# from calculator_ui import CalculatorUI
importlib.import_module('CalculatorUI')


class HistorySystem:
    def __init__(self):
        self.name = 'History'
        self.history = []

    def clear(self):
        self.history = []


class CalculatingSystem:
    def __init__(self, ui: CalculatorUI, history_sys: HistorySystem):
        self.name = 'Calculator'
        self.equation = ''
        self.result = ''
        self.history_sys = history_sys
        self.ui = ui

    def eval(self):
        try:
            result = eval(self.equation)
        except TypeError:
            return
        else:
            self.result = f'{result}'
            self.history_sys.history.append([self.equation, self.result])
            return result

    # @staticmethod
    # def get_functions():
    #     return [i.value for i in MathFunctions]


if __name__ == '__main__':
    text = "log2(8)"
    print('Hello, world!')
