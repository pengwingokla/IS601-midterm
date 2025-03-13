"""
command_handler.py

This module defines the Command pattern for executing various operations dynamically. 
It includes an abstract base class `Command` for defining executable commands 
and a `CommandHandler` class for managing and executing registered commands.

Classes:
    - Command: Abstract base class for all commands.
    - CommandHandler: Manages the registration and execution of commands.

Usage:
    To create a new command, subclass `Command` and implement the `execute` method.
    Register commands using `CommandHandler.register_command()`, and execute them 
    dynamically using `CommandHandler.execute_command()`.

"""
from abc import ABC, abstractmethod

class Command(ABC):
    """Command object"""
    @abstractmethod
    def execute(self, *args):
        """General execution function"""
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
