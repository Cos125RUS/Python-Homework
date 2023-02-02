import time
import datetime as dt
import logging
import random
from aiogram import Bot, Dispatcher, executor, types
from os import path

# 'UTF-8-sig'
logging.basicConfig(level=logging.INFO, filename="bot_log.csv", filemode="w",
                    format="%(asctime)s: %(levelname)s %(funcName)s-%(lineno)d %(message)s")


MSG = "{}, choose an action:"

bot = Bot("6012678486:AAEkMXJOmBjStU1kbadh6yuTBhDIdkoh7oo")
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    user_bot = message.from_user.is_bot
    user_message = message.text
    logging.info(f'{user_id=} {user_bot=} {user_message=}')
    await message.reply(f"Hi, {user_full_name}!")
    time.sleep(1)
    btns = types.ReplyKeyboardMarkup(row_width=1)
    btn_photo = types.KeyboardButton('/Photo')
    btns.add(btn_photo)
    await bot.send_message(user_id, MSG.format(user_name), reply_markup=btns)



@dp.message_handler(commands=['Photo'])
async def start_handler(message: types.Message):
    count_img = counter()
    num = random.randint(0, count_img)
    name = f'photo\{num}.jpg'
    print(f'{dt.datetime.now()}\t{message.from_user.full_name}\t{name}')
    with open(name, 'rb') as img:
        await bot.send_photo(message.from_user.id, img)
    await bot.send_message(message.from_user.id, "I give you my photo")


def counter():
    count = 0
    while path.isfile(f'photo\{count}.jpg'):
        count += 1
    return count



# @dp.message_handler(content_types=['photo'])
# def photo_id(message):
#     photo = max(message.photo, key=lambda x: x.height)
#     print(photo.file_id)


@dp.message_handler(content_types=['photo'])
def photo(message):
     fileID = message.photo[-1].file_id
     file_info = bot.get_file(fileID)
     # downloaded_file = bot.download_file(file_info.file_path)
     # with open("image.jpg", 'wb') as new_file:
     #     new_file.write(downloaded_file)


# @dp.message_handler(content_types=['photo'])
# async def download_file_by_id(message):
#     file = bot.get_file(message.file_id)
#     file_path = file.
#     downloaded_file = bot.download_file(file.file_path)



if __name__ == '__main__':
    print("Server start")
    executor.start_polling(dp)
