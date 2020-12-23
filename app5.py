import collections
import requests
import json

Location = collections.namedtuple('Location', 'City State Country')
Weather = collections.namedtuple('Weather', 'location temp wind condition')

def print_header():
    print('-------------------')
    print('   Weather App')
    print('-------------------')
    print()


def convert_plaintext_to_location(text):
    if not text or not text.strip():
        return None
    location_text = text.strip().lower()
    parts = location_text.split(',')
    city = ''
    state = ''
    country = 'us'
    if len(parts) == 1:
        city = parts[0].strip()
    elif len(parts) == 2:
        city = parts[0].strip()
        country = parts[1].strip()
    elif len(parts) == 3:
        city = parts[0].strip()
        state = parts[1].strip()
        country = parts[2].strip()

    return Location(City=city, State=state, Country=country)


def get_weather(loc: Location):
    url = "https://weather.talkpython.fm/api/weather?city={}&country={}".format(loc.City, loc.Country)
    if loc.State:
        url += '&state={}'.format(loc.State)

    resp = requests.get(url)
    if resp.status_code in {400, 404, 500}:
        print("Error getting result")
        return None
    data = resp.json()
    return(get_weather_from_api(data, loc))


def get_weather_from_api(data, loc):
    t = data.get('forecast').get('temp')
    c = data.get('weather').get('description')
    w = data.get('wind').get('speed')
    weather = Weather(location=loc, temp=t, condition=c, wind=w)
    return weather


def main():
    print_header()
    location_text = input('Where do you want the weather report in format city, state, country (e.g Amersfroot, Utrecht, NL)?')
    print('You selected {}'.format(location_text))
    loc = convert_plaintext_to_location(location_text)
    weather = get_weather(loc)
    # weather_dict = json.loads(weather)
    print("In {}, The Condition: {}, Temp: {}, Wind: {}".format(weather.location, weather.condition, weather.temp, weather.wind))




if __name__ == '__main__':
    main()
