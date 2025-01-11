# импорт
import telebot as tb
from telebot import types
import random as rand

# подключение к боту
bot = tb.TeleBot('7705755205:AAFeOIgU8OHxJTDK0NMx9timoqvy4YHtWAo')

# переменные
members = {}
games_sorn = {}
games_sorn2 = {}
st1 = open('save_stars.txt')
st2 = open('save_stars2.txt')
sorn_elements = {'Кошка': False, 'Яблоко':True, 'Сыр':True, 'Лось':False, 'Лещ':True, 'Сок':True, 'Вода':True, 'Змея':False, 'Ёлка':False, 'Ты':False, 'Рыба':True, 'Икра':True, 'Сапог':False, 'Бот':False, 'Самолёт':False, 'Камень':False, 'Батарейка':False, 'Банан':True}
sorn_elements2 = ['Кошка','Яблоко','Сыр','Лось','Лещ','Сок','Вода','Змея','Ёлка','Ты','Рыба','Икра','Сапог','Бот','Самолёт','Камень','Батарейка','Банан']
stars = {}
stars2 = {}
stars3 = {} # Главные Звёзды
stars4 = {}
one = ['Кошка', 'Собака', 'Крыса', 'Стол', 'Лось', 'Пекарь', 'Баран', 'Бот', 'Компьютер', 'Банка', 'Лиса', 'Ножницы', 'Дом']
two = ['ищет', 'роет', 'льёт', 'тыкает', 'рисует', 'пишет', 'лижет', 'прыгает', 'играет на пианино', 'играет в']
three = ['котика', 'кротика', 'ёлочку', 'телеграм', 'ботика', 'телефон', 'шарик', 'рыбку', 'фломастер', 'иглу', 'ленту']
four = ['в туалете', 'на воде', 'в ракете', 'в пикселе', 'в желудке', 'на таблетке', 'в учебнике', 'в телефоне', 'в проводе']

# функция '/start'
@bot.message_handler(commands=['start'])
def start_bot(mess):
    id = mess.chat.id
    hello_mess = '<b>Всем</b> привет🖐! В этой группе бот-админ. У меня есть такие функции:\n  /chepuha\n  /groupgames :\n    /vsbot\n    /vsgroup\n    /samzasebya\n    /sorn\n    /englesh :\n      /rlub\n      /veg'
    markup = types.ReplyKeyboardMarkup()
    key1 = types.KeyboardButton(text='➕Принять участие в играх')
    key2 = types.KeyboardButton(text='➖Не принимать участие в играх')
    markup.add(key1, key2)
    bot.send_message(id, hello_mess, parse_mode='html', reply_markup=markup)
    members.update({id : []})
    stars.update({mess.chat.id : {}})
    stars2.update({mess.chat.id : []})
    try:
        stars4[mess.chat.id]
    except:
        stars3.update({mess.chat.id : {}})
        stars4.update({mess.chat.id : []})

# функция '/chepuha'
@bot.message_handler(commands=['chepuha'])
def chepuha_bot(mess):
    ch_mess = rand.choice(one)+' '+rand.choice(two)+' '+rand.choice(three)+' '+rand.choice(four)+'.'
    markup = types.ReplyKeyboardMarkup()
    bot.send_message(mess.chat.id, ch_mess, parse_mode='html', reply_markup=markup)

# функция '/groupgames'
@bot.message_handler(commands=['groupgames'])
def groupgames_bot(mess):
    id = mess.chat.id
    games_mess = 'Выберите игру:\n/vsbot\n/vsgroup\n/samzasebya\n/sorn\n/englesh :\n  /rlub\n  /veg'
    markup = types.ReplyKeyboardMarkup()
    bot.send_message(id, games_mess, parse_mode='html', reply_markup=markup)

# функциИ '/groupgames'
commands = ['vsbot', 'vsgroup', 'samzasebya', 'sorn']
@bot.message_handler(commands=['sorn'])
def game(mess):
    global in_sorn
    message = '<b>/sorn</b> -\nигра "Съедобное или нет".\nЗвучит просто, но если в группе много участников...🫥\nДело в том😂, что кто быстрее других и правильно ответит тот победит.\nПобедитель заработает звезду🤩.\nНачнём?'
    markup = types.ReplyKeyboardMarkup()
    key1 = types.KeyboardButton(text='Да')
    key2 = types.KeyboardButton(text='Нет')
    markup.add(key1, key2)
    bot.send_message(mess.chat.id, message, parse_mode='html', reply_markup=markup)
    games_sorn.update({mess.chat.id : True})
    try:
        stars[mess.chat.id].update({mess.from_user.id : 0})
        stars2[mess.chat.id].append(mess.from_user.id)
    except:
        stars.update({mess.chat.id : {}})
        stars2.update({mess.chat.id : []})
        stars[mess.chat.id].update({mess.from_user.id : 0})
        stars2[mess.chat.id].append(mess.from_user.id)
    
