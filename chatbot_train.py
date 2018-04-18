#dependencies
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

#Setting up the bot
bot=ChatBot('bot')
bot.set_trainer(ListTrainer)

#Path of where the dataset is
for files in os.listdir('C:/Users/Isabel Elavoko\Desktop\AIG\Chatbot\Dataset\chatterbot-corpus-master\chatterbot_corpus\data\oshikwanyama/'):
    data=open('C:/Users/Isabel Elavoko\Desktop\AIG\Chatbot\Dataset\chatterbot-corpus-master\chatterbot_corpus\data\oshikwanyama/' + files ,'r').readlines()
    bot.train(data)
	

while True:
	print('----------------------------------------------------------')
	print('Say Something!')
	message = input('You:')
	if message.strip() != 'Bye':
		reply = bot.get_response(message)
		print('Zimmy :',reply)
	if message.strip() == 'Bye':
		print('Zimmy : GodBye :-)')
		print('----------------------------------------------------------')
		break

		#C:\Users\Isabel Elavoko\Desktop\AIG\Chatbot\Dataset\chatterbot-corpus-master\chatterbot_corpus\data\oshikwanyama
		#C:/Users/Isabel Elavoko\Desktop\AIG\Chatbot\Dataset\chatterbot-corpus-master\chatterbot_corpus\data\english/