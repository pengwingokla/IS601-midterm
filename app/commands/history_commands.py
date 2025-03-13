from commands import Command
from history_manager import HistoryManager

class HistoryCommand(Command):
    def execute(self, *args):
        """Displays calculation history."""
        history_manager = HistoryManager()
        history = history_manager.get_history()
        if history.empty:
            return "No history available."
        return history.to_string(index=True)

class ClearHistoryCommand(Command):
    def execute(self, *args):
        """Clears calculation history."""
        history_manager = HistoryManager()
        history_manager.clear_history()
        return "Calculation history cleared."

class DeleteHistoryCommand(Command):
    def execute(self, *args):
        """Deletes a specific history entry by index."""
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
