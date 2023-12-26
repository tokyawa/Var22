from telebot import TeleBot

#токен бота
TOKEN = '6920599577:AAHEjR9pOlZ3N3bo_GF1HmdEeN77Q_imlv4'
bot = TeleBot(TOKEN)


#распишем 3 команды
#проверяем работу через старт - ввод: /start вывод: я работаю!!!
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет, как твои дела?")

@bot.message_handler(message='Отлично')
def send(message = "Супер)"):
	bot.reply_to(message, "Супер)")

#бот выводит сообщение идентичное тому, что отправил ему человек
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)
#бот выводит эмодзи
@bot.message_handler(func=lambda msg: msg.text.encode("utf-8") == SOME_FANCY_EMOJI)
def send_something(message):
    pass
#функционирование бота
bot.polling(none_stop=True, interval = 0)