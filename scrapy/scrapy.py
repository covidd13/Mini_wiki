import requests

url="https://www.reddit.com/r/MachineLearning/new/"
data=requests.get(url)
print(data.text)