import requests


api_key = "Push_your_API_key "
city = input("City: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

r = requests.get(url)
data = r.json()
print(f"City:{data['city']}")
print(f"Temperature:{data['main']['temp']}°C")
print(f"Feels Like:{data['main']['feels_like']}°C")
print(f"Humidity:{data['main']['humidity']}%")
print(f"Wind Speed:{data['wind']['speed']} km/h")
print(f"Condition:{data['weather'][0]['description']}")


