import telepot
import common, time
from telepot.loop import MessageLoop

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        if "/cronograma" in msg['text'] :
            bot.sendMessage(chat_id, common.mensagem['cronograma'])

        elif "/livrodomes" in msg['text'].lower() :
            bot.sendPhoto(chat_id, common.mensagem['foto'])
            bot.sendMessage(chat_id, f"Essa é a leitura do mês, acompanhe nosso cronograma.\n{common.mensagem['cronograma']}")
            
        print(msg)
        
    elif content_type == 'new_chat_member' :
        bot.sendMessage(chat_id, f"🦉 Uuh uuh {msg['new_chat_participant']['first_name']}, {common.mensagem['bem-vindo']} 🦉")
    elif content_type == 'left_chat_member' :
        bot.sendMessage(chat_id, f"🦉 Uuh uuh {msg['left_chat_participant']['first_name']} deixou o grupo :(")


bot = telepot.Bot(common.token)
print (bot.getMe())
print (bot.getUpdates())

MessageLoop(bot, handle).run_as_thread()

def send_welcome(message):
    bot.reply_to(message, u"Olá, bem-vindo ao bot!")


while 1:
    time.sleep(10)