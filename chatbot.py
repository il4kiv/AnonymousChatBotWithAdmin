import telebot
from telebot import types

bot = telebot.TeleBot(' gfgf')

admin_user_id = 123  # change to your telegram ID (getyouridbot)


class User:
    def __init__(self, user_id):
        self.user_id = user_id


user_dict = {}


@bot.message_handler(commands=['start'])
def welcome(message):
    if message.from_user.id != admin_user_id:
        user = User(message.from_user.id)
        user_dict[message.from_user.id] = user
    bot.send_message(message.from_user.id,
                     "Welcome to the anonymous chat! Send a message, image, video, voice, sticker, GIF, or file to get started.")


@bot.message_handler(func=lambda message: True,
                     content_types=['text', 'photo', 'document', 'video', 'voice', 'sticker', 'animation'])
def chat(message):
    global admin_user_id

    if len(user_dict) >= 2:
        if message.from_user.id in user_dict.keys():
            companion = [key for key in user_dict.keys() if key != message.from_user.id][0]
            if message.content_type == 'text':
                bot.send_message(companion, message.text)
                bot.forward_message(admin_user_id, message.chat.id, message.message_id)
            elif message.content_type == 'photo':
                photo = message.photo[-1].file_id
                bot.send_photo(companion, photo)
                bot.forward_message(admin_user_id, message.chat.id, message.message_id)
            elif message.content_type == 'document':
                doc = message.document.file_id
                bot.send_document(companion, doc)
                bot.forward_message(admin_user_id, message.chat.id, message.message_id)
            elif message.content_type == 'video':
                video = message.video.file_id
                bot.send_video(companion, video)
                bot.forward_message(admin_user_id, message.chat.id, message.message_id)
            elif message.content_type == 'voice':
                voice = message.voice.file_id
                bot.send_voice(companion, voice)
                bot.forward_message(admin_user_id, message.chat.id, message.message_id)
            elif message.content_type == 'sticker':
                sticker = message.sticker.file_id
                bot.send_sticker(companion, sticker)
                bot.forward_message(admin_user_id, message.chat.id, message.message_id)
            elif message.content_type == 'animation':
                animation = message.animation.file_id
                bot.send_animation(companion, animation)
                bot.forward_message(admin_user_id, message.chat.id, message.message_id)
            else:
                bot.send_message(message.from_user.id, "Unsupported content type.")
        else:
            bot.send_message(message.from_user.id,
                             "You are not currently in a chat.")
    else:
        bot.send_message(message.from_user.id, "Waiting for another user to join the chat.")


print("BOT IS WORKING")
bot.polling()
