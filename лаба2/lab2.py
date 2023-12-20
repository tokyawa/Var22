from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

TOKEN = 'Токен Вашего Бота'

def start(update, context):
    user = update.message.from_user
    update.message.reply_text(f"Добрый день, {user.first_name}! Я бот, обладающий кнопками")

def show_buttons(update, context):
    keyboard = [[InlineKeyboardButton("Кнопка 1", callback_data='unique_button1')],
                [InlineKeyboardButton("Кнопка 2", callback_data='unique_button2')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Выберите одну из кнопок:', reply_markup=reply_markup)

def button_callback(update, context):
    query = update.callback_query
    button_data = query.data
    update.callback_query.answer(f'Вы нажали на уникальную кнопку: {button_data}')

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("buttons", show_buttons))
    dp.add_handler(CallbackQueryHandler(button_callback))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

