import telebot
from urllib.request import urlopen
from bs4 import BeautifulSoup

bot = telebot.TeleBot("5730197111:AAH7hq8hEMKdKKCyyNhlODNVqT-Q2c5J0o8")

@bot.message_handler(commands=['start', 'hello'])
def start_message(message):
    bot.send_message(message.chat.id, "Hello there my dear user!")

@bot.message_handler(commands=['update'])
def update_message(message):
    response = urlopen("https://kurs.onliner.by/")
    soup = BeautifulSoup(response)
    tag_list = soup.find_all('p', {'class':'value'})
    buy = tag_list[0].text
    sell = tag_list[1].text
    nb = tag_list[2].text

    bot.send_message(message.chat.id, f"Buy: {buy}, sell: {sell}, nb: {nb}")