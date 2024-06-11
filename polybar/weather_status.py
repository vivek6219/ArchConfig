import requests

#variables
api_key = "49a634e427d2382d7809e3527e3bffba"
byCity = "san jose"
byZip = 95148

url = f"https://api.openweathermap.org/data/2.5/weather?q={byZip}&appid={api_key}&units=imperial"
#url = "https://api.openweathermap.org/data/2.5/weather?q=95148&appid=49a634e427d2382d7809e3527e3bffba&units=imperial"
response = requests.get(url)

if response.status_code == 200:
    
    print(response)
    data = response.json()
     
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    weather = data['weather'][0]['description']
    city = data['name']
    country = data['sys']['country']

    weather_info = f"""
    Weather in {city}, {country}:
    ---------------------------------
    Temperature      : {temp}°F
    Feels Like       : {feels_like}°F
    Minimum Temp     : {temp_min}°F
    Maximum Temp     : {temp_max}°F
    Description      : {weather.capitalize()}
    """

    print(weather_info)

else:
    print(f'Error fetching weather data: {response.status_code}')
