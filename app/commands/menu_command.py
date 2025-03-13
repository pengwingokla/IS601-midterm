"""
history_commands.py

This module defines Include a REPL "Menu" command to list all available 
plugin commands, ensuring user discoverability and interaction.
"""
from commands import Command

class MenuCommand(Command):
    """Command to list all available plugin commands."""
    def __init__(self, command_handler):
        """Stores reference to command handler to list available commands."""
        self.command_handler = command_handler

    def execute(self, *args):
        """Displays all available commands."""
        return "Available Commands:\n" + "\n".join(f" - {cmd}" for cmd in self.command_handler.commands.keys())
