import telebot
bot = telebot.TeleBot("680513701:AAHHqGqi0D18MHjJhSwLUgL-vn7jSNbtj9E")

@bot.message_handler(content_types = ["text"])
def handle_text(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет.Го общаться.")
    
    elif message.text == "Как поживаешь?" or message.text == "Как дела?":
        bot.send_message(message.from_user.id, "Шикарно")
    
    else:
        bot.send_message(message.from_user.id, "Братишка/сестренка я тебя не понял.Обьясни пожалуйста понятным языком.")



bot.polling(none_stop=True, interval=0)

