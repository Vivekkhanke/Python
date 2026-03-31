import requests

url = "https://api.openweathermap.org/data/2.5/weather?q=Mumbai&appid=123456"
data = requests.get(url)

res = data.json()
print(res)