import tkinter as tk
from tkinter import ttk, Grid
from calculator.keypad import Keypad
from calculator.math_functions import *
from calculator.controller import Controller
from calculator.calculator_sys import CalculatingSystem, HistorySystem


class CalculatorUI(tk.Tk):
    def __init__(self, controller: Controller):
        super().__init__()
        self.title("Calculator")
        self.controller = controller

        self.shown = ''

        self.function = tk.StringVar()

        self.init_components()

    def handle_num_press(self, event: tk.Event):
        self.label['text'] += event.widget['text']

    def handle_op_press(self, event: tk.Event):
        self.label['text'] += MathOperators.get(event.widget['text'])[0]

    def handle_clr_press(self, *args):
        self.label.configure(text='')

    def handle_dlt_press(self, *args):
        self.label['text'] = self.label['text'][:-1]
        while self.label['text'] and self.label['text'][-1].isalpha():
            self.label['text'] = self.label['text'][:-1]

    def handle_eq_press(self, *args):
        result = self.controller.handle_calculate(*args)
        self.label.configure(text=result)

    def init_components(self):
        """Create components and layout the UI."""
        font = {'font': ('Georgia', 21)}
        big_font = {'font': ('Verdana', 42)}
        sticky = {'sticky': tk.NSEW}
        pad = {'padx': 3, 'pady': 2}

        # frame
        num_keys = list('789456123 0.')  # = ['7','8','9',...]
        math_sym = ['(', ')', '*', '/', '+', '-', '^', 'mod']
        equal_key = ['=']
        del_key = ['DEL']
        clr_key = ['CLR']
        self.numpad = Keypad(self, keynames=num_keys, columns=3)
        self.operator = Keypad(self, keynames=math_sym, columns=2)
        self.equal = Keypad(self, keynames=equal_key, columns=1)
        self.dlt = Keypad(self, keynames=del_key, columns=1)
        self.clr = Keypad(self, keynames=clr_key, columns=1)

        self.numpad.grid(row=3, column=0, rowspan=2, **pad, **sticky)
        self.operator.grid(row=3, column=1, columnspan=2, **pad, **sticky)
        self.equal.grid(row=4, column=1, columnspan=2, **pad, **sticky)
        self.dlt.grid(row=2, column=1, **pad, **sticky)
        self.clr.grid(row=2, column=2, **pad, **sticky)

        self.numpad.bind('<Button>', self.handle_num_press)
        self.operator.bind('<Button>', self.handle_op_press)
        self.dlt.bind('<Button>', self.handle_dlt_press)
        self.clr.bind('<Button>', self.handle_clr_press)

        # label
        self.label = tk.Label(self, bg='black', fg='yellow', text=self.shown, anchor='e', **big_font)
        self.label.grid(row=1, column=0, columnspan=3, **sticky)

        # combobox
        self.combobox = ttk.Combobox(self, textvariable=self.function, **font)
        self.combobox.grid(row=2, column=0, **sticky)

        func_for_cal = [i.value for i in MathFunctions]
        func_show = [i[0] for i in func_for_cal]
        self.combobox['value'] = func_show

        # scroll bar & text
        self.history_box = tk.Text(self, height=10)
        self.history_box.grid(row=0, column=0, **sticky)

        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command='yscrollcommand')
        self.scrollbar.grid(row=0, column=1, **sticky)

        # fill the window
        for i in range(5):
            self.rowconfigure(i, weight=1)
        for i in range(3):
            self.columnconfigure(i, weight=1)

    def run(self):
        """start the app, wait for events"""
        self.mainloop()


if __name__ == '__main__':
    sticky = {'sticky': 'NSEW'}
    num_keys = list('789456123 0.')  # = ['7','8','9',...]
    math_sym = ['(', ')', '*', '/', '+', '-', '^', 'mod']
    equal_key = ['=']
    del_key = ['DEL']
    clr_key = ['CLR']

    history_sys = HistorySystem()
    calculator = CalculatingSystem(history_sys)
    controller = Controller(calculator)
    ui = CalculatorUI(controller)
    ui.run()
