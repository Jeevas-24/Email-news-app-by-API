import requests

api_key = '4d96f699b9c84f539c19d87b03bb5498'
url2 = 'https://newsapi.org/v2/everything?q=tesla&from=2024-09-20&sortBy=publishedAt&apiKey=4d96f699b9c84f539c19d87b03bb5498'

# Make the request
req = requests.get(url2)

# Get the dictionary with data
# content = req.text gives the sting back
content = req.json()

# Access the articles title and description
for article in content['articles']:
    print(article['title'])
    print(article['description'])