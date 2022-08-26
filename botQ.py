import telebot
from telebot import types

TOKEN = '5794385260:AAGZxeEDjzu4QHFlLPj70DPdHh3XcqzTcUw'

bot = telebot.TeleBot(TOKEN)
row = ['1', '2','3','4','5','6','7','8','9','10']
row2 = ['1.', '2.', '3.', '4.', '5.']
row3 = ['no_0', 'yes_10', 'yes_30']


def read_info(message, text,  question):
    user_id = ''
    if message.from_user.is_bot:
        user_id = message.chat.id
    else:
        user_id = message.from_user.id
    with open('bd_file.txt', 'a') as bd:
        bd.write(f"{user_id}*{question}*{text}'\n'")


@bot.message_handler(commands=['start'])
def helper(message):
    text = ''' Добрый день, мы команда специалистов, которая планирует разработать мобильное решение, 
которое будет наполнено инструментами, позволяющими справиться со сложными эмоциями, который порой у 
нас возникают во взаимоотношениях с близкими людьми, прежде всего с гневом. Мы можем кричать, ругаться, 
ломать предметы и вести себя агрессивно, что обижает и расстраивает в последствии и нас, и наших близких.
Нам очень поможет ваше мнение и ожидания от подобного решения. Пожалуйста, найдите 15 минут времени и 
заполните небольшой конфиденциальный опросник ниже. Нажмите /poll . Спасибо вам за помощь!
'''
    with_name = message.from_user.first_name + ', ' + text
    bot.reply_to(message, with_name)




@bot.message_handler(commands=['poll'])
def poll(message):
    one = "1.Страна проживания"
    bot.send_message(message.chat.id, one)
    bot.register_next_step_handler(message, get_two)

def get_two(message):
    two = '2.Пол'
    question = '1'
    read_info(message, message.text, question)
    keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
    gender_man = types.InlineKeyboardButton(text='M', callback_data='M') #кнопка «M»
    gender_woman = types.InlineKeyboardButton(text='Ж', callback_data='Ж') #кнопка «Ж»
    keyboard.row(gender_woman)
    keyboard.row(gender_man)
    bot.send_message(message.chat.id, two, reply_markup=keyboard)



#@bot.message_handler(commands=['three'])
def get_three(message):
    three = "3.Возраст "
    question = '2'
    keyboard = types.InlineKeyboardMarkup()
    age_1 = types.InlineKeyboardButton(text='21-30', callback_data='21-30')
    age_2 = types.InlineKeyboardButton(text='31-45', callback_data='31-45')
    age_3 = types.InlineKeyboardButton(text='Старше 45', callback_data='Старше 45')
    keyboard.add(age_1, age_2, age_3)
    bot.send_message(message.chat.id, three, reply_markup=keyboard)
    


def get_fourth(message):
    fourth = '4.Образование:'
    question = '3'
    keyboard = types.InlineKeyboardMarkup()
    edu_1 = types.InlineKeyboardButton(text='Высшее', callback_data='Высшее')
    edu_2 = types.InlineKeyboardButton(text='Среднее специальное', callback_data='Среднее специальное')
    edu_3 = types.InlineKeyboardButton(text='Среднее', callback_data='Среднее')
    edu_4 = types.InlineKeyboardButton(text='Другое', callback_data='Другое')
    #keyboard.add(edu_1, edu_2, edu_3, edu_4)
    keyboard.row(edu_1, edu_3)
    keyboard.row(edu_2)
    keyboard.row(edu_4)
    bot.send_message(message.chat.id, fourth, reply_markup=keyboard)
    #if message.text != fourth:
        #bot.register_next_step_handler(message, get_fifth)

def get_fifth(message):
    fifth = '''5.Как вы оцениваете уровень вашего взаимодействия с мобильными приложениями по 10-ти балльной шкале, где 10 - это опытный пользователь, а 0 - необходима помощь при установке и работе с приложениями?'''
    question = '4'
    keyboard = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton(text='1', callback_data='1')
    b = types.InlineKeyboardButton(text='2', callback_data='2')
    c = types.InlineKeyboardButton(text='3', callback_data='3')
    e = types.InlineKeyboardButton(text='4', callback_data='4')
    f = types.InlineKeyboardButton(text='5', callback_data='5')
    g = types.InlineKeyboardButton(text='6', callback_data='6')
    o = types.InlineKeyboardButton(text='7', callback_data='7')
    p = types.InlineKeyboardButton(text='8', callback_data='8')
    r = types.InlineKeyboardButton(text='9', callback_data='9')
    d = types.InlineKeyboardButton(text='10', callback_data='10')
    keyboard.row(a, b, c, e, f)
    keyboard.row(g, o, p, r, d)
    bot.send_message(message.chat.id, fifth, reply_markup=keyboard)
    #if message.text != fifth:
        #bot.register_next_step_handler(message, get_sixth)


def get_sixth(message):
    sixth = '6.Какой мобильной операционной системой вы пользуетесь сейчас?'
    question = '5'
    keyboard = types.InlineKeyboardMarkup()
    android = types.InlineKeyboardButton(text='Android', callback_data='Android')
    iOS = types.InlineKeyboardButton(text='iOS', callback_data='iOS')
    keyboard.add(android, iOS)
    bot.send_message(message.chat.id, sixth, reply_markup=keyboard)
    #if message.text != sixth:
        #bot.register_next_step_handler(message, get_seventh)

