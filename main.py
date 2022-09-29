import telebot
from telebot import types

bot = telebot.TeleBot('5788182596:AAHkivLbZx8r5guunucQ7POUpcI_LpoPBW0')


@bot.message_handler(commands=['instagram'])
def instagram(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Перейти в Инстаграм", url="https://instagram.com/anninails_minsk?igshid=YmMyMTA2M2Y="))
	bot.send_message(message.chat.id, "Нажмите на кнопку ниже,чтобы посмотреть работу мастера", parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start_message(message):
    app_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    app_keyboard = types.KeyboardButton(text="💬 Написать мне")
    app_keyboard2 = types.KeyboardButton(text="💅 Мои работы")
    app_keyboard3 = types.KeyboardButton(text="💵 Прайс на услугу")
    app_keyboard4 = types.KeyboardButton(text="📞 Контакты")
    back = types.KeyboardButton('⬅️ Назад')
    app_markup.add(app_keyboard, app_keyboard2, app_keyboard3, app_keyboard4, back)
    chat_id = message.chat.id
    first_name = message.chat.first_name
    bot.send_message(chat_id, f"Привет {first_name} !\n"
                              f"Здесь вы можите отправить заявку и администратор с вами свяжется !", reply_markup=app_markup)


@bot.message_handler(content_types=["text"])
def text(message):
        chat_id =message.chat.id
        if message.chat.type == 'private':
            if message.text == '💬 Написать мне':
                bot.send_message(chat_id, "Пришлите что хотите отправить :")
                bot.register_next_step_handler(message, send_z)
        if message.text =='💵 Прайс на услугу':
            app_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            app_keyboard1 = types.KeyboardButton(text="Маникюр + гель-лак - 30р.")
            app_keyboard2 = types.KeyboardButton(text="Маникюр + френч - 35р.")
            app_keyboard3 = types.KeyboardButton(text="Наращивание- 40р.")
            app_keyboard4 = types.KeyboardButton(text="Маникюр без покрытия-20р.")
            back = types.KeyboardButton('⬅️ Назад')
            app_markup.add(app_keyboard1, app_keyboard2, app_keyboard3, app_keyboard4, back)
            bot.send_message(message.chat.id, '💵 Прайс на услугу', reply_markup=app_markup)


        if message.text == "📞 Контакты":
            app_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            app_keyboard1 = types.KeyboardButton(text="🙍🏻‍ Anni 📞+375(33)3578350)")
            app_keyboard2 = types.KeyboardButton(text="Инстаграм:👉👉👉 , https://instagram.com/anninails_minsk?igshid=YmMyMTA2M2Y=")
            app_keyboard3 = types.KeyboardButton(text="Viber 📞+375(33)3578350)")
            back = types.KeyboardButton('⬅️ Назад')
            app_markup.add(app_keyboard1, app_keyboard2, app_keyboard3, back)

            bot.send_message(message.chat.id, "📞 Контакты", reply_markup=app_markup)


        if message.text == '⬅️ Назад':
            app_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            app_keyboard = types.KeyboardButton(text="💬 Написать мне")
            app_keyboard2 = types.KeyboardButton(text="💅 Мои работы")
            app_keyboard3 = types.KeyboardButton(text="💵 Прайс на услугу")
            app_keyboard4 = types.KeyboardButton(text="📞 Контакты")
            back = types.KeyboardButton('⬅️ Назад')
            app_markup.add(app_keyboard, app_keyboard2, app_keyboard3, app_keyboard4, back)

            bot.send_message(message.chat.id, '⬅️ Назад', reply_markup=app_markup)


        if message.text == '💅 Мои работы':
            app_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            app_keyboard = types.KeyboardButton(text="Инстаграм:👉👉👉 , https://instagram.com/anninails_minsk?igshid=YmMyMTA2M2Y=")
            back = types.KeyboardButton('⬅️ Назад')
            app_markup.add(app_keyboard, back)

            bot.send_message(message.chat.id, '💅 Мои работы', reply_markup=app_markup)


def send_z(message):
    first_name = message.chat.first_name
    chat_id = message.chat.id
    user_name = message.chat.username
    z = message.text
    admin_id = 1691974670
    app_text = []
    app_name = []
    app_username = []
    app_name.append(first_name)
    app_username.append(user_name)
    app_text.append(z)
    bot.send_message(admin_id, f"Поступила заявка от {app_name[0]} !\n"
                               f"Его username = @{app_username[0]}\n"
                               f"Его текст :\n"
                               f"{app_text[0]}")

    app_name.clear()
    app_username.clear()
    app_text.clear()
    bot.send_message(chat_id, "Заявка отправлена !")


bot.polling(none_stop=True)


