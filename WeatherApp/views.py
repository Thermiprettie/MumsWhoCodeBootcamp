from django.shortcuts import render

# Create your views here.
import json  # import json to load json data to python dictionary
import urllib.request  # urllib.request to make a request to api

def index(request):
    if request.method == 'POST':
        city = request.POST.get('city', True)

        # source contain JSON data from API
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + 
                                        city + '&units=metric&appid=7b245577692ef04c44b8088b8ebd790d').read()

        # converting JSON data to a dictionary
        list_of_data = json.loads(source)

        # data for variable list_of_data
        data = {
            'city': city,
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + '°C',
            "pressure": str(list_of_data['main']['pressure']) + 'hPa',
            "humidity": str(list_of_data['main']['humidity']) + '%',
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data ={}#empty dictionary. i.e. to return nothing
        
    # send dictionary to the home.html
    return render(request, "index.html", data)
