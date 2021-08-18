import telebot

TOKEN = "1944695816:AAE7C2exNGLuCyAuRIl3ZxsecLUpvjQEEmU"
#creando una variable que se llama bot
bot = telebot.TeleBot(TOKEN, parse_mode=None) 

@bot.message_handler(commands=['start'])
def saludar(message):
	bot.reply_to(message, "Hola por fin pude hacerlo")

@bot.message_handler(commands=['help'])
def saludar(message):
	bot.reply_to(message, "Hola soy Yelena")

bot.polling()