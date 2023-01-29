from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime 
from spy import *

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    user_id = update.effective_user.id
    if user_id == 582499322:
        print(1)
        await update.message.reply_text(f'Привет, моя стервозинка =)')
    elif user_id == '582499322':
        print(2)
        await update.message.reply_text(f'Привет, моя стервозинка =)')
    else:
        await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hello\n/time\n/help')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')