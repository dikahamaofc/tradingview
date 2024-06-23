import requests

TELEGRAM_TOKEN = '6996949870:AAF3oMQtk9BbYJpeeTCxDAA0kovF5lTJNMI'
TELEGRAM_CHAT_ID = '-1002216540134'

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    response = requests.post(url, data=payload)
    return response.json()

if __name__ == '__main__':
    message = "Signal from TradingView!"
    send_telegram_message(message)
