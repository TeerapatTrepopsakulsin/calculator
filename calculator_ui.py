import tkinter
import tkinter as tk
from tkinter import ttk
from keypad import Keypad


class CalculatorUI(tk.Tk):
    """User Interface for a unit converter.

    The UI displays units and handles user interaction.  It invokes
    a UnitConverter object to perform actual unit conversions.
    """

    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.keypad = Keypad(self, keynames=keys, columns=3)

        self.shown = ''

        self.init_components()

    def calculate_handler(self, *args):
        """An event handler for conversion actions.
        You should call the unit converter to perform actual conversion.
        """
        pass

    def handle_press(self, event: tk.Event):
        self.label['text'] += event.widget['text']

    def clear(self, *args):
        pass

    def clear_command(self):
        self.calculator.clear()
        self.shown.set("")
    # bind the method to a key on the calculator UI
    #clear_key = tk.Button(self, text="Clear", command = clear_command)

    def init_components(self):
        """Create components and layout the UI."""
        options = {'font': ('Georgia', 21)}
        sticky = {'sticky': tk.NSEW}
        pad = {'padx': 3, 'pady': 2}
        self.keypad.grid(row=1, column=0, **pad, **sticky)
        self.keypad.bind('<Button>', self.handle_press)
        # Components

        # label
        self.label = tk.Label(self, bg='black', fg='yellow', text=self.shown, **options)
        self.label.grid(row=0, column=0, **sticky)

    def run(self):
        """start the app, wait for events"""
        self.mainloop()


if __name__ == '__main__':
    sticky = {'sticky': 'NSEW'}
    keys = list('789456123 0.')  # = ['7','8','9',...]

    calculator = CalculatorUI()
    calculator.run()