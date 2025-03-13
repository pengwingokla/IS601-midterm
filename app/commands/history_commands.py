"""
history_commands.py

This module defines commands for managing and interacting with the calculation history. 
It includes commands to view, clear, and delete history entries, utilizing the `HistoryManager`.

Classes:
    - HistoryCommand: Retrieves and displays the calculation history.
    - ClearHistoryCommand: Clears the entire calculation history.
    - DeleteHistoryCommand: Deletes a specific entry from the history by index.

Usage:
    These command classes are designed to be used with a `CommandHandler`, 
    allowing dynamic execution of history-related commands.
"""

from commands import Command
from history_manager import HistoryManager

class HistoryCommand(Command):
    """Command to retrieve and display the calculation history."""
    def execute(self, *args):
        """Executes the command to retrieve history.
        Args:
            *args: Unused arguments (included for compatibility).
        Returns:
            str: A string representation of the calculation history.
                 If the history is empty, returns a message indicating so.
        """
        history_manager = HistoryManager()
        history = history_manager.get_history()
        if history.empty:
            return "No history available."
        return history.to_string(index=True)

class ClearHistoryCommand(Command):
    """Command to clear the entire calculation history."""
    def execute(self, *args):
        """Executes the command to clear history.
        Args:
            *args: Unused arguments (included for compatibility).
        Returns:
            str: Confirmation message indicating the history has been cleared.
        """
        history_manager = HistoryManager()
        history_manager.clear_history()
        return "Calculation history cleared."

class DeleteHistoryCommand(Command):
    """Command to delete a specific calculation history entry by index."""
    def execute(self, *args):
        """Executes the command to delete a history entry.
        Args:
            *args (str): A single argument representing the index of the entry to delete.
        Returns:
            str: Success or error message indicating the result of the deletion.
        Raises:
            ValueError: If the provided index is not a valid number.
        """
        if len(args) != 1:
            return "Usage: delhis <index>"

        try:
            index = int(args[0])
            history_manager = HistoryManager()
            if history_manager.delete_history_entry(index):
                return f"Deleted history entry {index}."
            return f"No history entry at index {index}."
        except ValueError:
            return "Error: Index must be a number."
