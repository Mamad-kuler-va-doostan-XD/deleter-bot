from past.builtins import execfile
from redis import Redis

import functions
from telebot import types, TeleBot
import config
import keys
import json

data = open("TXT.json", encoding="utf8").read()
texts = json.loads(data)
print("Loaded texts")
# ===================================== #

bot = TeleBot(config.TOKEN)
db = Redis("localhost", decode_responses=True)
admins = functions.get_sudo()
db.flushall()
# ===================================== #

print(
    '''
Hi,
Welcome to our project...
--- Bot :D
Your bot is running,
Admins:
{}
-------------------------

'''.format(admins)
)

for plugin in config.plugins:
    try:
        execfile("plugins/{}.py".format(plugin))
        print("Loaded plugin {}".format(plugin))
    except Exception as error:
        print("There was an error loading plugin {}\nCheck log file for more information.".format(plugin))
        functions.save_to_log(error)
# ======================================= #
print("Plugins loaded successfully.")
# ======================================= #
bot.polling()
