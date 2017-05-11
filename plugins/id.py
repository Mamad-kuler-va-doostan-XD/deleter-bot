@bot.message_handler(commands=['id'])
def send_id(msg):
    cp = msg.chat.type
    if cp == 'private':
        text = '<b>ID:</b> {}'.format(str(msg.chat.id))
    else:
        text = '<b>Your ID: </b> {}\n<b>Group\'s ID: </b> {}'.format(str(msg.from_user.id), str(msg.chat.id))
    bot.send_message(msg.chat.id, text, parse_mode='HTML')
