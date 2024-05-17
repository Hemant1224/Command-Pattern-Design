# Step-by-Step Explanation
# Step 1: Define the Command Interface
# First, we define a blueprint (interface) for our commands. This blueprint ensures that all commands have an execute method to perform the action and an undo method to reverse it.
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass



# Command Interface: Think of this as a promise that every command will know how to execute an action and how to undo it.
# Step 2: Create Concrete Commands
# Next, we create specific commands that follow the blueprint. Each command knows how to perform a specific action and how to undo it.
# CreateFileCommand: This command creates a file and can also delete it if undone.
import os

class CreateFileCommand(Command):
    def __init__(self, filename):
        self.filename = filename

    def execute(self):
        with open(self.filename, 'w') as file:
            file.write("")
        print(f'File {self.filename} created.')

    def undo(self):
        os.remove(self.filename)
        print(f'File {self.filename} deleted.')



# CreateFileCommand: This command knows how to create a file and delete it if we need to undo the creation.
# AddCommand: This command adds two numbers and can undo the addition by subtracting one of the numbers.
class AddCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.result = None

    def execute(self):
        self.result = self.a + self.b
        print(f'Add: {self.a} + {self.b} = {self.result}')

    def undo(self):
        print(f'Undo Add: {self.result} - {self.b} = {self.a}')



# AddCommand: This command knows how to add two numbers and undo the addition by "removing" the second number.
# Step 3: Define the Invoker
# The invoker is like a remote control that stores commands and can execute or undo them.
class CommandInvoker:
    def __init__(self):
        self.history = []

    def execute_command(self, command):
        command.execute()
        self.history.append(command)

    def undo_command(self):
        if self.history:
            command = self.history.pop()
            command.undo()



# CommandInvoker: Think of this as a manager that keeps track of all the actions you've done and can undo them if needed.
# Step 4: Client Code
# Finally, we use the commands and the invoker to perform actions and undo them.
if __name__ == "__main__":
    invoker = CommandInvoker()

    create_file = CreateFileCommand('testfile.txt')
    invoker.execute_command(create_file)
    # Output: File testfile.txt created.

    add_command = AddCommand(10, 5)
    invoker.execute_command(add_command)
    # Output: Add: 10 + 5 = 15

    invoker.undo_command()
    # Output: Undo Add: 15 - 5 = 10

    invoker.undo_command()
    # Output: File testfile.txt deleted.
# Client Code: This is where we create our commands and use the invoker to run and undo them. We create a file, add two numbers, then undo the addition and the file creation.
