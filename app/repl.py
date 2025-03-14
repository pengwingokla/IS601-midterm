"""
calculator_repl.py
This module defines the `CalculatorREPL` class, which implements a
command-line Read-Eval-Print Loop (REPL) for an advanced calculator.
It supports basic arithmetic operations, history management,
plugin loading, and command handling.
Classes:
    - CalculatorREPL: Implements the interactive calculator REPL.

Usage:
    Run this script to start the REPL for the calculator.

Example:
    python calculator_repl.py
"""

import logging
from commands.calculator import Calculator
from plugins.plugin_loader import PluginLoader
from history_manager import HistoryManager


class CalculatorREPL:
    """Command-Line REPL for the Advanced Calculator."""

    def __init__(self):
        """Initializes the calculator REPL.

        Attributes:
            calculator (Calculator): The core calculator object.
            history_manager (HistoryManager): Manages operation history.
            plugin_loader (PluginLoader): Loads and manages plugins.
            commands (dict): Maps command names to their handler functions.
        """
        self.calculator = Calculator()
        self.history_manager = HistoryManager()
        self.plugin_loader = PluginLoader()
        self.commands = {
            "add": self.add,
            "sub": self.subtract,
            "mul": self.multiply,
            "div": self.divide,
            "history": self.show_history,
            "clear": self.clear_history,
            "exit": self.exit_repl,
            "help": self.show_help,
            "menu": self.show_plugins
        }
        self.plugin_loader.load_plugins(self.commands)

    def run(self):
        """Starts the interactive REPL loop for the calculator."""
        print("Welcome to the Advanced Calculator REPL. \
              Type 'help' for commands.")
        while True:
            try:
                user_input = input("calc> ").strip()
                if not user_input:
                    continue
                command, *args = user_input.split()
                if command in self.commands:
                    self.commands[command](*args)
                else:
                    print(f"Unknown command: {command}. \
                          Type 'help' for a list of commands.")
            except Exception as e:
                logging.error("Error in REPL: %s", e)
                print(f"An error occurred: {e}")

    def add(self, *args):
        """Performs addition of given numbers.

        Args:
            *args (str): Numbers to be added.

        Returns:
            None. Prints the result and saves it in history.
        """
        result = self.calculator.add(*map(float, args))
        print(f"Result: {result}")
        self.history_manager.save_operation("add", args, result)

    def subtract(self, *args):
        """Performs subtraction of given numbers.

        Args:
            *args (str): Numbers to be subtracted.

        Returns:
            None. Prints the result and saves it in history.
        """
        result = self.calculator.subtract(*map(float, args))
        print(f"Result: {result}")
        self.history_manager.save_operation("sub", args, result)

    def multiply(self, *args):
        """Performs multiplication of given numbers.

        Args:
            *args (str): Numbers to be multiplied.

        Returns:
            None. Prints the result and saves it in history.
        """
        result = self.calculator.multiply(*map(float, args))
        print(f"Result: {result}")
        self.history_manager.save_operation("mul", args, result)

    def divide(self, *args):
        """Performs division of given numbers.

        Args:
            *args (str): Numbers to be divided.

        Returns:
            None. Prints the result and saves it in history.

        Raises:
            ZeroDivisionError: If division by zero is attempted.
        """
        try:
            result = self.calculator.divide(*map(float, args))
            print(f"Result: {result}")
            self.history_manager.save_operation("div", args, result)
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")

    def show_history(self):
        """Displays the calculation history."""
        print(self.history_manager.get_history())

    def clear_history(self):
        """Clears the stored calculation history."""
        self.history_manager.clear_history()
        print("History cleared.")

    def show_help(self):
        """Displays a list of available commands."""
        print("\nAvailable Commands:")
        for cmd in self.commands:
            print(f"- {cmd}")

    def show_plugins(self):
        """Displays a list of available plugins."""
        print("\nAvailable Plugins:")
        for plugin in self.plugin_loader.get_plugin_names():
            print(f"- {plugin}")

    def exit_repl(self):
        """Exits the REPL loop and terminates the program."""
        print("Exiting calculator...")
        exit()


if __name__ == "__main__":
    CalculatorREPL().run()