def get_seventh(message):
    seventh = '''7.Нужно ли вам время от времени такое приложение? Было бы оно полезно? Оцените по 5-ти балльной шкале, где 5 - безусловно пригодилось бы, а 0 - это бесполезная идея, я и сам могу справиться со своими чувствами.'''
    question = '6'
    keyboard = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton(text='1', callback_data='1.')
    b = types.InlineKeyboardButton(text='2', callback_data='2.')
    c = types.InlineKeyboardButton(text='3', callback_data='3.')
    e = types.InlineKeyboardButton(text='4', callback_data='4.')
    f = types.InlineKeyboardButton(text='5', callback_data='5.')
    keyboard.row(a, b, c, e, f)
    bot.send_message(message.chat.id, seventh, reply_markup=keyboard)
    #if message.text != seventh:
       # bot.register_next_step_handler(message, get_еighth)
    


def get_еighth(message):
    еighth='''8.Есть ли уже у в вашем арсенале приложения, которые помогают вам расслабиться в момент, 
когда вы испытываете сложные эмоции? 
Что это за приложения? Что в них вам помогает? Опишите, пожалуйста, коротко.'''
    question = '7'
    #keyboard = types.InlineKeyboardMarkup()
    #еighth_btn = types.InlineKeyboardButton(text='Пропустить', callback_data='еighth')
    #keyboard.add(еighth_btn)
    bot.send_message(message.chat.id, еighth)
    bot.register_next_step_handler(message, get_ninth)


@bot.message_handler(commands=['Question9'])
def get_ninth(message):
    question = '8'
    read_info(message, message.text, question)
    ninth = '''9.Что бы вы хотели видеть в таком приложении? 
Напишите, пожалуйста, ваши идеи и рекомендации.'''
    #keyboard = types.InlineKeyboardMarkup()
    #ninth_btn = types.InlineKeyboardButton(text='Пропустить', callback_data='ninth')
    #keyboard.add(ninth_btn)
    bot.send_message(message.chat.id, ninth)
    bot.register_next_step_handler(message, get_tenth)


def get_tenth(message):
    tenth = '10.Готовы ли вы оформить подписку на такое мобильное приложение, когда оно будет готово?'
    question = '9'
    read_info(message, message.text, question)
    keyboard = types.InlineKeyboardMarkup()
    no_0 = types.InlineKeyboardButton(text='Нет', callback_data='no_0')
    yes_10 = types.InlineKeyboardButton(text='Да, но до 10$ в месяц', callback_data='yes_10')
    yes_30 = types.InlineKeyboardButton(text='Я бы и более 30$ платил, если полезно', callback_data='yes_30')
    keyboard.row(no_0)
    keyboard.row(yes_10)
    keyboard.row(yes_30)
    bot.send_message(message.chat.id, tenth, reply_markup=keyboard)
    #if message.text != tenth:
        #bot.register_next_step_handler(message, get_finish)

def get_finish(message):
    question = '10'
    name = ''
    if message.from_user.is_bot:
        #print(message)
        name = message.chat.first_name
    else:
        name = message.from_user.first_name
    with_name = name + ', Cпасибо!'
    bot.send_message(message.chat.id, with_name)



@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "M":
        question = '2'
        read_info(call.message, call.data, question)
        get_three(call.message)
    if call.data == "Ж":
        question = '2'
        read_info(call.message, call.data, question)
        #bot.send_message(call.message.chat.id, "/three")
        get_three(call.message)
    if call.data == "21-30":
        question = '3'
        read_info(call.message, call.data, question)
        #bot.send_message(call.message.chat.id, "21-30")
        get_fourth(call.message)
    if call.data == "31-45":
        question = '3'
        read_info(call.message, call.data, question)
        #bot.send_message(call.message.chat.id, "31-45")
        get_fourth(call.message)
    if call.data == "Старше 45":
        question = '3'
        read_info(call.message, call.data, question)
        #bot.send_message(call.message.chat.id, "Старше 45")
        get_fourth(call.message)
    if call.data == "Высшее":
        question = '4'
        read_info(call.message, call.data, question)
        #bot.send_message(call.message.chat.id, "Высшее")
        get_fifth(call.message)
    if call.data == "Среднее специальное":
        question = '4'
        read_info(call.message, call.data, question)
        #bot.send_message(call.message.chat.id, "Среднее специальное")
        get_fifth(call.message)
    if call.data == "Среднее":
        question = '4'
        read_info(call.message, call.data, question)
        #bot.send_message(call.message.chat.id, "Среднее")
        get_fifth(call.message)
    if call.data == "Другое":
        question = '4'
        read_info(call.message, call.data, question)
        #bot.send_message(call.message.chat.id, "Другое")
        get_fifth(call.message)
    if call.data in row:
        question = '5'
        read_info(call.message, call.data, question)
        #bot.send_message(call.message.chat.id, call.data)
        get_sixth(call.message)
    if call.data == "Android":
        question = '6'
        read_info(call.message, call.data, question)
        #bot.send_message(call.message.chat.id, "Android")
        get_seventh(call.message)
    if call.data == "iOS":
        question = '6'
        read_info(call.message, call.data, question)
        #bot.send_message(call.message.chat.id, "iOS")
        get_seventh(call.message)
    if call.data in row2:
        question = '7'
        read_info(call.message, call.data, question)
        #bot.send_message(call.message.chat.id, call.data)
        get_еighth(call.message)
    if call.data in row3:
        question = '10'
        read_info(call.message, call.data, question)
        #bot.send_message(call.message.chat.id, call.data)
        get_finish(call.message)


bot.polling(none_stop=True)