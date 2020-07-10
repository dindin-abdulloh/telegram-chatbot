from telegram.ext import Updater, CommandHandler


def command_handling_fn(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="Hallo selamat pagi")

if __name__=="__main__":
    updater = Updater(token="889859284:AAFeKjOv3zDsclgPw09Q4X2lJOB6NvlVuso", use_context=True)
    dispatcher = updater.dispatcher

    handler = CommandHandler("start",command_handling_fn)

    dispatcher.add_handler(handler)

    updater.start_polling()