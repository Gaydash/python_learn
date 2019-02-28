from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    logging.info('Бот запустился')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling() #bot will connect with telegram
    mybot.idle() #will work before we stop it

def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text
#    user_text='Привет {}! Ты писал: {}'.format(update.message.chat.first_name, update.message.text)
    logging.info('User: %s, Chat id: $s, Message: % ', update.message.chat.username,
                 update.message.chat.id, update.message.text)
    print(update.message)
    update.message.reply_text(user_text)

main()