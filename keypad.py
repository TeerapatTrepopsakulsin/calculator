import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import *


class Keypad(ttk.Frame):

    def __init__(self, parent, keynames=[], columns=1, **kwargs):
        super().__init__(parent, **kwargs)
        # keynames and columns
        self.keynames = keynames
        self.buttons = []
        self.frame = self.init_components(columns)

    def init_components(self, columns):
        """Create a keypad of keys using the keynames list.
        The first keyname is at the top left of the keypad and
        fills the available columns left-to-right, adding as many
        rows as needed.
        :param columns: number of columns to use
        """
        options = {'font': ('Georgia', 21)}
        sticky = {'sticky': tk.NSEW}
        pad = {'padx': 2, 'pady': 3}

        frame = ttk.Frame(self)

        for i in range(len(self.keynames)):
            num_button = tk.Button(frame, text=self.keynames[i], fg="Black", **options)
            row = i // columns
            col = i % columns
            num_button.grid(row=row, column=col, **pad, **sticky)
            self.buttons.append(num_button)

        frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        for i in range(len(self.keynames) // columns):
            frame.rowconfigure(i, weight=1)
        for i in range(columns):
            frame.columnconfigure(i, weight=1)

        return frame

    def bind(self, sequence, handler, add=''):
        """Bind an event handler to an event sequence."""
        for button in self.buttons:
            button.bind(sequence, handler, add)

    def __setitem__(self, key, value) -> None:
        """Overrides __setitem__ to allow configuration of all buttons
        using dictionary syntax.

        Example: keypad['foreground'] = 'red'
        sets the font color on all buttons to red.
        """
        for button in self.buttons:
            button.configure(key=value)

    def __getitem__(self, key):
        """Overrides __getitem__ to allow reading of configuration values
        from buttons.
        Example: keypad['foreground'] would return 'red' if the button
        foreground color is 'red'.
        """
        return self.buttons[0].config(key)[-1]

    def configure(self, cnf=None, **kwargs):
        """Apply configuration settings to all buttons.

        To configure properties of the frame that contains the buttons,
        use `keypad.frame.configure()`.
        """

    # TODO Write a property named 'frame' the returns a reference to
    # the the superclass object for this keypad.
    # This is so that a programmer can set properties of a keypad's frame,
    # e.g. keypad.frame.configure(background='blue')


if __name__ == '__main__':
    sticky = {'sticky': 'NSEW'}
    keys = list('789456123 0.')  # = ['7','8','9',...]

    root = tk.Tk()
    root.title("Keypad Demo")
    keypad = Keypad(root, keynames=keys, columns=3)
    keypad.pack(expand=True, fill=tk.BOTH)
    print(keypad['foreground'])
    # keypad.frame.configure(foreground='blue')
    root.mainloop()
