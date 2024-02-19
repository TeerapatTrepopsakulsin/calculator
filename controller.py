"""Controller module, use for invoking calculating system"""
import tkinter as tk
from calculator_sys import CalculatingSystem
from math_functions import MathOperators


class Controller:
    """Controller class, use for invoking calculating system."""
    def __init__(self, calculating_sys: CalculatingSystem):
        self.calculator = calculating_sys

    def handle_num_press(self, event: tk.Event):
        """Append the pressed number to the calculating system."""
        self.calculator.for_eval.append(event.widget['text'])

    def handle_op_press(self, event: tk.Event):
        """Append the pressed operator to the calculating system."""
        self.calculator.for_eval.append(MathOperators.get(event.widget['text'])[1])

    def handle_func_press(self, *args):
        """Append the selected function to the calculating system.

        :param: arg: str of selected function"""
        if self.calculator.for_eval and self.calculator.for_eval[-1].isdecimal():
            self.calculator.for_eval = [*args] + self.calculator.for_eval + [')']
        else:
            self.calculator.for_eval += [*args]

    def handle_clr_press(self, *args):
        """Clear the calculating system."""
        self.calculator.clear()

    def handle_dlt_press(self, *args):
        """Delete the last value in the calculating system."""
        if self.calculator.for_eval:
            self.calculator.for_eval.pop()
        while self.calculator.for_eval and self.calculator.for_eval[-1].isalpha():
            self.calculator.for_eval.pop()

    def handle_calculate(self, *args) -> str:
        """Received an equation and return the evaluated value from the calculating system.

        :param: arg: str of equation
        :return: str of evaluated value
        """
        self.calculator.equation = str(*args)
        result = self.calculator.evaluate()
        return result

    def handle_his_click(self, *args):
        """Set the clicked value to the calculating system

        :param: arg: str of clicked value
        """
        self.calculator.for_eval = list(*args)

    def get_last_history(self):
        """Get last history, convert it into text, then return it"""
        last_history = self.calculator.history_sys[-1]
        last_history_text = '\n' + last_history[0] + '\n = ' + last_history[1] + '\n'
        return last_history_text

    def recall_history(self, index):
        """Get the specific history according to the given index"""
        return self.calculator.history_sys[index]

    def get_len_history(self):
        """Get the length of history"""
        return len(self.calculator.history_sys.history)
