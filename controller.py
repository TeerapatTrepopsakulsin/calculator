import tkinter as tk
from calculator_sys import CalculatingSystem
from math_functions import MathOperators


class Controller:
    def __init__(self, calculating_sys: CalculatingSystem):
        self.calculator = calculating_sys

    def handle_num_press(self, event: tk.Event):
        self.calculator.for_eval.append(event.widget['text'])

    def handle_op_press(self, event: tk.Event):
        self.calculator.for_eval.append(MathOperators.get(event.widget['text'])[1])

    def handle_func_press(self, *args):
        if self.calculator.for_eval and self.calculator.for_eval[-1].isdecimal():
            self.calculator.for_eval = [*args] + self.calculator.for_eval + [')']
        else:
            self.calculator.for_eval += [*args]

    def handle_clr_press(self, *args):
        self.calculator.clear()

    def handle_dlt_press(self, *args):
        while len(self.calculator.for_eval) >= 1 and self.calculator.for_eval[-1].isalpha():
            self.calculator.for_eval.pop()

    def handle_calculate(self, *args):
        self.calculator.equation = str(*args)
        result = self.calculator.eval()
        return result
