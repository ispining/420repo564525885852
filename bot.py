import telebot

bot = telebot.TeleBot(input('токен: \n'))
keyboard1 = telebot.types.ReplyKeyboardMarkup()
code = '1234'
block = []


def delete_messages(chat_id, message_id):
    block.append(chat_id)
    for i in range(0, message_id + 3):
        try:
            bot.delete_message(chat_id, i)
        except Exception as error:
            pass
    bot.send_message(chat_id, 'Channel deleted')
    
    

@bot.message_handler(commands=['newcode'])
def start_message(message):
    if message.chat.id in block:
        bot.delete_message(message.chat.id, message.message_id)     
    global code
    if message.text[9:]:
        bot.send_message(message.chat.id, 'Code changed:')
        bot.send_message(message.chat.id, message.text[9:])
        code = message.text[9:]



@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.chat.id in block:
        bot.delete_message(message.chat.id, message.message_id) 
    global code
    if message.text == code:
        delete_messages(message.chat.id, message.message_id)  
      
            
@bot.channel_post_handler(content_types=['text'])    
def channelhandler_TextToConsole2(message):
    if message.chat.id in block:
        bot.delete_message(message.chat.id, message.message_id)     
    global code
    if message.text == code:
        delete_messages(message.chat.id, message.message_id)
        

bot.polling()