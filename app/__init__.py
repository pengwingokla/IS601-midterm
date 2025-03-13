""" This is the docstring """
import os
import pkgutil
import importlib
import sys
from commands import CommandHandler, Command
from dotenv import load_dotenv
import logging
import logging.config
from commands.calculator import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

class App:
    def __init__(self):
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()
        self.register_calculator_commands()
        
        # Debug: Log registered commands at startup
        logging.info(f"Registered commands: {list(self.command_handler.commands.keys())}")
        print("DEBUG: Registered commands ->", list(self.command_handler.commands.keys()))

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)

    def load_plugins(self):
        plugins_package = 'plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            logging.warning(f"Plugins directory '{plugins_path}' not found.")
            return
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    self.register_plugin_commands(plugin_module, plugin_name)
                except ImportError as e:
                    logging.error(f"Error importing plugin {plugin_name}: {e}")

    def register_plugin_commands(self, plugin_module, plugin_name):
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                self.command_handler.register_command(plugin_name, item())
                logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")

    def register_calculator_commands(self):
        """Registers calculator commands directly inside `app/__init__.py` to avoid circular imports."""
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("sub", SubtractCommand())
        self.command_handler.register_command("mul", MultiplyCommand())
        self.command_handler.register_command("div", DivideCommand())
        logging.info("Calculator commands registered successfully.")

    def start(self):
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
                    result = self.command_handler.execute_command(command_name, *args)
                    if result is not None:
                        print(f"Result: {result}")
                except KeyError:
                    logging.error(f"Unknown command: {command_name}")
                    print(f"Unknown command: {command_name}")
                except ValueError as ve:
                    logging.error(f"ValueError: {ve}")
                    print(f"Error: {ve}")

        except KeyboardInterrupt:
            logging.info("Application interrupted and exiting gracefully.")
            sys.exit(0)
        except Exception as e:
            logging.error(f"Error: {e}")
            print(f"Error: {e}")

if __name__ == "__main__":
    app = App()
    app.start()
