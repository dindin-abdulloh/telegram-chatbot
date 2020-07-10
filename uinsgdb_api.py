from telegram.ext import Updater, CommandHandler, MessageHandler, Filters




def start(update, context):
    update.message.reply_text('Hi! Apa kamu sudah makan???')

def message(update, context):
    update.message.reply_text(update.message.text.upper())

def command_handler(update, context):
    update.message.reply_text(f"Command: {update.message.text}")

def main():
    """Start the bot."""
    updater = Updater("889859284:AAFeKjOv3zDsclgPw09Q4X2lJOB6NvlVuso", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(MessageHandler(Filters.text, message))
    dp.add_handler(MessageHandler(Filters.command, command_handler))
    updater.start_polling()
    updater.idle()




if __name__=="__main__":
    main()