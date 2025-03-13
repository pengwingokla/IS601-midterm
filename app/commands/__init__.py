from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        pass

class CommandHandler:
    """Handles command execution dynamically."""
    
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        """Register a command with the handler."""
        self.commands[command_name] = command

    def execute_command(self, command_name: str, *args):
        """Execute a registered command if it exists."""
        if command_name in self.commands:
            try:
                # ✅ Convert arguments to numbers (floats) before execution
                converted_args = [float(arg) for arg in args]  
                return self.commands[command_name].execute(*converted_args)
            except ValueError:
                raise ValueError(f"Invalid input: Arguments must be numbers. Got: {args}")
        else:
            raise KeyError(f"No such command: {command_name}")