# функция '/vsbot'
@bot.message_handler(commands=['vsbot'])
def vsbot_bot(mess):
    id = mess.chat.id
    instruction = 'Правила:\nБот выбирает '+str(bot.get_chat_members_count)+' игроков.'

# inline mode
@bot.inline_handler(func=lambda query: True)
def inline(query):
    text = query.query
    ReturnText = 'Вы не всё сделали'
    description = 'Займы'
    if text == '':
        title = 'Введите через запятую: цена, username вашего собеседника, username группы'
    else:
        try:
            error = 0
            List = eval('['+text+']')
            '''try:
                List = eval('['+text+']')
            except:
                pass
            
            error = 1
            List[0] + 1
            
            error = 2
            if len(List) >= 2:
                List[1] + 'a'
            
            error = 3
            if len(List) >= 3:
                List[2] + 'a'
            
            error = 4
            if len(List) >= 2:
                None
            
            error = 5
            if len(List) >= 3:
                bot.get_chat(List[2])
            
            error = 6
            if len(List) >= 3:
                bot.get_chat_member(List[2], List[1])'''
            if len(List) == 3:
                title = 'Готово'
                ReturnText = 'Я хочю взять у тебя займы ценой 🤩'+str(List[0])+' в группе '+bot.get_chat(List[2]).title+'.'
            else:
                title = 'Почти готово'
        except Exception as e:
            print(e)
            title = 'Ошибочка! '
            if error == 0:
                title += 'Неправильная структура'
            elif error == 1:
                title += 'Цена должна быть числом'
            elif error == 2:
                title += 'Username, пожалуйста, напишите в кавычках'
            elif error == 3:
                title += 'Username, пожалуйста, напишите в кавычках'
            elif error == 4:
                title += 'Не найден пользователь'
            elif error == 5:
                title += 'Не найдена группа'
            elif error == 6:
                title += 'Пользователь даже не пытался получить звёзды'
    answer = [types.InlineQueryResultArticle(
        id = '1',
        title = title,
        description = description,
        input_message_content = types.InputTextMessageContent(message_text=ReturnText))]
    bot.answer_inline_query(query.id, answer)

