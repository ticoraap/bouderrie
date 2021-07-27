from commandregistry import CommandRegistry

commandRegistry = CommandRegistry()

for key, value in commandRegistry.commands.items():
    print(key)
    print(value)
