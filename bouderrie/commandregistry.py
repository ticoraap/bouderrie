import pickle
import os


class CommandRegistry:
    def __init__(self):
        self.load()

    def load(self):
        if os.path.isfile("commands.pkl"):
            with open("commands.pkl", "rb") as f:
                self.commands = pickle.load(f)
        else:
            self.commands = {}

    def save(self):
        with open("commands.pkl", "wb") as f:
            pickle.dump(self.commands, f)

    def add(self, command, soundfile):
        if command in self.commands:
            return False
        else:
            self.commands[command] = soundfile
            self.save()
            return True

    def remove(self, command):
        if command in self.commands:
            del self.commands[command]
            self.save()

    def get(self, command):
        if command in self.commands:
            return self.commands[command]
        else:
            return None
