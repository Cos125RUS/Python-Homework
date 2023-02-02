# Модули telegram
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

# Командный модуль
from bot_commands import *

# Ключи
from config import token


#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------
# Бот
def main() -> None:
    # Создание
    app = ApplicationBuilder().token(token).build()


    # Список команд
    app.add_handler(CommandHandler("hello", hello_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("weather", weather_command))
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CallbackQueryHandler(button))


    # Стартер
    print("Start server")
    app.run_polling()
#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------



if __name__ == "__main__":
    main()