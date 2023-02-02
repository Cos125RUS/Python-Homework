# Модули telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

# Модуль логирования
from spy import *

# Модуль запроса данных о погоде
from weather import *

# Модуль обработки данных
from answer import *


#-------------------------------------------------------------------------------------
# Хранение меню
keyboard = [[InlineKeyboardButton("Томск", callback_data="Tomsk"),
        InlineKeyboardButton("Владивосток", callback_data="Vladivostok"), 
        InlineKeyboardButton("Новокузнецк", callback_data="Novokuznetsk")],  
        [InlineKeyboardButton("Гродно", callback_data="Grodno"), 
        InlineKeyboardButton("Вунгтау", callback_data="Vung Tau"),
        InlineKeyboardButton("Шымкент", callback_data="Shymkent")],
        [InlineKeyboardButton("Мурманск", callback_data="Красногорск"), 
        InlineKeyboardButton("Уфа", callback_data="Ставрополь"),
        InlineKeyboardButton("Барнаул", callback_data="Barnaul")], 
        [InlineKeyboardButton("Москва", callback_data="Moscow"), 
        InlineKeyboardButton("Санкт-Петербург", callback_data="St. Petersburg"),
        InlineKeyboardButton("Казань", callback_data="Kazan")]]
keyboard_menu = InlineKeyboardMarkup(keyboard)
#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------
# Привтствие юзера
async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.message.chat.id # id пользователя
    update.effective_user.first_name # first_name пользователя на входе
    update.message.chat.first_name # first_name пользователя на выходе
    # <class 'telegram._update.Update'>
    log(update, context)
    # user_id = update.effective_user.id 
    await update.message.reply_text(f'Привет {update.effective_user.first_name}')

#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------
# Подсказка для пользователей
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Напиши /weather <<Твой город>> (на английском)\nНапример:\n/weather Moscow')

#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------
# Отрисовка кнопок
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text("Выберите город из списка\nИли напишите: /weather 'город' (на английском)", reply_markup=keyboard_menu)

#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------
# Считывание нажатий
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    weather_data = get_answer(query.data)
    answer = create_answer(weather_data)
    # await query.answer()
    await query.edit_message_text(text=answer, reply_markup=keyboard_menu) # Ответ пользователю

#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------
# Ответ на команду /weather
async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    city = update.message.text.replace('/weather ','')
    weather_data = get_answer(city)
    answer = create_answer(weather_data)
    await update.message.reply_text(answer)

#-------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------