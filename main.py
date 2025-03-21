import telebot

bot = telebot.TeleBot('7262591637:AAHWKYb2p-3eQYWQ3jR6M2q1BcvEa7Y1tkc')



# @bot.message_handler()
# def info(message):
#     if message.text.lower() =='Привет':
#         bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
#     elif message.text.lower() == 'id':
#         bot.reply_to(message, f'ID: {message.from_user.id}')

# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = type.ReplyKeyboardMarkup()
#     btn1 = type.KeyboardButton('о мне')
#     markup.row(btn1)

#     bot.register_next_step_handler(message, on_click)

# def on_click(message):
#     if message.text == 'о мне':
#         bot.send_message(message.chat.id, 'меня завут Элмырза я живу в Кыргызстане и мне 14лет')


@bot.message_handler(commands=['aboutme'])
def about(message):
    bot.send_message(message.chat.id, 'Меня зовут Элмырза я из Кыргызстана и мне 14 лет')

@bot.message_handler(commands=['start','hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')

    
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'что бы начать разговор нажмити на /start', parse_mode='html')





@bot.message_handler(commands=['myhobby'])
def hobby(message):
    bot.send_message(message.chat.id, 'мой хобби играть валейбол') 


@bot.message_handler(commands=['class'])
def Сlass(message):
    bot.send_message(message.chat.id, 'Я учус в 8 классе')

    
@bot.message_handler(commands=['dateofbirth'])
def data(message):
    bot.send_message(message.chat.id, '28.12.2010')


@bot.message_handler(commands=['mybeautifulcar'])
def car(message):
    bot.send_message(message.chat.id, 'Tayota')


@bot.message_handler(commands=['mybestfriend'])
def best(message):
    bot.send_message(message.chat.id, '@ACdDNYi @inv0lv3d @Aku09092010 @Aisezim_Aibekovna @xxoasi_3')
 

 
@bot.message_handler(commands=['music'])
def music(message):
    bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=l61l0AtSg2Y')
bot.polling(none_stop=True)





