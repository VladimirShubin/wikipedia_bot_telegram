import telebot
import wikipedia

wikipedia.set_lang('de')
bot = telebot.TeleBot('5693898055:AAHEh3afLNYNciP5MPe6CTeoh5CBzcNHatg')
def main():
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.send_message(message.chat.id, 'Geben Sie bitte etwas ein!')

    @bot.message_handler(content_types=['text'])
    def input(message):
        def text(page):
            try:
                message = wikipedia.summary(page, sentences=3)
                return message
            except Exception as e:
                return 'Ich weiß das leider noch nicht :('

        bot.send_message(message.chat.id, text(message.text))
        bot.send_message(message.chat.id, 'Was möchten Sie noch wissen?')


if __name__ == '__main__':
    main()
bot.infinity_polling()

