from commands import Command

class AddCommand(Command):
    def execute(self, *args):
        return sum(args)

class SubtractCommand(Command):
    def execute(self, *args):
        numbers = list(map(float, args))
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        return result

class MultiplyCommand(Command):
    def execute(self, *args):
        numbers = list(map(float, args))
        result = 1
        for num in numbers:
            result *= num
        return result

class DivideCommand(Command):
    def execute(self, *args):
        numbers = list(map(float, args))
        if 0 in numbers[1:]:  # Prevent division by zero
            raise ZeroDivisionError("Cannot divide by zero.")
        result = numbers[0]
        for num in numbers[1:]:
            result /= num
        return result
