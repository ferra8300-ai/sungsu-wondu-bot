import os
import telebot

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "성수왕님의 미국주식 단타봇이 준비되었습니다! 👑")

bot.polling()
