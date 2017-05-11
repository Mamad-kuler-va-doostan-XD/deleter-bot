# deleter-bot
-------------
# function 
~~~
def delete_msg(msg):
    url = "https://api.telegram.org/bot{}/deletemessage?chat_id={}&message_id={}".format(token, msg.chat.id,
                                                                                         msg.reply_to_message.message_id)
    info = requests.get(url).json()
    return info
~~~
# Installation
~~~
$ virtualenv -p python2.7 --no-site-packages --distribute .env
$ source .env/bin/activate
$ pip install -r requirements.txt
~~~
New things will add soon please wait...
