"""
greet_command.py

This module defines the `GreetCommand`, which implements a simple greeting command.
It follows the Command pattern and logs and prints a greeting message when executed.

Classes:
- GreetCommand: A command that logs and prints "Hello, World!".
"""
import logging
from app.commands import Command

class GreetCommand(Command):
    """A command that logs and prints a greeting message."""
    def execute(self):
        """Executes the greeting command.
        This method logs and prints "Hello, World!" to the console.
        It also demonstrates tuple and list initialization.
        """
        logging.info("Hello, World!")
        print("Hello, World!")
