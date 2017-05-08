@bot.message_handler(func=lambda msg: msg.text == '/start' and msg.chat.type == 'private')
def start(msg):
    db.sadd("{}:users".format(bot.get_me().username), msg.from_user.id)
    lang = db.hget("{}:user:{}".format(bot.get_me().username, str(msg.from_user.id)), "lang")
    if lang:
        bot.send_message(msg.chat.id, text=texts[lang]["START"].format(bot.get_me().username))
    else:
        bot.send_message(msg.chat.id, "Please choose your language", reply_markup=keys.lang_key)


@bot.callback_query_handler(func=lambda call: call.data.startswith("setlang"))
def set_lang(call):
    lang = call.data.replace("setlang|", "")
    bot.edit_message_text(text=texts[lang]["START"].format(bot.get_me().username), chat_id=call.message.chat.id,
                          message_id=call.message.message_id)
    db.hset("{}:user:{}".format(bot.get_me().username, str(call.from_user.id)), "lang", lang)
