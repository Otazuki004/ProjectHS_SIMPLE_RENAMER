from pyrogram import *
import os
import io
import sys

DIR = f"{os.getcwd()}/"

#init section

a_id = "10187126" # Your Api Id
a_hash = "ff197c0d23d7fe54c89b44ed092c1752" # Your Api Hash 
b_tok = "6196780979:AAEn9mTjzwGLeevJBC2h5dhpixKkuHtMEfU" # Your Bot Token

#addclients
bot = Client("Hyper Speed", bot_token=b_tok, api_id=a_id, api_hash=a_hash, plugins=dict(root="root/plugins"))
#Init End


@bot.on_message(filters.command("rename"))
def rename(_, message):
    thumb_id = f"{DIR}ok.jpg"

    try:
        filename = message.text.replace(message.text.split(" ")[0], "")
        if filename.endswith(".mp4"):
            print(None)
        elif filename.endswith(".mkv"):
            print(None)
        elif filename.endswith(".mp3"):
            print(None)
        elif filename.endswith(".jpeg"):
            print(None)
        elif filename.endswith(".png"):
            print(None)
        elif filename.endswith(".jpg"):
            print(None)
        elif filename.endswith(".py"):
            print(None)
        elif filename.endswith(".java"):
            print(None)
        elif filename.endswith(".txt"):
            print(None)
        elif filename.endswith(".text"):
            print(None)
        elif filename.endswith(".ogg"):
            print(None)
        elif filename.endswith(".m4a"):
            print(None)
        elif filename.endswith("crt"):
            print(None)
    except Exception as e:
        print(e)

    if reply := message.reply_to_message:
        x = message.reply_text("Downloading.....")
        path = reply.download(file_name=filename)
        x.edit("Uploading.....")
        message.reply_document(path, thumb=thumb_id, caption=filename)
        os.remove(path)
    else:
        bot.send_message(message.chat.id, "**USAGE** `/rename` [file name] And Reply A media")

@bot.on_message(filters.command("start"))
def start(_, message):
    bot.send_message(message.chat.id, "**USAGE** `/rename` [file name] And Reply A media")


bot.run()
