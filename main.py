from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler

TOKEN = "5495345535:AAE6uAEJoYJbYFOOLi4LgYvmERjubhwxlEA"
def echo(update, conext):
    txt = update.message.text

    n = txt
    if txt.lower() in ['коооляяя', 'коля']:
        txt = "фто???)))"
    if txt.lower() in ['любишь чокопай?', 'любишь чокопай', 'хочешь чокопай?', 'хочешь чокопай']:
        txt = "да"
    if txt.lower() in ['с говном?', 'с говном']:
        txt = "на колени!!!"
    if txt.lower() in ['че смотришь', 'чё смотришь', 'че палишь?', 'чё палишь?', 'че палишь', 'чё палишь', 'че смотришь?', 'чё смотришь?']:
        txt = "хочу и смотрю!!!"
    if txt.lower() in ['ты кому', 'ты кому?']:
        txt = "тебе!!!"
    if txt.lower() in ['сосал', 'сосёшь', 'сосешь']:
        txt = ")))"
    if txt == n:
        txt = "хммм"
    print(txt)
    update.message.reply_text(txt)

def start(update, conext):
    update.message.reply_text("фто?")


def main():
    updater = Updater(TOKEN,use_context=True)
    dp = updater.dispatcher
    print("а мы стартуем")

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, echo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()