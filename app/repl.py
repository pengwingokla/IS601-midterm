import readline
import logging
from commands.calculator import Calculator
from plugins.plugin_loader import PluginLoader
from history_manager import HistoryManager


class CalculatorREPL:
    """Command-Line REPL for the Advanced Calculator."""

    def __init__(self):
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
        """Start the REPL loop."""
        print("Welcome to the Advanced Calculator REPL. Type 'help' for commands.")
        while True:
            try:
                user_input = input("calc> ").strip()
                if not user_input:
                    continue
                command, *args = user_input.split()
                if command in self.commands:
                    self.commands[command](*args)
                else:
                    print(f"Unknown command: {command}. Type 'help' for a list of commands.")
            except Exception as e:
                logging.error(f"Error in REPL: {e}")
                print(f"An error occurred: {e}")

    def add(self, *args):
        result = self.calculator.add(*map(float, args))
        print(f"Result: {result}")
        self.history_manager.save_operation("add", args, result)

    def subtract(self, *args):
        result = self.calculator.subtract(*map(float, args))
        print(f"Result: {result}")
        self.history_manager.save_operation("sub", args, result)

    def multiply(self, *args):
        result = self.calculator.multiply(*map(float, args))
        print(f"Result: {result}")
        self.history_manager.save_operation("mul", args, result)

    def divide(self, *args):
        try:
            result = self.calculator.divide(*map(float, args))
            print(f"Result: {result}")
            self.history_manager.save_operation("div", args, result)
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")

    def show_history(self):
        print(self.history_manager.get_history())

    def clear_history(self):
        self.history_manager.clear_history()
        print("History cleared.")

    def show_help(self):
        print("\nAvailable Commands:")
        for cmd in self.commands:
            print(f"- {cmd}")

    def show_plugins(self):
        print("\nAvailable Plugins:")
        for plugin in self.plugin_loader.get_plugin_names():
            print(f"- {plugin}")

    def exit_repl(self):
        print("Exiting calculator...")
        exit()


if __name__ == "__main__":
    CalculatorREPL().run()
