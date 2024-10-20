import requests
from send_mails import send_mail
from datetime import date

topic = 'tesla'
# credentials
api_key = '4d96f699b9c84f539c19d87b03bb5498'
url2 = (f"https://newsapi.org/v2/everything?"
        f"q={topic}&"
        f"from=2024-09-20&"
        f"sortBy=publishedAt&"
        f"apiKey=4d96f699b9c84f539c19d87b03bb5498&"
        f"language=en")

# Make the request
req = requests.get(url2)

# Get the dictionary with data
#content = req.text gives the sting back
content = req.json()
message =f'''\
Subject:News of {date.today()}
'''''

# Access the articles title and description
for article in content['articles'][:20]:
    if article['title'] is not None:
        raw_message = (f"{article['title']}\n{article['description']}."
                       f"\n{article['url']}" + 2*"\n")
        message = message + f'{raw_message}'

message = message.encode('utf-8')
send_mail(message=message)