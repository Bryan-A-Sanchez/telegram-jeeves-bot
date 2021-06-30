import telebot
import random
import urllib

daddy_bot = telebot.TeleBot("") # bot id must be entered into parentheses

command_list = '''\
Commands are case sensitive:
/comms - List of currently available commands
/hi - Says hi back
/fb insertNameHere - Casts a fireball at specified name for 0 - 100 damage
/hs insertCardNameHere - Shows an image of the requested card. Name of card is not case sensitive.
'''
	
@daddy_bot.message_handler(commands=['hi', 'hello'])
def say_hello(message):
	#daddy_bot.reply_to(message, "Howdy, how are you doing?")
	daddy_bot.send_message(message.chat.id, random.choice(['Hello @', 'Hi @', 'What\'s up @', 'Papi is here, what\'s up @']) + message.from_user.first_name)

@daddy_bot.message_handler(commands=['comms'])
def send_command_list(message):
	daddy_bot.send_message(message.chat.id, command_list)

@daddy_bot.message_handler(commands=['fb'])
def cast_fireball(message):
	damage = random.randrange(0,101)

	if(damage <= 95 and damage > 10):
		daddy_bot.send_message(message.chat.id, '@{} casts a 🔥fireball🔥 to @{} for {} Damage'.format(message.from_user.first_name, 
			message.text.replace('/fb ', ''), damage) )
	elif(damage <= 10):
		daddy_bot.send_message(message.chat.id, '@{} casts a 🔥fireball🔥 to @{} for 💩{}💩 Damage. Better cast again! '.format(message.from_user.first_name, 
					message.text.replace('/fb ', ''), damage) )
	elif(damage == 100):
		daddy_bot.send_message(message.chat.id, '@{} casts a 🔥fireball🔥 to @{} for {} Damage. 🎯Critical Hit🎯!.'.format(message.from_user.first_name, 
					message.text.replace('/fb ', ''), damage) )
	else:
		daddy_bot.send_message(message.chat.id, '@{} casts a 🔥fireball🔥 to @{} for {} Damage. ☠️rip☠️.'.format(message.from_user.first_name, 
					message.text.replace('/fb ', ''), damage) )


@daddy_bot.message_handler(commands=['hs'])
def show_hearthstone_card(message):
	card = message.text.replace('/hs ', '').replace(' ','-')
	try:
		daddy_bot.send_photo(message.chat.id, 'https://www.hearthstonetopdecks.com/cards/{}/'.format(card) )
	except telebot.apihelper.ApiException:
		daddy_bot.send_message(message.chat.id, 'Can not find {} card, please check spelling'.format(card.replace('-', ' ')))


@daddy_bot.message_handler(func=lambda m: True)
def command_not_found(message):
	daddy_bot.send_message(message.chat.id, "Currently not a command: " + message.text)

print('Starting Polling...')

daddy_bot.polling()



