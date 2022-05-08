
from distutils.log import error
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from response import respon
from model import clean_text


#pembuka
def start(update: Update, context: CallbackContext):
    #chat_id agar bot tidak reply user input
    # chat_id = update.effective_chat.id
    # context.bot.send_message(chat_id=chat_id, 
    # text=
    #     '''
    #     Halo, saya nama_bot . Ada yang bisa dibantu?
    #     \n\nKetikkan /help untuk bantuan terkait bot
    #     ''')
    update.message.reply_text('Halo, saya nama_bot. Ada yang bisa dibantu?')

#/help
def help(update: Update, context: CallbackContext):
    update.message.reply_text("Hubungi developer untuk bantuan lebih lanjut pada https://github.com/Riezn/.")

#error
def error(update: Update, context: CallbackContext):
    # update.message.reply_text(
    #     "Maaf, Kak. Aku tidak mengerti perintah '%s'." % update.message.text)
    print(f"update{update} caused error {context.error}")

#handle message
def handle_message(update: Update, context: CallbackContext):
    text = str(update.message.text).lower()
    text = clean_text(text)
    resp = respon(text)
    update.message.reply_text(resp)

#end to end
def main():
    #token dari botfather
    token_app = '5327133782:AAGj5NVVR_wJu4gqFzu5A8A8Lgi_-pvJObc'

#koneksiin ke bot telegram
    updater = Updater(token_app,
                  use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text,handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()