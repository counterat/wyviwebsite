import requests
from config import token


TOKEN = token
def send_message_to_admins(text, adress):


    chat_id = 'идентификатор_чата'
    text = text

    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data = {'chat_id': '801856613', 'text': text}
    

    response = requests.post(url, data=data)
    print(response.json())