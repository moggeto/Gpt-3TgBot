import os
import telebot
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
bot = telebot.TeleBot('5896976499:AAEX8j7zE_Jta8YZzzuPKeUQCwDcvrzkCrk')


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am Chat-gpt-3 bot.
Type me any questions\
""")

@bot.message_handler(func=lambda _: True)
def handle_message(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,

    )

    bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])
    with open('log.txt', 'a') as w:
        w.write(f'Вопрос -\n\n{message.text}\n\n'
                f"Ответ - {response['choices'][0]['text']}")

bot.polling()



