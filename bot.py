from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

# --- Настройка токена ---
# Рекомендуется хранить токен в переменной окружения
# На Bothost можно добавить переменную окружения TELEGRAM_TOKEN
TOKEN = os.getenv("TELEGRAM_TOKEN", "7815618712:AAETEhnXEKSI88nrc1iYYyOcYKvqWe_TP6g")

# --- Сообщение, которое бот будет отправлять ---
REPLY_TEXT = "Здравствуйте, чтобы приобрести христианские ресурсы пишите сюда 
👉 @Godskidss"

# --- Функция-обработчик всех сообщений ---
async def reply_any(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(REPLY_TEXT)

# --- Основная функция запуска бота ---
def main():
    # Создаём приложение бота
    app = ApplicationBuilder().token(TOKEN).build()

    # Обработчик любых текстовых сообщений (включает команды)
    app.add_handler(MessageHandler(filters.TEXT, reply_any))

    print("Бот запущен...")
    app.run_polling()

# --- Точка входа ---
if __name__ == "__main__":
    main()
