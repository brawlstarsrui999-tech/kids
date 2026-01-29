from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

# Сообщение, которое бот будет отправлять
REPLY_TEXT = "Здравствуйте, чтобы и приобрести христианские ресурсы пишите сюда 👉 @Godskidss"

# Функция-обработчик любого сообщения
async def reply_any(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(REPLY_TEXT)

# Главная функция запуска бота
def main():
    # Вставь сюда токен своего бота
    TOKEN = "7815618712:AAETEhnXEKSI88nrc1iYYyOcYKvqWe_TP6g"

    # Создаем приложение
    app = ApplicationBuilder().token(TOKEN).build()

    # Обработчик любой команды
    app.add_handler(CommandHandler(filters.ALL, reply_any))

    # Обработчик любых текстовых сообщений
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_any))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
