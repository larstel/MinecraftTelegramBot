#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from mcrcon import MCRcon

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text("Available commands:/online, /send message, /startWatchdog, /stopWatchdog")

def online(update, context):
    """Send a message when the command /online is issued."""
    with MCRcon("192.168.178.47", "123ichbincool") as mcr:
        resp = mcr.command("/list")
        update.message.reply_text(resp)
        print(resp)

def sound(update, context):
    """Send a message when the command /sound is issued."""
    with MCRcon("192.168.178.47", "123ichbincool") as mcr:
        resp = mcr.command("/playsound minecraft:entity.villager.ambient voice @a")

def send(update, context):
    """Send a message when the command /send is issued."""
    with MCRcon("192.168.178.47", "123ichbincool") as mcr:
        name = update.message.from_user.first_name
        mess = update.message.text
        resp = mcr.command('/say ' + name + ":" + mess[5:])
        update.message.reply_text(resp)
        print(resp)

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def alarm(context):
    fileHandle = open ('logs/latest.log',"r")
    lineList = fileHandle.readlines()
    fileHandle.close()
    output_text = lineList[-1]
    file_size = os.path.getsize('logs/latest.log')
    global old_file_size
    if old_file_size != file_size:
        old_file_size = file_size
        if "[Server thread/INFO]" in output_text:
            context.bot.send_message(context.job.context, text=output_text[33:])
    global watchdog_enabled
    if watchdog_enabled == True:
        job = context.job_queue.run_once(alarm, 1, context=context.job.context)

def start_watchdog(update, context):
    """Add a job to the queue."""
    global watchdog_enabled
    watchdog_enabled = True
    chat_id = update.message.chat_id

    # Add job to queue
    job = context.job_queue.run_once(alarm, 2, context=chat_id)
    context.chat_data['job'] = job

def stop_watchdog(update, context):
    global watchdog_enabled
    watchdog_enabled = False

old_file_size = 0
watchdog_enabled = True
def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("TELEGRAM_TOKEN", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("online", online))
    dp.add_handler(CommandHandler("send", send))
    dp.add_handler(CommandHandler("sound", sound))
    dp.add_handler(CommandHandler("startWatchdog", start_watchdog))
    dp.add_handler(CommandHandler("stopWatchdog", stop_watchdog))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
