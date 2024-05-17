# Command Interface
class Command:
    def execute(self):
        pass

# Concrete Commands
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

# Receiver
class Light:
    def turn_on(self):
        print("Light turned on.")

    def turn_off(self):
        print("Light turned off.")

# Invoker
class Switch:
    def __init__(self):
        self.on_command = None
        self.off_command = None

    def set_commands(self, on_command, off_command):
        self.on_command = on_command
        self.off_command = off_command

    def switch_on(self):
        if self.on_command:
            self.on_command.execute()
        else:
            print("No on command set.")

    def switch_off(self):
        if self.off_command:
            self.off_command.execute()
        else:
            print("No off command set.")

# Client
if __name__ == "__main__":
    light = Light()
    light_on_command = LightOnCommand(light)
    light_off_command = LightOffCommand(light)

    switch = Switch()

    switch.set_commands(light_on_command, light_off_command)
    switch.switch_on()  # Output: Light turned on.
    switch.switch_off()  # Output: Light turned off.

    switch.set_commands(None, None)
    switch.switch_on()  # Output: No on command set.
    switch.switch_off()  # Output: No off command set.