# если что-то написали
@bot.message_handler(func=lambda m:True)
def write(mess):
    if mess.text == '➕Принять участие в играх':
        print('➕Принять участие в играх')
        NewMember = mess.from_user.id
        print(NewMember)
        plas = True
        try:
            for member in members[mess.chat.id]:
                if member == NewMember:
                    plas = False
        except:
            members.update({mess.chat.id : []})
            for member in members[mess.chat.id]:
                if member == NewMember:
                    plas = False
        if plas:
            try:
                NewListMembers = members[mess.chat.id]
                NewListMembers.append(NewMember)
                members.update({mess.chat.id : NewListMembers})
            except:
                members.update({mess.chat.id : []})
                NewListMembers = members[mess.chat.id]
                NewListMembers.append(NewMember)
                members.update({mess.chat.id : NewListMembers})
            pl = '@'+mess.from_user.username+' будет <b>участвовать в играх</b>.\n\nВ этой группе участвуют в играх:\n'
            i = 0
            for member in members[mess.chat.id]:
                i += 1
                pl += '@'+bot.get_chat_member(mess.chat.id, member).user.username
                if i == len(members[mess.chat.id]):
                    pl += '.'
                else:
                    pl += ';\n'
            markup = types.InlineKeyboardMarkup()
            bot.send_message(mess.chat.id, pl, parse_mode='html', reply_markup=markup)
        else:
            pl = '@'+mess.from_user.username+' <b>уже</b> участвует в играх.'
            markup = types.InlineKeyboardMarkup()
            bot.send_message(mess.chat.id, pl, parse_mode='html', reply_markup=markup)
    elif mess.text == '➖Не принимать участие в играх':
        try:
            members[mess.chat.id].pop(members[mess.chat.id].index(mess.from_user.id))
            delete_mess = '@'+mess.from_user.username+' <b>не будет</b> участвовать в играх.'
            markup = types.InlineKeyboardMarkup()
            bot.send_message(mess.chat.id, delete_mess, parse_mode='html', reply_markup=markup)
        except:
            delete_mess = '@'+mess.from_user.username+' <b>итак не участвует</b> в играх.'
            markup = types.InlineKeyboardMarkup()
            bot.send_message(mess.chat.id, delete_mess, parse_mode='html', reply_markup=markup)
    try:
        if games_sorn[mess.chat.id]:
            if mess.text == 'Да':
                message = 'Хорошо, тогда начнём.\n(Чтобы ответить, нажимайте на кнопки👇.)'
                markup = types.ReplyKeyboardMarkup()
                key1 = types.KeyboardButton(text='Съедобное')
                key2 = types.KeyboardButton(text='Несъедобное')
                markup.add(key1, key2)
                bot.send_message(mess.chat.id, message, parse_mode='html', reply_markup=markup)
                #games_sorn.update({mess.chat.id : True})
                startElem = rand.choice(sorn_elements2)
                games_sorn2.update({mess.chat.id : {'whatNum' : 0, 'what' : startElem}})
                markup = types.ReplyKeyboardMarkup()
                bot.send_message(mess.chat.id, startElem, parse_mode='html', reply_markup=markup)
            if mess.text == 'Съедобное' or mess.text == 'Несъедобное':
                iffer = True
                markup = types.InlineKeyboardMarkup()
                for i in stars2[mess.chat.id]:
                    if i == mess.from_user.id:
                        iffer = False
                if iffer:
                    stars[mess.chat.id].update({mess.from_user.id : 0})
                    stars2[mess.chat.id].append(mess.from_user.id)
                iffer = True
                for i in stars4[mess.chat.id]:
                    if i == mess.from_user.id:
                        iffer = False
                if iffer:
                    stars3[mess.chat.id].update({mess.from_user.id : 0})
                    stars4[mess.chat.id].append(mess.from_user.id)
                startElem = rand.choice(sorn_elements2)
                doljno = sorn_elements[startElem]
                if doljno:
                    doljno2 = 'Съедобное'
                else:
                    doljno2 = 'Несъедобное'
                if doljno2 == mess.text:
                    stars[mess.chat.id][mess.from_user.id] += 1
                    print(stars)
                for i in stars2[mess.chat.id]:
                    if stars[mess.chat.id][i] == 20:
                        try:
                            stars3[mess.chat.id][i] += 1
                        except:
                            stars3.update({mess.chat.id : {}})
                        print(stars3)
                        games_sorn[mess.chat.id] = False
                        startElem = 'Стоп игра. Звёзды:\n'
                        for i in stars4[mess.chat.id]:
                            print(i)
                            try:
                                startElem += '@'+bot.get_chat_member(mess.chat.id, i).user.username+': 🤩'+str(stars3[mess.chat.id][i])+'\n'
                            except Exception as E:
                                print(E)
                        markup = types.InlineKeyboardMarkup()
                        startElem += 'Можете зайти магазин / подарки нажав на кнопку внизу'
                        key = types.InlineKeyboardButton(text = 'магазин / подарки', callback_data=str(mess.chat.id))
                        markup.add(key)
                games_sorn2.update({mess.chat.id : {'whatNum' : 0, 'what' : startElem}})
                try:
                    bot.send_message(mess.chat.id, startElem, parse_mode='html', reply_markup=markup)
                except Exception as d:
                    print(d)
            elif mess.text == 'Нет':
                message = 'Хорошо'
                markup = types.ReplyKeyboardMarkup()
                bot.send_message(mess.chat.id, message, parse_mode='html', reply_markup=markup)
                games_sorn.update({mess.chat.id : False})

    except:
        pass

