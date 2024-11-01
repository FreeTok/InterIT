import telebot
from telebot import types

import json

with open('webinars.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

token='7987637304:AAEOkZjAKri8t5cLH4eShIgjLWYMjEv5vUI'
bot=telebot.TeleBot(token)

kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn_types1 = types.KeyboardButton(text='Вебинары')
btn_types2 = types.KeyboardButton(text='Навигация')
kb.add(btn_types1, btn_types2)

kb1 = types.InlineKeyboardMarkup()
btn_types1 = types.InlineKeyboardButton(text='Рекрутмент', callback_data='btn_types_recrutment')
btn_types2 = types.InlineKeyboardButton(text='Новости hh.ru и советы по работе', callback_data='btn_types_news')
btn_types3 = types.InlineKeyboardButton(text='Развитие бренда работодателя', callback_data='btn_types_brand')
btn_types4 = types.InlineKeyboardButton(text='HR-бранчи Talantix', callback_data='btn_types_branch')
btn_types5 = types.InlineKeyboardButton(text='HR-аналитика и исследование рынка труда', callback_data='btn_types_analitic')
btn_types6 = types.InlineKeyboardButton(text='Для малого бизнеса', callback_data='btn_types_buissness')
kb1.add(btn_types1, btn_types2, btn_types3, btn_types4, btn_types5, btn_types6)

kb3 = types.InlineKeyboardMarkup()
btn_types1 = types.InlineKeyboardButton(text='❤️', callback_data='btn_types_yes')
btn_types2 = types.InlineKeyboardButton(text='❌', callback_data='btn_types_no')
kb3.add(btn_types1, btn_types2)

kb4 = types.InlineKeyboardMarkup(row_width=2)
btn_types1 = types.InlineKeyboardButton(text='Продвижение резюме', callback_data='btn_types_helpresume')
btn_types2 = types.InlineKeyboardButton(text='Готовое резюме', callback_data='btn_types_readyresume')
btn_types3 = types.InlineKeyboardButton(text='Рекомендации по резюме', callback_data='btn_types_recomendresume')
btn_types4 = types.InlineKeyboardButton(text='Сетка', callback_data='btn_types_setka')
kb4.add(btn_types1, btn_types2, btn_types3, btn_types4)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет, меня зовут Ежик Хантер, работник компании Head Hunter, отвечаю за образование. В нашей компании я помогаю развиваться людям. Ты же знаешь, что мы проводим лекции и вебинары?", reply_markup=kb)

@bot.message_handler()
def get_message(message):
    if message.json['text'] == 'Вебинары':
        bot.send_message(message.chat.id, 'Вебинары какого направления тебе больше интересны?', reply_markup=kb1)
    elif message.json['text'] == 'Навигация':
        bot.send_message(message.chat.id, 'Ты знал, что на нашем сайте помимо поиска работы, есть ещё', reply_markup=kb4)
        bot.send_message(message.chat.id, 'Что тебе больше интересно?')

@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'btn_types_it':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'Какой твой скилл?', reply_markup=kb2)

    elif call.data == 'btn_types_start':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'Отлично, я подобрал вебинары специально для тебя: ...')
    elif call.data == 'btn_types_mid':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'Отлично, я подобрал вебинары специально для тебя: ...')
    elif call.data == 'btn_types_hard':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'Отлично, я подобрал вебинары специально для тебя: ...')

    elif call.data == 'btn_types_helpresume':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.delete_message(call.message.chat.id, call.message.message_id + 1)
        bot.send_message(call.message.chat.id, 'Здесь тебе могут помочь с резюме')

        kb3 = types.InlineKeyboardMarkup()
        btn_types1 = types.InlineKeyboardButton(text='❤️', url='https://krasnogorsk.hh.ru/applicant/services/findjob?hhtmFrom=services&hhtmFromLabel=menu')
        btn_types2 = types.InlineKeyboardButton(text='❌', callback_data='btn_types_no_helpresume')
        kb3.add(btn_types1, btn_types2)

        bot.send_message(call.message.chat.id, 'Тебе интересно?', reply_markup=kb3)
    
    elif call.data == 'btn_types_readyresume':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.delete_message(call.message.chat.id, call.message.message_id + 1)
        bot.send_message(call.message.chat.id, 'Здесь тебе могут показать пример резюме')
        
        kb3 = types.InlineKeyboardMarkup()
        btn_types1 = types.InlineKeyboardButton(text='❤️', url='https://krasnogorsk.hh.ru/mentors?purposeId=1')
        btn_types2 = types.InlineKeyboardButton(text='❌', callback_data='btn_types_no_readyresume')
        kb3.add(btn_types1, btn_types2)

        bot.send_message(call.message.chat.id, 'Тебе интересно?', reply_markup=kb3)

    
    elif call.data == 'btn_types_recomendresume':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.delete_message(call.message.chat.id, call.message.message_id + 1)
        bot.send_message(call.message.chat.id, 'Здесь тебе могут порекомендовать резюме')

        kb3 = types.InlineKeyboardMarkup()
        btn_types1 = types.InlineKeyboardButton(text='❤️', url='https://krasnogorsk.hh.ru/article/resume_audit?hhtmFrom=services&hhtmFromLabel=menu')
        btn_types2 = types.InlineKeyboardButton(text='❌', callback_data='btn_types_no_recomendresume')
        kb3.add(btn_types1, btn_types2)

        bot.send_message(call.message.chat.id, 'Тебе интересно?', reply_markup=kb3)


    elif call.data == 'btn_types_setka':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.delete_message(call.message.chat.id, call.message.message_id + 1)
        bot.send_message(call.message.chat.id, 'Это Сетка')

        kb3 = types.InlineKeyboardMarkup()
        btn_types1 = types.InlineKeyboardButton(text='❤️', url='https://hi.setka.ru/?referrer=appmetrica_tracking_id%3D317055592281706223%26ym_tracking_id%3D925433669639828790')
        btn_types2 = types.InlineKeyboardButton(text='❌', callback_data='btn_types_no_setka')
        kb3.add(btn_types1, btn_types2)

        bot.send_message(call.message.chat.id, 'Тебе интересно?', reply_markup=kb3)

    elif 'btn_types_no' in call.data:
        bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'Ты знал, что на нашем сайте помимо поиска работы, есть ещё', reply_markup=kb4)
        bot.send_message(call.message.chat.id, 'Что тебе больше интерсно?')

    elif call.data == 'btn_types_recrutment' or call.data == 'btn_types_news' or call.data == 'btn_types_brand' or call.data == 'btn_types_branch' or call.data == 'btn_types_analitic' or call.data == 'btn_types_buissness':
        try:
            d = data[call.data.split('btn_types_')[1]]
            bot.send_message(call.message.chat.id, 'Вот вебинары по вашей теме:')
            for webinar in data[call.data.split('btn_types_')[1]]:
                print(call.data.split('btn_types_')[1], webinar)
                kb = types.InlineKeyboardMarkup()
                btn_types1 = types.InlineKeyboardButton(text='Подробнее', callback_data=f"btn_types_more_{call.data.split('btn_types_')[1]}_{webinar}")
                kb.add(btn_types1)
                js = data[call.data.split('btn_types_')[1]][webinar]
                text = f"***{js['name']}***\n{js['speaker']}\n{js['date']}"
                bot.send_message(call.message.chat.id, text, reply_markup=kb, parse_mode='markdown')
        except:
            bot.send_message(call.message.chat.id, 'Пока что вебинары не запланированы. Следите за анонсами!')
    elif 'btn_types_more_' in call.data:
        a = call.data.split('btn_types_more_')[1].split('_')
        print(data[a[0]][a[1]])
        bot.send_message(call.message.chat.id, f'{data[a[0]][a[1]]['about']}')


if __name__ == '__main__':
    bot.polling(none_stop=True)