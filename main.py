from bot import bot

# bot commands implementation
import commands.users
import commands.extracts

# default hello world
@bot.message_handler(commands=['online'])
def hello_world(message):
    bot.send_message(message.chat.id, "seja bem vindo")

bot.infinity_polling()
