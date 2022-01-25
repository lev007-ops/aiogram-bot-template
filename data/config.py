from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # We take a value of type STR

# This is a message that will be sent with a large load.
THROTTLING_MESSAGE = 'Too many messages!'

"""
This is a list of bots of bots which it will offer himself.
An example of adding a command:('command_text', 'description')
"""
BOT_COMMANDS = [

]
