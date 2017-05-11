# deleter-bot
-------------
function 
~~~
def delete_msg(msg):
    url = "https://api.telegram.org/bot{}/deletemessage?chat_id={}&message_id={}".format(token, msg.chat.id,
                                                                                         msg.reply_to_message.message_id)
    info = requests.get(url).json()
    return info
~~~

New things will add soon please wait...
