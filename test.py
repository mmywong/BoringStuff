import requests
res = requests.get('https://www.google.com/search?q=dog')

saveFile = open('dog.txt', 'w')

saveFile.write(res.text)

saveFile.close()
