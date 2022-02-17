import telebot
import config
import shutil
token = 'ТОКЕН БОТА'
from telebot import types
import corect
import create

def sendM(text, id):
    bot.send_message(id, text)
def getCfg(name):
    return config.get("data/" + name + ".json")
def sendEND(user, id):
    sendM("Вот твоя Дія(клон): http://(ВАШ САЙТ)" + create.create(user, photo[id]), id)
    config.set("data/" + user + ".json", "end", "true")
data = {}
photo = {}
bot = telebot.TeleBot(token)

#download pass
@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    if (not (message.chat.username == None)):
        #
        if("end" not in getCfg(message.chat.username)):
            if("type" in getCfg(message.chat.username)):
                #
                try:
                    file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
                    downloaded_file = bot.download_file(file_info.file_path)
                    src='screenshot/' + str(message.chat.id) + '.jpg';
                    with open(src, 'wb') as new_file:
                        new_file.write(downloaded_file)
                        bot.reply_to(message,"Та ти шо какой пирожочек 🤤🤖")
                except Exception as e:
                    bot.reply_to(message, e)
                #cfg = getCfg(message.chat.username)
                if(getCfg(message.chat.username)['type'] == 'diya'):
                    if(getCfg(message.chat.username)['type1'] == 'pasport'):
                        photo[message.chat.id] = corect.photo(str(message.chat.id) + ".jpg", 'pasport')
                    # print(photo(message.chat.id))
                        sendM("Вот как-то так получилось:", message.chat.id)
                        bot.send_photo(message.chat.id, photo = open('done/' + photo[message.chat.id], 'rb'))
                    else:
                        photo[message.chat.id] = corect.photo(str(message.chat.id) + ".jpg", 'student')
                        sendM("Вот как-то так получилось ))", message.chat.id)
                        bot.send_photo(message.chat.id, photo=open('done/' + photo[message.chat.id], 'rb'))
                    markup_inline = types.InlineKeyboardMarkup()
                    markup_inline.add(types.InlineKeyboardButton(text='Все ок', callback_data='end_true'), types.InlineKeyboardButton(text='Свое фото', callback_data='end_false'))
                    bot.send_message(message.chat.id, "Решение с фото", reply_markup=markup_inline)
                else:
                    photo[message.chat.id] = corect.photo(str(message.chat.id) + ".jpg", 0, 1)
                    shutil.copy("screenshot/" + photo[message.chat.id], "done/")
                    sendM("Секунду ...", message.chat.id)
                    sendEND(message.chat.username, message.chat.id)

        else:
            sendM("Больше возможностей нету :) \nПри проблемах писать сюда: https://cyberpolice.gov.ua/", message.chat.id)
    else:
        sendM("Для использования бота у тебя в профеле должен бить указан 'UserName' \nПри проблемах писать сюда: https://cyberpolice.gov.ua/", message.chat.id)


#command
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет пупсик 😅! \nМеня зовут 'Гкод' \nМой создатель: https://cyberpolice.gov.ua/ 😇")
  markup_inline = types.InlineKeyboardMarkup()
  markup_inline.add(types.InlineKeyboardButton(text='GO', callback_data='one_go'))
  bot.send_message(message.chat.id, "Эсли тебе нету 18, то я помогу тебе купить твой запретний товар 😼\nДля породолжения нажми книпу 'GO'", reply_markup=markup_inline)
