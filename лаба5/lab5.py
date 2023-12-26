import telebot
from telebot import types

TOKEN = '6701836773:AAGXG9Y4alqFn1Ybk7eobXDqfHyskNRcxMc'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('C++')
    item2 = types.KeyboardButton('C#')
    item3 = types.KeyboardButton('C')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}'.format(message.from_user)
                     , reply_markup = markup)
    
@bot.message_handler(content_types =['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'C++':
            bot.send_message(message.chat.id, 'Информационный ресурс - https://learn.microsoft.com/ru-ru/cpp/cpp/cpp-language-reference?view=msvc-170')
            
        elif message.text == 'C':
            bot.send_message(message.chat.id, 'Информационный ресурс - https://learn.microsoft.com/ru-ru/cpp/c-language/c-relational-and-equality-operators?view=msvc-170')
        
        elif message.text == 'C#':
            bot.send_message(message.chat.id, 'Информационный ресурс - https://learn.microsoft.com/ru-ru/dotnet/csharp/')

bot.polling(none_stop = True)