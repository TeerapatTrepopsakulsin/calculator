"""Main block to run the program."""
from calculator_sys import CalculatingSystem, HistorySystem
from calculator_ui import CalculatorUI
from controller import Controller


history_sys = HistorySystem()
calculator = CalculatingSystem(history_sys)
controller = Controller(calculator)
ui = CalculatorUI(controller)
ui.run()
