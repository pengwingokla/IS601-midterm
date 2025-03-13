""""
Calculator Application
"""
import os
import pkgutil
import importlib
import logging.config
import sys
from commands import CommandHandler, Command
from dotenv import load_dotenv
from commands.menu_command import MenuCommand
from commands.calculator import (
    AddCommand,
    SubtractCommand,
    MultiplyCommand,
    DivideCommand,
)
from commands.history_commands import HistoryCommand, ClearHistoryCommand, DeleteHistoryCommand
from history_manager import HistoryManager


class App:
    """ This is the main class of the calculator application"""
    def __init__(self):
        os.makedirs('logs', exist_ok=True)
        os.makedirs('data', exist_ok=True)
        os.makedirs('app/plugins', exist_ok=True)

        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')

        self.command_handler = CommandHandler()
        self.history_manager = HistoryManager()
        self.register_calculator_commands()
        self.register_history_commands()
        self.load_plugins()
        self.register_command_menu()

        logging.info("Registered commands: %s", list(self.command_handler.commands.keys()))

    def configure_logging(self):
        """
        Logs in terminal
        """
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(
                logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(
                level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        """ Load environment variables"""
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        """ Get environment variable"""
        return self.settings.get(env_var, None)

    def load_plugins(self):
        """ Plugin loader """
        plugins_package = 'plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            logging.warning("Plugins directory %s not found.", plugins_path)
            return
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                try:
                    plugin_module = importlib.import_module(
                        f'{plugins_package}.{plugin_name}')
                    self.register_plugin_commands(plugin_module, plugin_name)
                except ImportError as e:
                    logging.error("Error importing plugin %s: %s", plugin_name, e)

    def register_plugin_commands(self, plugin_module, plugin_name):
        """ Function to register plugin commands """
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                self.command_handler.register_command(plugin_name, item())
                logging.info("Command %s from plugin %s registered.", plugin_name, plugin_name)

    def register_command_menu(self):
        """Registers the 'menu' command properly."""
        self.command_handler.register_command(
            "menu", MenuCommand(self.command_handler))

    def register_calculator_commands(self):
        """Registers calculator commands directly inside `app/__init__.py` to avoid circular imports."""
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("sub", SubtractCommand())
        self.command_handler.register_command("mul", MultiplyCommand())
        self.command_handler.register_command("div", DivideCommand())
        logging.info("Calculator commands registered successfully.")

    def register_history_commands(self):
        """Registers history-related commands."""
        self.command_handler.register_command("history", HistoryCommand())
        self.command_handler.register_command("clrhis", ClearHistoryCommand())
        self.command_handler.register_command("delhis", DeleteHistoryCommand())

    def show_history(self, *args):
        """Displays calculation history."""
        history_df = self.history_manager.get_history()
        if history_df.empty:
            print("No history available.")
        else:
            print(history_df.to_string(index=True))

    def clear_history(self, *args):
        """Clears calculation history."""
        self.history_manager.clear_history()
        print("Calculation history cleared.")

    def delete_history_entry(self, *args):
        """Deletes a specific history entry by index."""
        if len(args) != 1:
            print("Usage: delete_history <index>")
            return
        try:
            index = int(args[0])
            if self.history_manager.delete_history_entry(index):
                print(f"Deleted history entry {index}.")
            else:
                print(f"No history entry at index {index}.")
        except ValueError:
            print("Error: Index must be a number.")

    def start(self):
        """ Function when starting application """
        self.load_plugins()
        logging.info("Application started. Type 'exit' to exit.")
        try:
            while True:
                cmd_input = input(">>> ").strip()
                if cmd_input.lower() == 'exit':
                    logging.info("Application exit.")
                    sys.exit(0)

                command_parts = cmd_input.split()
                if not command_parts:
                    continue

                command_name = command_parts[0]
                args = command_parts[1:]

                # Debugging command execution
                # logging.info(f"Received command: {command_name} with args: {args}")
                # print(f"DEBUG: Command -> {command_name}, Args -> {args}")

                try:
                    # Ensure arguments are passed correctly
                    result = self.command_handler.execute_command(
                        command_name, *args)
                    if result is not None:
                        print(f"Result: {result}")
                        self.history_manager.save_operation(
                            command_name, args, result)
                except KeyError:
                    logging.error("Unknown command: %s", command_name)
                    print(f"Unknown command: {command_name}")
                except ValueError as ve:
                    logging.error("ValueError: %s", ve)
                    print(f"Error: {ve}")

        except KeyboardInterrupt:
            logging.info("Application interrupted and exiting gracefully.")
            sys.exit(0)
        except ValueError as ve:
            logging.error("ValueError: %s", ve)
            print(f"Error: {ve}")



if __name__ == "__main__":
    app = App()
    app.start()
