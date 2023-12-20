const TelegramBot = require('node-telegram-bot-api');

const token = 'Твой Токен';

// Создайте экземпляр бота
const bot = new TelegramBot(token, {polling: true});

// Обработчик команды /start
bot.onText(/\/start/, (msg) => {
  const chatId = msg.chat.id;
  bot.sendMessage(chatId, 'Привет! Я ваш простой бот.');
});

// Обработчик команды /hello
bot.onText(/\/hello/, (msg) => {
  const chatId = msg.chat.id;
  bot.sendMessage(chatId, 'Привет! Как дела?');
});

// Обработчик любых текстовых сообщений
bot.on('text', (msg) => {
  const chatId = msg.chat.id;
  const messageText = msg.text;

  // Пример простой обработки текстовых сообщений
  if (messageText.toLowerCase().includes('привет')) {
    bot.sendMessage(chatId, 'Привет! Как я могу помочь вам?');
  }
});

// Обработчик кнопок (в этом примере не используется)
bot.on('callback_query', (query) => {
  // Здесь можно обработать нажатие кнопки
  console.log('Кнопка нажата:', query.data);
});

console.log('Бот запущен. Ожидание сообщений...');
