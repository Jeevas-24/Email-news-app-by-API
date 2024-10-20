import requests

url = 'https://cdn.pixabay.com/photo/2024/04/03/18/07/fish-8673535_640.jpg'
req = requests.get(url)
#print(req.text)
#print(req.content)

with open('image.jpg', 'wb') as file:
    file.write(req.content)
