import os
import telebot
from fastapi import FastAPI, Request
import uvicorn

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

app = FastAPI()

@app.post(f"/{TOKEN}")
async def telegram_webhook(req: Request):
    body = await req.body()
    update = telebot.types.Update.de_json(body.decode("utf-8"))
    bot.process_new_updates([update])
    return "OK"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "성수왕님의 미국주식 단타봇이 준비되었습니다! 👑")

if __name__ == "__main__":
    webhook_url = f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}/{TOKEN}"
    bot.remove_webhook()
    bot.set_webhook(url=webhook_url)

    port = int(os.environ.get("PORT", 5000))
    uvicorn.run(app, host="0.0.0.0", port=port)
