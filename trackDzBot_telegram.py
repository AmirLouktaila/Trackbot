import telebot
import requests

Mytext='''
    ✅ ما تريد معرفته

    1️⃣ الخدمة مجانية وغير محدودة!

    2️⃣ اكتب كود تتبع فقط

    4️⃣ هناك 200 دولة مدعومة
    '''
bot = telebot.TeleBot("<Yor token>")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, Mytext)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	
    r=requests.get(f'https://global.cainiao.com/global/getCity.json?mailNo={message.text}&lang=en-US&language=en-US')
    r_json=r.json()
    re=requests.get(f'https://global.cainiao.com/global/detail.json?mailNos={message.text}&lang=en-US&language=en-US')
    r_j=re.json()
    track_mailNo=r_j.get('module')[0].get('mailNo')
    track_originCountry=r_j.get('module')[0].get('originCountry')
    track_destCountry=r_j.get('module')[0].get('destCountry')
    MYINFO="✅ Tracking on : "+track_mailNo+"\n"+"✅ From :"+str(track_originCountry)+"\n"+"✅ To :"+str(track_destCountry)+"\n"+"✅ in :"+r_json.get('module')

    if track_originCountry==None:
          
        bot.send_message(message.chat.id,"يوجد خطأ تأكد من رقم التتبع")
    else:
        bot.send_message(message.chat.id,MYINFO)




bot.infinity_polling()
