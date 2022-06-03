#!/usr/bin/env python
# -*- coding: utf-8 -*-


#import's'

import pyrogram
from pyrogram import Client, filters
from datetime import datetime

#puplic var's
now = datetime.now()



#api's var's
api_id = 11619572
api_hash = "f9dd1efc1781f1476c53afa04d76b234"
bot_token = "5353696413:AAG5PDs7YKW0FhW8HP6c0pUU6MJf4meyyoo"


#api's of bot'
app = Client(
    "my_bot",
    api_id=api_id, 
    api_hash=api_hash,
    bot_token=bot_token
)
print("\n {} : bot api's is working..." .format(now))

#methods
##start command (private) | /start
@app.on_message(filters.command('start')  )
def reply_start(app, message):
    app.send_message(message.chat.id, "hello, world")
    print("[{}] : /start::: hi \n" .format(datetime.now()))


##simple help command | /help
@app.on_message(filters.command('help'))
def reply_command_help(app, message):
    message.reply_text( text="I'm here to help you.")
    print("[LOG: {}] : /help::: im here. \n" .format(now))

#get user ID&USERNAME ::: /id command
@app.on_message(filters.command('id'))
def gget_id(app, msg):
    #private var's for ggeet_id {its for ID and USERNAME}...
    uid = msg.from_user.id
    usn = msg.from_user.username
    #send in [USER_CHAT&LOG]:- from user ID&USERNAME 
    #app.send_message(msg.chat.id, text="Your ID: {} \n your USERNAME : {} ." .format(uid, usn))
    msg.reply("Your ID: {} \n your USERNAME : {} ." .format(uid, usn))
    print("[LOG {}] : /id::: ur ID: {} // ur USERNAME : {} \n" .format(now, uid, usn))

#testing the midia with command /m
@app.on_message(filters.command('m'))
def send_m_command(app, msg):
    app.send_photo(msg.chat.id, photo="https://docs.pyrogram.org/_static/pyrogram.png")
    app.send_document(msg.chat.id, document="hi.txt")

#bot runnig
print("{} : the bot is running" .format(now))
app.run()