#chat_button
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    m = call.message.chat
    if(not(m.username == None)):
        cfg = getCfg(m.username)
        if ("end" not in getCfg(m.username)):
            if("DR" not in cfg):
                #First
                if call.data == 'one_go':
                    # bot.send_message(call.message.chat.id, 'Ваш выбор - Принять')
                    bot.edit_message_text("Ну погнали", m.id, call.message.message_id)
                    bot.send_message(m.id, "Начнем с простого\nКак тебя зовут ?")
                if call.data == 'one_name':
                    config.set("data/"+ m.username + ".json", "Имя", data[m.id])
                    bot.edit_message_text("Твоя фамилия? ", m.id, call.message.message_id)
                if call.data == 'two_name':
                    config.set("data/"+ m.username + ".json", "Фамилия", data[m.id])
                    bot.edit_message_text("Как тебя по отцу? ", m.id, call.message.message_id)
                if call.data == 'fri_name':
                    config.set("data/"+ m.username + ".json", "Отчество", data[m.id])
                    bot.edit_message_text("Отлично!\nТеперь введи дату рождения\n В форматe (дд.мм.рр/03.02.2004)", m.id, call.message.message_id)
                if call.data == 'date':
                    config.set("data/" + m.username + ".json", "DR", data[m.id])
                    bot.edit_message_text("Отлично!\nТеперь вибери способ загрузки фото", m.id, call.message.message_id)
                    #keyboard
                    markup_inline = types.InlineKeyboardMarkup()
                    markup_inline.add(types.InlineKeyboardButton(text='Скрин с ДіЯ', callback_data='type_diya'), types.InlineKeyboardButton(text='Своє фото', callback_data='type_my'))
                    bot.send_message(m.id, "Скрін з Дії автоматично виріже фото (BETA)",reply_markup=markup_inline)

            else:
                if call.data == 'type_diya':
                    bot.edit_message_text("😎", m.id, call.message.message_id)
                    markup_inline = types.InlineKeyboardMarkup()
                    markup_inline.add(types.InlineKeyboardButton(text='Паспорт', callback_data='pasport'), types.InlineKeyboardButton(text='Студенчиский', callback_data='student'))
                    bot.send_message(m.id, "Какой скрин возьмем?🙃", reply_markup=markup_inline)
                    config.set("data/" + m.username + ".json", "type", 'diya')

                if call.data == 'type_my':
                    bot.edit_message_text("Жду готове фото 😴", m.id, call.message.message_id)
                    config.set("data/" + m.username + ".json", "type", 'done')

                if call.data == 'pasport':
                    bot.edit_message_text("Жду скрин ДІЇ з паспортом (Можно замазать лишні цифри): ", m.id, call.message.message_id)
                    config.set("data/" + m.username + ".json", "type1", 'pasport')
                if call.data == 'student':
                    bot.edit_message_text("Жду скрин ДІЇ з студенчиским (Можно замазать лишні цифри): ", m.id, call.message.message_id)
                    config.set("data/" + m.username + ".json", "type1", 'student')
                if call.data == 'end_true':
                    bot.edit_message_text("Юхху", m.id, call.message.message_id)
                    sendEND(m.username, m.id)
                if call.data == 'end_false':
                    bot.edit_message_text("Жду готове фото 😴", m.id, call.message.message_id)
                    config.rem("data/" + m.username + ".json", "type1")
                    config.rem("data/" + m.username + ".json", "type")
                    config.set("data/" + m.username + ".json", "type", 'done')               
        else:
            sendM("Больше возможностей нету :) \nПри проблемах писать сюда: https://cyberpolice.gov.ua/", m.id)
    else:
        sendM("Для использования бота у тебя в профеле должен бить указан 'UserName' \nПри проблемах писать сюда: https://cyberpolice.gov.ua/", m.id)
@bot.message_handler(content_types='text')
def go(message):
    id = message.chat.id
    if (not (message.chat.username == None)):
        #
        #text = message.text.lower()
        cfg = getCfg(message.chat.username)
        if("Имя" not in cfg):
            #
            markup_inline = types.InlineKeyboardMarkup()
            markup_inline.add(types.InlineKeyboardButton(text='Да', callback_data='one_name'))
            bot.send_message(message.chat.id, "Тебя зовут (" + message.text + ")\n Верно ?\nЭли не верно отправ повторно свое имя)", reply_markup=markup_inline)
            data[id] = message.text
        if("Фамилия" not in cfg and "Имя" in cfg):
            #
            markup_inline = types.InlineKeyboardMarkup()
            markup_inline.add(types.InlineKeyboardButton(text='Да', callback_data='two_name'))
            bot.send_message(message.chat.id, "Твоя фамилия (" + message.text + ")\n Верно ?\nЭли не верно отправ повторно свою фамилию)", reply_markup=markup_inline)
            data[id] = message.text
        if ("Отчество" not in cfg and "Фамилия" in cfg):
            #
            markup_inline = types.InlineKeyboardMarkup()
            markup_inline.add(types.InlineKeyboardButton(text='Да', callback_data='fri_name'))
            bot.send_message(message.chat.id, "Тебя по отцу (" + message.text + ")\n Верно ?\nЭли не верно отправ повторно)", reply_markup=markup_inline)
            data[id] = message.text
        if("DR" not in cfg and "Отчество" in cfg):
            markup_inline = types.InlineKeyboardMarkup()
            markup_inline.add(types.InlineKeyboardButton(text='Да', callback_data='date'))
            bot.send_message(message.chat.id, "Ти хотел родится (" + message.text + ")\n Верно ?\nЭли не верно отправ повторно)", reply_markup=markup_inline)
            data[id] = message.text
        if("DR" in cfg):
            sendM("Больше возможностей нету :) \nПри проблемах писать сюда: https://cyberpolice.gov.ua/", id)
    else:
        sendM("Для использования бота у тебя в профеле должен бить указан 'UserName' \nПри проблемах писать сюда: https://cyberpolice.gov.ua/", id)


#Start bot
if __name__ == '__main__':
    print("!> Start")
    bot.polling(none_stop=True)
