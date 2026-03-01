from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

# --- Настройка токена ---
TOKEN = os.getenv("TELEGRAM_TOKEN", "7815618712:AAETEhnXEKSI88nrc1iYYyOcYKvqWe_TP6g")

# --- Сообщение, которое бот будет отправлять ---
REPLY_TEXT = (
    "Здравствуйте, чтобы приобрести христианские ресурсы пишите сюда\n\n"
    "👉 @Godskidss"
)

# --- Функция-обработчик всех сообщений ---
async def reply_any(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(REPLY_TEXT)

# --- Основная функция запуска бота ---
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Обработчик любых текстовых сообщений
    app.add_handler(MessageHandler(filters.TEXT, reply_any))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
