import telebot
from flask import Flask
from threading import Thread
import os

BOT_TOKEN = "5937330270:AAGiVsbLmjXisi3uirKfI5mhUtBt61iPzbo"
ADMIN_ID = 5103348494  # YOUR TELEGRAM ID

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

# ---------- BOT LOGIC (FORWARD ONLY) ----------
@bot.message_handler(
    func=lambda message: True,
    content_types=['text','photo','video','document','sticker','voice','audio']
)
def forward_all(message):
    if message.from_user.id != ADMIN_ID:
        bot.forward_message(
            chat_id=ADMIN_ID,
            from_chat_id=message.chat.id,
            message_id=message.message_id
        )

# ---------- FLASK SERVER ----------
@app.route('/')
def home():
    return "Bot is running ✅"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

def run_bot():
    bot.infinity_polling(skip_pending=True)

# ---------- MAIN ----------
if __name__ == "__main__":
    Thread(target=run_flask).start()
    Thread(target=run_bot).start()
