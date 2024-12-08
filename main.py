from telebot import TeleBot
from constans import TOKEN
from todo.controllers import Controller
bot = TeleBot(TOKEN)
controller = Controller(bot)
controller.register_handlers()
if __name__ == "__main__":
    print("Bot is starting...")
    bot.polling()
    
