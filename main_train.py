#dependencies
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

#Setting up the bot
bot=ChatBot('bot')
bot.set_trainer(ListTrainer)

for files in os.listdir('C:/Users/Isabel Elavoko\Desktop\AIG\Chatbot\Dataset\chatterbot-corpus-master\chatterbot_corpus\data\english/'):
    data=open('C:/Users/Isabel Elavoko\Desktop\AIG\Chatbot\Dataset\chatterbot-corpus-master\chatterbot_corpus\data\english/' + files ,'r').readlines()
    bot.train(data)


while True:
	message = input('You:')
	if message.strip() != 'Bye':
		reply = bot.get_response(message)
		print('Zimmy :',reply)
	if message.strip() == 'Bye':
		print('Zimmy : Bye!')
		break
