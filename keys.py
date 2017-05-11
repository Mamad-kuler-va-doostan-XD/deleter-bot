from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

lang_key = InlineKeyboardMarkup()
langs = {
    "En": {
        "text": "English",
        "callback": "setlang|en"
    },
    "Fa": {
        "text": "Farsi",
        "callback": "setlang|fa"
    }
}
for i in langs:
    lang_key.row(InlineKeyboardButton(text=langs[i]["text"], callback_data=langs[i]["callback"]))
