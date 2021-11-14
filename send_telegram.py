import requests

def send_message(title, body):
    url = 'https://api.telegram.org/bot2133332644:AAGXWbjIr33p9P-_WE4gSYB9Iq_ZjK3HBZU/sendMessage'



    myobj = {'chat_id': '@airdropdiggersangin',
             'text': title + '\n' + body,
             'disable_notification': False}

    x = requests.post(url, data = myobj)

    print(x.text)