from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem
from datetime import datetime

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    logging.info('Бот запустился')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    #add pricessing some action like command stsrt with 2  parameters
    # command_name and name_function that write some action from this commandd
    dp.add_handler(CommandHandler('planet', finder_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling() #bot will connect with telegram by his Api key
    mybot.idle() #will work before we stop it

def greet_user(mybot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)

def finder_planet(mybot, update):
    text = update.message.text
    text_list = text.split()
#    user_text = datetime.strptime(text_list[1], '%Y/%m/%d')
#    planet = ephem.Mars(user_text)
#    info = ephem.constellation(planet)
#    print(ephem.constellation(planet))
#    print(info)
#    print(update.message)
#    update.message.reply_text(info)
    try:
        if len(text_list) == 3:
            planet_name = text_list[1].strip()
            planet_date = text_list[2].strip()
            datetime.strptime(planet_date, '%Y/%m/%d')
            planet = getattr(ephem, planet_name)(planet_date)
        elif len(text_list) == 2:
            planet_name = text_list[1].strip()
            planet = getattr(ephem, planet_name)(datetime.strftime(datetime.now(), '%Y/%m/%d'))
        else:
            update.message.reply_text('Not correct input data')
    except AttributeError as ex:
        update.message.reply_text('Incorrect planet name!')
        logging.error('user: {username}, chat id: {chat_id}, message: {message}'.format(
            username=text_list.chat.username,
            chat_id=text_list.chat.id,
            message=text_list
        ), ex)
    except ValueError as ex:
        update.message.reply_text('Incorrect date!')
        logging.error('user: {username}, chat id: {chat_id}, message: {message}'.format(
            username=text_list.chat.username,
            chat_id=text_list.chat.id,
            message=text_list
        ), ex)
    else:
        update.message.reply_text(ephem.constellation(planet))


def talk_to_me(mybot, update):
#    user_text = update.message.text
    user_text = 'Привет {}! Ты писал: {}'.format(update.message.chat.first_name, update.message.text)
    logging.info('User: %s, Chat id: $s, Message: % ', update.message.chat.username,
                 update.message.chat.id, update.message.text)
#    print(update.message)
    update.message.reply_text(user_text)

if __name__ == '__main__':
    main()