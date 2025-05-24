import telebot
from config import TOKEN, formatted_dict
from extensions import APIException, CurrancyConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.reply_to(message, 'Привет я помогу посчитать тебе валюту исходя из актуального курса. \n\n \
*Отправь сообщение типа: <имя валюты, цену которой хочешь узнать><пробел>\
<имя валюты, в которой надо узнать цену первой валюты><пробел><количество первой валюты>\n\n\
Список доступных валют: /values')

@bot.message_handler(commands=['values'])
def print_list_command(message):
    bot.reply_to(message, f'Доступные валюты:\n\n{formatted_dict}')

@bot.message_handler(content_types=['text'])
def currency_convert(message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise APIException('Неверно введены параметры.')
        base, quote, amount = values
        result_amount = CurrancyConverter.get_price(base, quote, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя:\n\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Ошибка сервера:\n\n{e}')
    else:
        text = f'Цена {amount} {base} в {quote} равна: {result_amount:.2f}'
        bot.send_message(message.chat.id, text)

bot.infinity_polling()



