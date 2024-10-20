import requests
from send_mails import send_mail
from datetime import date

api_key = '4d96f699b9c84f539c19d87b03bb5498'
url2 = 'https://newsapi.org/v2/everything?q=tesla&from=2024-09-20&sortBy=publishedAt&apiKey=4d96f699b9c84f539c19d87b03bb5498'

# Make the request
req = requests.get(url2)

# Get the dictionary with data
#content = req.text gives the sting back
content = req.json()
message =f'''\
Subject:News of {date.today()}
'''''
# Access the articles title and description
for article in content['articles']:
    if article['title'] is not None:
        raw_message = f'{article['title']}\n{article['description']}.'
        message = message + f'{raw_message}' + 2*'\n'

message = message.encode('utf-8')
send_mail(message=message)