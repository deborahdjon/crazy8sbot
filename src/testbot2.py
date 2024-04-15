from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from constants import BOT_INFOS


def echo(update, context):
    message = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text=message.replace('bot2 ',''))

echo_handler = MessageHandler(Filters.regex('bot2'), echo)

def kill():
    updater.stop()
    updater.is_idle = False
    exit()

def main():
    global updater
    updater = Updater(token=BOT_INFOS["testbot2"]["token"], use_context=True)
    # sends updates all added handlers, the handlers send out commands or do sth. based on the input
    dispatcher = updater.dispatcher
    dispatcher.add_handler(echo_handler)
    updater.start_polling()

if __name__ == "__main__":
    main()

