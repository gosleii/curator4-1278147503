import telebot

bot = telebot.TeleBot("7429002934:AAF3EVdgTDm8tGEg4ebWkBwq0YeGPnO2vUk")

@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "Привет! Ты запустил бота 🙋‍♀️\nТут тебя ждёт небольшая подборка случайных статей с википедии\n\nСписок команд:\n/start - Запустить бота\n/lem - Статья про леммингов 🐹\n/chaser - Статья про Toyota Chaser 🚗\n/hardsign - Статья про твёрдый знак 🤔 (Ъ)\n/watermelon - Статья про арбуз 🍉\n/dev - Автор бота🧑‍💻")

@bot.message_handler(commands=["lem"])
def lem_handler(message):
    bot.send_message(message.chat.id, "[*Статья про леммингов 🐹 (ТЫК)*](https://ru.wikipedia.org/wiki/Лемминги)", parse_mode="Markdown")

@bot.message_handler(commands=["chaser"])
def chaser_handler(message):
    bot.send_message(message.chat.id, "[*Статья про Toyota Chaser 🚗 (ТЫК)*](https://ru.wikipedia.org/wiki/Toyota_Chaser)", parse_mode="Markdown")

@bot.message_handler(commands=["hardsign"])
def hardsign_handler(message):
    bot.send_message(message.chat.id, "[*Статья про твёрдый знак 🤔 (Ъ) (ТЫК)*](https://ru.wikipedia.org/wiki/Ъ)", parse_mode="Markdown")

@bot.message_handler(commands=["watermelon"])
def watermelon_handler(message):
    bot.send_message(message.chat.id, "[*Статья про арбуз 🍉 (ТЫК)*](https://ru.wikipedia.org/wiki/Арбуз)", parse_mode="Markdown")

@bot.message_handler(commands=["dev"])
def dev_handler(message):
    bot.send_message(message.chat.id, "*📞\nПо всем насущным жизненным вопросам, можно обратиться ко мне*:\n[(ТЫК)](https://t.me/kapiw0n)", parse_mode="Markdown")

# Тематику круче придумать не смог :(
bot.infinity_polling()