# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler
from telegram.update import Update
from telegram import User
import telegram
import time
import datetime
from dateutil.relativedelta import relativedelta
import requests
from bs4 import BeautifulSoup
import logging
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO, filename='.temporary_log_2')

updater = Updater(token='')

dispatcher = updater.dispatcher

blocked_ids = {}

def orbit(bot, update):
    if update.message.from_user.id == 726041690:
        with open(".temporary_log_2") as f:
            for line in f:
                bot.send_message(chat_id=update.message.chat_id, text=line)
    else:
        msg = " First Name: {}, Last Name: {}, username: {}, Function: start, chat_id: {}, user_id: {}".format(update.message.from_user.first_name, update.message.from_user.last_name, update.message.from_user.username, update.message.chat_id, update.message.from_user.id)
        logging.info(msg)

def filter(name = None):
    if name in blocked_ids.values():
        return False
    return True

def start(bot, update):
    if filter(update.message.from_user.id):
        bot.send_message(chat_id=update.message.chat_id, text="1) /mnac \n2) /gnac \n3) /anekdot\n")
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Dear {} You are blocked !".format(update.message.from_user.first_name))

    msg = " First Name: {}, Last Name: {}, username: {}, Function: start, chat_id: {}, user_id: {}".format(update.message.from_user.first_name, update.message.from_user.last_name, update.message.from_user.username, update.message.chat_id, update.message.from_user.id)
    logging.info(msg)
    #bot.send_photo(chat_id=update.message.chat_id, photo=open('yes.jpg', 'rb'))

def give_anekdot():
    session = requests.Session()
    session.max_redirects = 9999999
    page = session.get("https://nekdo.ru/random", verify = False)
    soup = BeautifulSoup(page.content, 'html.parser')
    res =  soup.find('div', class_="text")
    return res.text

def anekdot(bot, update):
    if filter(update.message.from_user.id):
        bot.send_message(chat_id=update.message.chat_id, text=give_anekdot())
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Dear {} You are blocked !".format(update.message.from_user.first_name))

    msg = " First Name: {}, Last Name: {}, username: {}, Function: start, chat_id: {}, user_id: {}".format(update.message.from_user.first_name, update.message.from_user.last_name, update.message.from_user.username, update.message.chat_id, update.message.from_user.id)
    logging.info(msg)


def  mnac(bot, update):
    if filter(update.message.from_user.id):
        a = '2018-07-26 08:00:00'
        b = '2020-07-26 08:00:00'
        now = datetime.datetime.now()
        start = datetime.datetime.strptime(a, '%Y-%m-%d %H:%M:%S')
        ends = datetime.datetime.strptime(b, '%Y-%m-%d %H:%M:%S')
        diff1 = relativedelta(ends, now)
        diff1_1 = (datetime.date(ends.year, ends.month, ends.day) - datetime.date(now.year, now.month, now.day))
        diff2 = relativedelta(now, start)
        diff2_1 = datetime.date(now.year, now.month, now.day) - datetime.date(start.year, start.month, start.day)
        bot.send_message(chat_id=update.message.chat_id, text="Մնացել է")
        bot.send_message(chat_id=update.message.chat_id, text="{} Տարի {} Ամիս {} Օր {} Ժամ {} Րոպե ".format(diff1.years, diff1.months, diff1.days, diff1.hours, diff1.minutes))
        bot.send_message(chat_id=update.message.chat_id, text="{} Օր ".format(diff1_1.days))
        bot.send_message(chat_id=update.message.chat_id, text="{:.3f} % ".format(100*diff1_1.days/731.0))
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Dear {} You are blocked !".format(update.message.from_user.first_name))
    msg = " First Name: {}, Last Name: {}, username: {}, Function: start, chat_id: {}, user_id: {}".format(update.message.from_user.first_name, update.message.from_user.last_name, update.message.from_user.username, update.message.chat_id, update.message.from_user.id)
    logging.info(msg)

def  gnac(bot, update):
    if filter(update.message.from_user.id):
        a = '2018-07-26 08:00:00'
        b = '2020-07-26 08:00:00'
        now = datetime.datetime.now()
        start = datetime.datetime.strptime(a, '%Y-%m-%d %H:%M:%S')
        ends = datetime.datetime.strptime(b, '%Y-%m-%d %H:%M:%S')
        diff1 = relativedelta(ends, now)
        diff1_1 = (datetime.date(ends.year, ends.month, ends.day) - datetime.date(now.year, now.month, now.day))
        diff2 = relativedelta(now, start)
        diff2_1 = datetime.date(now.year, now.month, now.day) - datetime.date(start.year, start.month, start.day)
        bot.send_message(chat_id=update.message.chat_id, text="Անցել է")
        bot.send_message(chat_id=update.message.chat_id, text="{} Տարի {} Ամիս {} Օր {} Ժամ {} Րոպե ".format(diff2.years, diff2.months, diff2.days, diff2.hours, diff2.minutes))
        bot.send_message(chat_id=update.message.chat_id, text="{} Օր ".format(diff2_1.days))
        bot.send_message(chat_id=update.message.chat_id, text="{:.3f} % ".format(100*diff2_1.days/731.0))
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Dear {} You are blocked !".format(update.message.from_user.first_name))

    msg = " First Name: {}, Last Name: {}, username: {}, Function: start, chat_id: {}, user_id: {}".format(update.message.from_user.first_name, update.message.from_user.last_name, update.message.from_user.username, update.message.chat_id, update.message.from_user.id)
    logging.info(msg)

start_handler = CommandHandler('start', start)
anekdot_handler = CommandHandler('anekdot', anekdot)
mnac_handler = CommandHandler('mnac', mnac)
gnac_handler = CommandHandler('gnac', gnac)
orbit_handler = CommandHandler('orbit', orbit)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(anekdot_handler)
dispatcher.add_handler(mnac_handler)
dispatcher.add_handler(gnac_handler)
dispatcher.add_handler(orbit_handler)


updater.start_polling()
