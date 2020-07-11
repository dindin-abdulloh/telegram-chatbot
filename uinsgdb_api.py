from telegram.ext import Updater, CommandHandler, MessageHandler, Filters




def start(update, context):
    update.message.reply_text('Hi! Apa kamu sudah makan???')

def message(update, context):
    update.message.reply_text(update.message.text.upper())

def command_handler(update, context):
    update.message.reply_text(f"Command: {update.message.text}")

def receive_image(update, context):
    try:
        print(update)
        obj = context.bot.getFile(file_id=update.message.document.file_id)
        obj.download()
        update.message.reply_text("File has been download.")
    except Exception as e:
        print(str(e))

def receive_audio(update, context):
    try:
        audio_obj = context.bot.getFile(file_id=update.message.audio.file_id)
        audio_obj.download()
        update.message.reply_text("Your audio has been processed")
    except expression as e:
        pass

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