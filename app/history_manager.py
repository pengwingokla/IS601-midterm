"""
history_manager.py
"""

import os
import pandas as pd

class HistoryManager:
    """Manages the history of calculations using Pandas."""
    HISTORY_FILE = "data/history.csv"

    def __init__(self):
        self.history = self.load_history()

    def load_history(self):
        """Load history from CSV file or create an empty dataframe."""
        if os.path.exists(self.HISTORY_FILE):
            return pd.read_csv(self.HISTORY_FILE)
        return pd.DataFrame(columns=["Operation", "Operands", "Result"])

    def save_operation(self, operation, operands, result):
        """Save a calculation to history."""
        new_entry = pd.DataFrame([{
            "Operation": operation,
            "Operands": " ".join(map(str, operands)),
            "Result": result
        }])
        self.history = pd.concat([self.history, new_entry], ignore_index=True)
        self.history.to_csv(self.HISTORY_FILE, index=False)

    def get_history(self):
        """Return the history as a DataFrame."""
        return self.history

    def clear_history(self):
        """Clear calculation history."""
        self.history = pd.DataFrame(columns=["Operation", "Operands", "Result"])
        self.history.to_csv(self.HISTORY_FILE, index=False)

    def delete_history_entry(self, index):
        """Delete a specific history entry by index."""
        if index < 0 or index >= len(self.history):
            return False  # Entry does not exist
        self.history = self.history.drop(index).reset_index(drop=True)
        self.history.to_csv(self.HISTORY_FILE, index=False)
        return True
