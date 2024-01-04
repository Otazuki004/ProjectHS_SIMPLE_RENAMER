from pyrogram import *
import os
import io
import sys

DIR = f"{os.getcwd()}/"

#init section

video_formats = ['mp4', 'avi', 'mkv', 'mov', 'wmv', 'flv', 'webm', '3gp']
audio_formats = ['mp3', 'wav', 'ogg', 'aac', 'flac', 'wma', 'm4a']
text_formats = ['txt', 'csv', 'json', 'xml', 'html', 'md', 'pdf', 'text']
coding_languages = ['py', 'java', 'js', 'c', 'css', 'ruby', 'php', 'swift']
Image_Formats = ['jpeg', 'png', 'gif', 'tiff', 'bmp', 'webp']

formats = [video_formats, audio_formats, text_formats, coding_languages, Image_Formats]

a_id = "10187126" # Your Api Id
a_hash = "ff197c0d23d7fe54c89b44ed092c1752" # Your Api Hash 
b_tok = "6196780979:AAEn9mTjzwGLeevJBC2h5dhpixKkuHtMEfU" # Your Bot Token

#addclients
bot = Client("Hyper Speed", bot_token=b_tok, api_id=a_id, api_hash=a_hash, plugins=dict(root="root/plugins"))

#Init End




@bot.on_message(filters.command("rename"))
def rename(_, message):
    thumb_id = f"{DIR}ok.jpg"
    if reply := message.reply_to_message:
        try:
            filename = message.text.replace(message.text.split(" ")[0], "")
            if not any(filename.endswith(format) for format_list in formats for format in format_list):
                message.reply_text("**Enter text ⚡ or a valid format (e.g., .mp4).**")
            else:
                if reply := message.reply_to_message:
                    x = message.reply_text("Downloading.....")
                    path = reply.download(file_name=filename)
                    x.edit("Uploading.....")
                    message.reply_document(path, thumb=thumb_id, caption=filename)
                    os.remove(path)
                    x.delete()
                else:
                    bot.send_message(message.chat.id, "**USAGE** `/rename` [file name] And Reply A media")
        except Exception as e:
            print(e)
            message.reply_text(f"**Error: ** {e}")
    else:
        bot.send_message(message.chat.id, "**Reply To A File 🗃️**")
        
@bot.on_message(filters.command("start"))
def start(_, message):
    bot.send_message(message.chat.id, "**USAGE** `/rename` [file name] And Reply A media")

@bot.on_message(filters.command("repo"))
def repo(_, message):
    bot.send_message(message.chat.id, "** Thanks For Finding Out Repo Please Star Us And Give Credits, This Repo Made By @Hyper_Speed0 and its Created for Our Cliant So I can't Give That Renamer Repo, If You Need Codes Only Take It From https://github.com/Otazuki004/QuantumRoBot.git ✅ its available in main.py**")
bot.run()
