import urllib3, json

cities = ['Nairobi', 'London', 'Lagos', 'Tehran', 'New Delhi', 'Tokyo']

def get_weather_info(city):
    api_key = 'f5f6ee17ea565e914cfeaa6f8ac6eda4'
    endpoint = 'http://api.openweathermap.org/data/2.5/weather'
    fields = {'q': city, 'units':'metrics', 'APPID': api_key }
    http = urllib3.PoolManager()
    r = http.request('GET', endpoint, fields)
    ans = json.loads(r.data.decode('utf-8'))
    return ans

print("CITY\t\tTEMP\t\tDESCRIPTION\n")
line_under = "="
line_under *= 50
print(line_under)
for city in cities:
    output = get_weather_info(city)
    print(city + '\t\t' + output['weather'][0]['description'] + '\t\t' + str(output['main']['temp']) + 'F')