# если нажали на кнопку
@bot.callback_query_handler(func=lambda call:True)
def button_bot(fc):
    mess = fc.message
    print('but')
    data = ''
    data2 = []
    for i in fc.data:
        data2.append(i)
    try:
        data = data2[0]+data2[1]+data2[2]+data2[3]+data2[4]+data2[5]+data2[6]
    except:
        pass
    if data == 'Podarok':
        chat_id = ''
        for i in range(7, len(data2)):
            chat_id += data2[i]
        chat_id = int(chat_id)
        markup = types.InlineKeyboardMarkup()
        for i in stars2[chat_id]:
            bt = bot.get_chat_member(chat_id, i).user.first_name
            key = types.InlineKeyboardButton(text=bt, callback_data='User['+str(i)+', '+str(chat_id)+']')
            markup.add(key)
        bot.edit_message_text(text='🎁Подарок\nВыберите того, кому хотите подарить подарок', chat_id=fc.from_user.id, message_id=mess.id, reply_markup=markup)
    data = ''
    data2 = []
    for i in fc.data:
        data2.append(i)
    try:
        data = data2[0]+data2[1]+data2[2]+data2[3]
    except:
        pass
    if data == 'User':
        list_id = ''
        for i in range(4, len(data2)):
            list_id += data2[i]
        list_id = eval(list_id)
        key = int(stars3[list_id[1]][list_id[0]]/2)
        markup = types.InlineKeyboardMarkup(row_width=4)
        list_id.append(key)
        key1 = types.InlineKeyboardButton(text='+🤩1', callback_data='+e'+str(list_id))
        key2 = types.InlineKeyboardButton(text='-🤩1', callback_data='-e'+str(list_id))
        key3 = types.InlineKeyboardButton(text='+🤩10', callback_data='+d'+str(list_id))
        key4 = types.InlineKeyboardButton(text='-🤩10', callback_data='-d'+str(list_id))
        key5 = types.InlineKeyboardButton(text='Готово', callback_data='Go'+str(list_id))
        markup.add(key1, key2, key3, key4, key5)
        message = 'Хорошо, Вы дарите подарок '+bot.get_chat_member(list_id[1], list_id[0]).user.first_name+'.\n\nВыберите количество звёзд:\n🤩'+str(key)
        bot.edit_message_text(text=message, chat_id=fc.from_user.id, message_id=mess.id, reply_markup=markup)

    data = ''
    data2 = []
    for i in fc.data:
        data2.append(i)
    try:
        data = data2[0]+data2[1]
    except:
        pass
    print(data)
    if data == '+e':
        list_id = ''
        for i in range(2, len(data2)):
            list_id += data2[i]
        list_id = eval(list_id)
        key = list_id[2]+1
        list_id[2] += 1
        markup = types.InlineKeyboardMarkup(row_width=4)
        key1 = types.InlineKeyboardButton(text='+🤩1', callback_data='+e'+str(list_id))
        key2 = types.InlineKeyboardButton(text='-🤩1', callback_data='-e'+str(list_id))
        key3 = types.InlineKeyboardButton(text='+🤩10', callback_data='+d'+str(list_id))
        key4 = types.InlineKeyboardButton(text='-🤩10', callback_data='-d'+str(list_id))
        key5 = types.InlineKeyboardButton(text='Готово', callback_data='Go'+str(list_id))
        markup.add(key1, key2, key3, key4, key5)
        message = 'Хорошо, Вы дарите подарок '+bot.get_chat_member(list_id[1], list_id[0]).user.first_name+'.\n\nВыберите количество звёзд:\n🤩'+str(key)
        bot.edit_message_text(text=message, chat_id=fc.from_user.id, message_id=mess.id, reply_markup=markup)
    if data == '-e':
        list_id = ''
        for i in range(2, len(data2)):
            list_id += data2[i]
        list_id = eval(list_id)
        key = list_id[2]-1
        list_id[2] -= 1
        markup = types.InlineKeyboardMarkup(row_width=4)
        key1 = types.InlineKeyboardButton(text='+🤩1', callback_data='+e'+str(list_id))
        key2 = types.InlineKeyboardButton(text='-🤩1', callback_data='-e'+str(list_id))
        key3 = types.InlineKeyboardButton(text='+🤩10', callback_data='+d'+str(list_id))
        key4 = types.InlineKeyboardButton(text='-🤩10', callback_data='-d'+str(list_id))
        key5 = types.InlineKeyboardButton(text='Готово', callback_data='Go'+str(list_id))
        markup.add(key1, key2, key3, key4, key5)
        message = 'Хорошо, Вы дарите подарок '+bot.get_chat_member(list_id[1], list_id[0]).user.first_name+'.\n\nВыберите количество звёзд:\n🤩'+str(key)
        bot.edit_message_text(text=message, chat_id=fc.from_user.id, message_id=mess.id, reply_markup=markup)
    if data == '+d':
        list_id = ''
        for i in range(2, len(data2)):
            list_id += data2[i]
        list_id = eval(list_id)
        key = list_id[2]+10
        list_id[2] += 10
        markup = types.InlineKeyboardMarkup(row_width=4)
        key1 = types.InlineKeyboardButton(text='+🤩1', callback_data='+e'+str(list_id))
        key2 = types.InlineKeyboardButton(text='-🤩1', callback_data='-e'+str(list_id))
        key3 = types.InlineKeyboardButton(text='+🤩10', callback_data='+d'+str(list_id))
        key4 = types.InlineKeyboardButton(text='-🤩10', callback_data='-d'+str(list_id))
        key5 = types.InlineKeyboardButton(text='Готово', callback_data='Go'+str(list_id))
        markup.add(key1, key2, key3, key4, key5)
        message = 'Хорошо, Вы дарите подарок '+bot.get_chat_member(list_id[1], list_id[0]).user.first_name+'.\n\nВыберите количество звёзд:\n🤩'+str(key)
        bot.edit_message_text(text=message, chat_id=fc.from_user.id, message_id=mess.id, reply_markup=markup)
    if data == '-d':
        list_id = ''
        for i in range(2, len(data2)):
            list_id += data2[i]
        list_id = eval(list_id)
        key = list_id[2]-10
        list_id[2] -= 10
        markup = types.InlineKeyboardMarkup(row_width=4)
        key1 = types.InlineKeyboardButton(text='+🤩1', callback_data='+e'+str(list_id))
        key2 = types.InlineKeyboardButton(text='-🤩1', callback_data='-e'+str(list_id))
        key3 = types.InlineKeyboardButton(text='+🤩10', callback_data='+d'+str(list_id))
        key4 = types.InlineKeyboardButton(text='-🤩10', callback_data='-d'+str(list_id))
        key5 = types.InlineKeyboardButton(text='Готово', callback_data='Go'+str(list_id))
        markup.add(key1, key2, key3, key4, key5)
        message = 'Хорошо, Вы дарите подарок '+bot.get_chat_member(list_id[1], list_id[0]).user.first_name+'.\n\nВыберите количество звёзд:\n🤩'+str(key)
        bot.edit_message_text(text=message, chat_id=fc.from_user.id, message_id=mess.id, reply_markup=markup)
    if data == 'Go':
        list_id = ''
        for i in range(2, len(data2)):
            list_id += data2[i]
        list_id = eval(list_id)
        if list_id[2] > 0 and stars3[list_id[1]][fc.from_user.id] >= list_id[2]:
            stars3[list_id[1]][list_id[0]] += list_id[2]
            stars3[list_id[1]][fc.from_user.id] -= list_id[2]
            message = 'Подарок '+bot.get_chat_member(list_id[1], list_id[0]).user.first_name+':\n\nЦена: 🤩'+str(list_id[2])+'\nУ Вас: '+str(stars3[list_id[1]][fc.from_user.id])+'\nУ получателя: '+str(stars3[list_id[1]][list_id[0]])+'\n\nВы подарили подарок!'
            markup = types.InlineKeyboardMarkup()
            key = types.InlineKeyboardButton(text='Вернуться в магазин / подарки', callback_data=str(list_id[1]))
            markup.add(key)
            bot.edit_message_text(text=message, chat_id=fc.from_user.id, message_id=mess.id, reply_markup=markup)
    if data == 'Za':
        chat_id = ''
        for i in range(2, len(data2)):
            chat_id += data2[i]
        chat_id = int(chat_id)
        message = 'Чтобы взять займы:\n•Зайдите в чат того, у кого хотите взять займы\n•Напишите @gR6vjHdQ013bot\n•Далее напишите так: цена, username вашего собеседника, username группы\n•Нажмите на "готово"'
        markup = types.InlineKeyboardMarkup()
        key = types.InlineKeyboardButton(text='Вернуться в магазин / подарки', callback_data=str(chat_id))
        markup.add(key)
        bot.edit_message_text(text=message, chat_id=fc.from_user.id, message_id=mess.id, reply_markup=markup)
    try:
        int(fc.data)
        message = '👤'+fc.from_user.first_name
        if fc.from_user.last_name != None:
            message += ' '+fc.from_user.last_name
        message += '\n🤩Звёзды: '
        try:
            message += str(stars3[int(fc.data)][fc.from_user.id])
        except Exception as e:
            message += '0'
            print(e)
        message += '\n\n🎁Подарок\n🤝Займы\n👤Аватар'
        markup = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='🎁Подарок', callback_data='Podarok'+fc.data)
        key2 = types.InlineKeyboardButton(text='🤝Займы', callback_data='Za'+fc.data)
        markup.add(key1, key2)
        print(fc.from_user.id)
        bot.send_message(fc.from_user.id, message, parse_mode='html', reply_markup=markup)
    except:
        pass
    bot.answer_callback_query(fc.id)
    
bot.polling(none_stop=True)
