import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TELEGRAM_TOKEN = '8172705039:AAHu4dKQhFDjGN9jisrQwXKEzp9BI8SQfk8'
OPENROUTER_API_KEY = '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'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Menga savolingizni yuboring 😊Meni Ziyayev Nurmuhammad yaratdi")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://t.me/ChatGPT_bot",  # o'rniga bot usernameni yoz
        "X-Title": "My Telegram Bot"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
       "messages": [
    {"role": "system", "content": "Sen ChatGPT assistentsan. Foydalanuvchiga har doim o‘zbek tilida, tushunarli va foydali tarzda javob ber."},
    {"role": "user", "content": user_message}
]

    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
    else:
        reply = "Kechirasiz, hozircha javob bera olmadim."

    await update.message.reply_text(reply)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("✅ Bot ishlayapti...")
    app.run_polling()
