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

kb1 = types.InlineKeyboardMarkup(row_width=1)
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

kb4 = types.InlineKeyboardMarkup(row_width=1)
btn_types1 = types.InlineKeyboardButton(text='Продвижение резюме', callback_data='btn_types_helpresume')
btn_types2 = types.InlineKeyboardButton(text='Карьерный маркетплейс', callback_data='btn_types_readyresume')
btn_types3 = types.InlineKeyboardButton(text='Карьерный консультант', callback_data='btn_types_recomendresume')
btn_types4 = types.InlineKeyboardButton(text='Сетка', callback_data='btn_types_setka')
kb4.add(btn_types1, btn_types2, btn_types3, btn_types4)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет, меня зовут ёжик Хантер, работник компании Head Hunter, отвечаю за образование. В нашей компании я помогаю развиваться людям. Чем я могу помочь?", reply_markup=kb)

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
        bot.send_message(call.message.chat.id, parse_mode='markdown', text='***Продвижение резюме для быстрого поиска работы***\n\n***Автоподнятие резюме*** — резюме автоматически обновляется 5 раз в день, поднимаясь в верхние позиции для лучшей видимости работодателям.\n***Яркое выделение резюме*** — резюме становится заметнее в поисковой выдаче, привлекая больше внимания.\n***Статистика по вакансиям*** — доступ к данным по откликам на вакансии, включая зарплатные ожидания, навыки и опыт конкурентов.\n\nДополнительные сервисы:\n***Готовое резюме*** — профессиональная помощь в создании резюме для улучшения шансов на трудоустройство.\n***Профориентация*** — онлайн-тест для подбора подходящей профессиональной сферы.\n***Репетиция собеседования*** — тренировка для уверенного прохождения интервью.')

        kb3 = types.InlineKeyboardMarkup()
        btn_types1 = types.InlineKeyboardButton(text='❤️', url='https://hh.ru/applicant/services/findjob')
        btn_types2 = types.InlineKeyboardButton(text='❌', callback_data='btn_types_no_helpresume')
        kb3.add(btn_types1, btn_types2)

        bot.send_message(call.message.chat.id, 'Тебе интересно?', reply_markup=kb3)
    
    elif call.data == 'btn_types_readyresume':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.delete_message(call.message.chat.id, call.message.message_id + 1)
        bot.send_message(call.message.chat.id, parse_mode='markdown' ,text='***Карьерный маркетплейс***\n\nЗадачи, которые данный сервис может помочь решить:\nСоздать резюме, составить карьерный план\nРазработать стратегию поиска работы\nПерейти в новую профессию или найти работу за границей\nПодготовиться к собеседованию\nПреодолеть синдром самозванца или справиться с выгоранием\n\nКарьерный наставник поможет:\nОпределить карьерные цели и пути их достижения\nСоставить резюме, стратегию поиска и подготовки к собеседованиям\nНайти подходящую профессию или сменить сферу деятельности\nПреодолеть профессиональные трудности\n\nРезультаты:\n100 000+ успешных консультаций\n86% клиентов достигли карьерных целей')
        
        kb3 = types.InlineKeyboardMarkup()
        btn_types1 = types.InlineKeyboardButton(text='❤️', url='https://hh.ru/mentors')
        btn_types2 = types.InlineKeyboardButton(text='❌', callback_data='btn_types_no_readyresume')
        kb3.add(btn_types1, btn_types2)

        bot.send_message(call.message.chat.id, 'Тебе интересно?', reply_markup=kb3)

    
    elif call.data == 'btn_types_recomendresume':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.delete_message(call.message.chat.id, call.message.message_id + 1)
        bot.send_message(call.message.chat.id, 'Карьерный консультант hh.ru поможет улучшить ваше резюме для быстрого поиска работы. За 3 дня вы получите экспертные рекомендации по усилению ключевых разделов, привлечению внимания работодателей и упаковке опыта для нужной сферы, даже с минимальным стажем.')

        kb3 = types.InlineKeyboardMarkup()
        btn_types1 = types.InlineKeyboardButton(text='❤️', url='https://hh.ru/article/resume_audit')
        btn_types2 = types.InlineKeyboardButton(text='❌', callback_data='btn_types_no_recomendresume')
        kb3.add(btn_types1, btn_types2)

        bot.send_message(call.message.chat.id, 'Тебе интересно?', reply_markup=kb3)


    elif call.data == 'btn_types_setka':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.delete_message(call.message.chat.id, call.message.message_id + 1)
        bot.send_message(call.message.chat.id, parse_mode='markdown', text='***Сетка*** — профессиональная соцсеть от hh.ru для обмена опытом, нетворкинга и карьерного роста. Она объединяет экспертов в сфере tech, digital и creative, помогая найти новых коллег, партнёров для проектов и быть в курсе трендов.\n\n***Ключевые преимущества***:\n- Быстрый вход в комьюнити специалистов.\n- Удобный поиск профессиональных контактов.\n- Возможность повышать видимость в сообществе.\n- Контент по интересам благодаря алгоритмам.\n\nПрисоединяйтесь к Сетке и расширяйте свои карьерные возможности!')

        kb3 = types.InlineKeyboardMarkup()
        btn_types1 = types.InlineKeyboardButton(text='❤️', url='https://hi.setka.ru')
        btn_types2 = types.InlineKeyboardButton(text='❌', callback_data='btn_types_no_setka')
        kb3.add(btn_types1, btn_types2)

        bot.send_message(call.message.chat.id, parse_mode='markdown', text='Тебе интересно?', reply_markup=kb3)

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

        kb = types.InlineKeyboardMarkup()
        btn_types1 = types.InlineKeyboardButton(text='Перейти на сайт', url=data[a[0]][a[1]]['url'])
        kb.add(btn_types1)

        bot.send_message(call.message.chat.id, f"{data[a[0]][a[1]]['about']}", reply_markup=kb)

if __name__ == '__main__':
    bot.polling(none_stop=True)