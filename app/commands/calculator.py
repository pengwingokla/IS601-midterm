"""
calculator_commands.py

This module defines arithmetic command classes following the Command pattern. 
Each class implements the `execute` method to perform basic mathematical operations.

Classes:
    - AddCommand: Performs addition of given numbers.
    - SubtractCommand: Performs subtraction of given numbers.
    - MultiplyCommand: Performs multiplication of given numbers.
    - DivideCommand: Performs division of given numbers with zero-division handling.

Usage:
    These command classes are designed to be used with a `CommandHandler` 
    that dynamically registers and executes commands.

Example:
    add = AddCommand()
    result = add.execute(2, 3, 4)  # Returns 9
"""

from commands import Command

class AddCommand(Command):
    """Command to perform addition of multiple numbers."""
    def execute(self, *args):
        """Executes the addition command.
        Args:
            *args (float): Numbers to be summed.
        Returns:
            float: The sum of all input numbers.
        """
        return sum(args)

class SubtractCommand(Command):
    """Command to perform subtraction of multiple numbers."""
    def execute(self, *args):
        """Executes the subtraction command.
        Args:
            *args (float): Numbers to subtract, starting from the first number.
        Returns:
            float: The result after sequential subtraction.
        """
        numbers = list(map(float, args))
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        return result

class MultiplyCommand(Command):
    """Command to perform multiplication of multiple numbers.""" 
    def execute(self, *args):
        """Executes the multiplication command.
        Args:
            *args (float): Numbers to multiply.
        Returns:
            float: The product of all input numbers.
        """
        numbers = list(map(float, args))
        result = 1
        for num in numbers:
            result *= num
        return result

class DivideCommand(Command):
    """Command to perform division of multiple numbers, ensuring no division by zero."""
    def execute(self, *args):
        """Executes the division command.
        Args:
            *args (float): Numbers to divide, starting from the first number.
        Returns:
            float: The result of sequential division.
        Raises:
            ZeroDivisionError: If division by zero is attempted.
        """
        numbers = list(map(float, args))
        if 0 in numbers[1:]:  # Prevent division by zero
            raise ZeroDivisionError("Cannot divide by zero.")
        result = numbers[0]
        for num in numbers[1:]:
            result /= num
        return result
