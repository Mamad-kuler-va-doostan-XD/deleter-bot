from config import *


def is_sudo(msg):
    return msg.from_user.id in SUDO_LIST


def get_sudo():
    text = ''
    for i in SUDO_LIST:
        text += str(i) + '\n'
    return text


def save_to_log(error):
    log = open("errors.log", "w")
    error = str(error) + "\n--------------\n"
    log.write(error)
