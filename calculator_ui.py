"""UI for calculator programme"""
import tkinter as tk
from tkinter import ttk, scrolledtext
from winsound import MessageBeep, SND_NOWAIT
from keypad import Keypad
from math_functions import MathOperators, MathFunctions
from controller import Controller


class CalculatorUI(tk.Tk):
    """Class of the UI of the calculator"""
    def __init__(self, controller: Controller):
        super().__init__()
        self.title("Calculator")
        self.controller = controller

        self.function = tk.StringVar()

        self.init_components()

    def handle_num_press(self, event: tk.Event):
        """Method which executed when pressing number button.
        Display the number.
        """
        self.label['text'] += event.widget['text']
        self.controller.handle_num_press(event)

    def handle_op_press(self, event: tk.Event):
        """Method which executed when pressing operator button.
        Display the operator.
        """
        self.label['text'] += MathOperators.get(event.widget['text'])[0]
        self.controller.handle_op_press(event)

    def handle_func_press(self, *args):
        """Method which executed when select function from combobox.
        Display the function.
        """
        _func = MathFunctions.get(self.function.get())
        if self.label['text'] and self.label['text'][-1].isdecimal():
            self.label['text'] = _func[0] + self.label['text'] + ')'
        else:
            self.label['text'] += _func[0]
        self.focus_set()
        self.function.set('Functions')
        self.controller.handle_func_press(_func[1])

    def handle_clr_press(self, *args):
        """Method which executed when pressing CLR button.
        Clears the input.
        """
        self.label.configure(text='', foreground='yellow')
        self.controller.handle_clr_press()

    def handle_dlt_press(self, *args):
        """Method which executed when pressing DEL button.
        Delete the last input value.
        """
        self.label['text'] = self.label['text'][:-1]
        while self.label['text'] and self.label['text'][-1].isalpha():
            self.label['text'] = self.label['text'][:-1]
        if not self.label['text']:
            self.label.configure(foreground='yellow')
        self.controller.handle_dlt_press()

    def handle_eq_press(self, *args):
        """Method which executed when pressing equal button.
        valuate wherever is shown on the display.
        If the expression is valid, then add it to the history.
        If the expression is invalid, then change the color of the display,
        make a sound, but don't add it to the history.
        """
        result = self.controller.handle_calculate(self.label['text'])
        if not result:
            self.label.configure(foreground='red')
            MessageBeep(SND_NOWAIT)
        else:
            self.label.configure(foreground='yellow', text=result)
            history_text = self.controller.get_last_history()
            self.history_box.configure(state='normal')
            self.history_box.insert(0.0, history_text)
            self.history_box.configure(state='disabled')

    def handle_his_click(self, event: tk.Event, *args):
        self.history_box.configure(state='normal')
        print()
        print(event)
        print(event.widget['x'])
        self.history_box.focus_set()
        self.history_box.getint(5)
        try:
            print('index')
            a = self.history_box.get(1.0, 'sel.first')

        except tk.TclError:
            print('except')
        # self.label['text'] = self.history_box.get()
        self.history_box.configure(state='disabled')

    def init_components(self):
        """Create components and layout the UI."""
        font = {'font': ('Georgia', 21)}
        big_font = {'font': ('Verdana', 42)}
        sticky = {'sticky': tk.NSEW}
        pad = {'padx': 3, 'pady': 2}

        # keypad
        num_keys = list('789456123 0.')  # = ['7','8','9',...]
        math_sym = [i.value[0] for i in MathOperators]
        self.numpad = Keypad(self, keynames=num_keys, columns=3)
        self.operator = Keypad(self, keynames=math_sym, columns=2)
        self.equal = Keypad(self, keynames=['='], columns=1)
        self.dlt = Keypad(self, keynames=['DEL'], columns=1)
        self.clr = Keypad(self, keynames=['CLR'], columns=1)

        self.operator.configure(fg='green')
        self.equal.configure(fg='white', bg='green')
        self.dlt.configure(fg='green')
        self.clr.configure(fg='green')

        self.numpad.grid(row=3, column=0, rowspan=2, **pad, **sticky)
        self.operator.grid(row=3, column=1, columnspan=2, **pad, **sticky)
        self.equal.grid(row=4, column=1, columnspan=2, **pad, **sticky)
        self.dlt.grid(row=2, column=1, **pad, **sticky)
        self.clr.grid(row=2, column=2, **pad, **sticky)

        self.numpad.bind('<Button>', self.handle_num_press)
        self.operator.bind('<Button>', self.handle_op_press)
        self.equal.bind('<Button>', self.handle_eq_press)
        self.dlt.bind('<Button>', self.handle_dlt_press)
        self.clr.bind('<Button>', self.handle_clr_press)

        # label
        self.label = tk.Label(self, bg='black', fg='yellow', anchor='e', **big_font)
        self.label.grid(row=1, column=0, columnspan=3, **sticky)

        # combobox
        func_for_cal = [i.value[0] for i in MathFunctions]
        self.combobox = ttk.Combobox(self, textvariable=self.function, values=func_for_cal, state='readonly', **font)
        self.combobox.grid(row=2, column=0, **sticky)

        self.combobox.bind_all('<<ComboboxSelected>>', self.handle_func_press)

        self.function.set('Functions')

        # scrolledText
        self.history_box = scrolledtext.ScrolledText(self, height=5, width=10, font=('Segoe UI Black', 21), state='disabled')
        self.history_box.bind('<Button-1>', self.handle_his_click)
        self.history_box.grid(row=0, column=0, columnspan=3, **sticky)

        # fill the window
        for row in range(5):
            self.rowconfigure(row, weight=1)
        for col in range(3):
            self.columnconfigure(col, weight=1)

    def run(self):
        """start the app, wait for events"""
        self.mainloop()


if __name__ == '__main__':
    from itertools import chain


    def get_events(widget):
        return set(chain.from_iterable(widget.bind_class(cls) for cls in widget.bindtags()))


    root = tk.Tk()
    a = get_events(scrolledtext.ScrolledText())
    for i in a:
        print(i)
    root.destroy()
