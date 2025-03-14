"""
square.py

This module defines the `SquareCommand` class, which calculates the square of a given number.
"""
from ..commands import Command


class SquareCommand(Command):
    """A command that returns the square of a given number."""
    def execute(self, *args):
        """Returns the square of a number."""
        if len(args) != 1:
            return "Usage: square <number>"
        try:
            num = float(args[0])
            return num ** 2
        except ValueError:
            return "Error: Argument must be a number."
