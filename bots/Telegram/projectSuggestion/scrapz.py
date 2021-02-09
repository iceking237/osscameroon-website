"""
libraries; python-telegram-bot
"""

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import telegram
"""
My chat ID : 767275493
"""

# Token of the bot
TOKEN = '1522183121:AAHHaLCO6WDSStncQDUuOMwVCUCuSR0ZuzE'


# This function replies with 'Hello <user.first_name>'
def hello(update: Update, context: CallbackContext) -> None:
  update.message.reply_text(f'Hello {update.effective_user.first_name}')

#Scheduling
def callback_alarm(context:CallbackContext):
  send_message(chat_id=767275493, text='Hi, This is a daily reminder')

def reminder(update,context):
   send_message(chat_id =767275493, text='Daily reminder has been set! You\'ll get notified at 8 AM daily')
   context.job_queue.run_daily(callback_alarm, context=update.message.chat_id,days=(0, 1, 2, 3, 4, 5, 6),time = time(hour = 23, minute = 12, second = 00))

def send_message():
    return None


updater = Updater(TOKEN)

# Make the hello command run the hello function
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('reminder', reminder))


# Connect to Telegram and wait for messages
updater.start_polling()

# Keep the program running until interrupted
updater.idle()
