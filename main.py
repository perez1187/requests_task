import requests
import json
# https://www.youtube.com/watch?v=tb8gHvYlCFs - tutorial request
# https://httpbin.org/ - he created this library
# beautiful soup https://www.youtube.com/watch?v=ng2o98k983k
# reading and writing files https://www.youtube.com/watch?v=Uh2ebFW8OYM
# r = requests.get('https://xkcd.com/353/')
def download_page():
    r = requests.get('https://imgs.xkcd.com/comics/python.png')
    with open('comic.png', 'wb') as f:
        f.write(r.content)
def testing_get():
    payload = {'page':2, 'count': 25}
    r = requests.get('https://httpbin.org/get', params=payload) #kiedy zamiast get post, wtedy zamiast params data
    # print (r.text) text show some text
    print (r.url)
def testing_post():
    payload = {'username':'corey', 'password': 'testing'}
    main_url = 'https://httpbin.org'
    rest_url = '/post'
    my_url = main_url+rest_url                #'https://httpbin.org/post'
    r = requests.post(my_url, data=payload)
    r_dict = r.json()
    print(r_dict['form'])
def json_testing():
    #tutorial https://www.youtube.com/watch?v=9N6a-VLBa2I
    state_string = '''
    {
        "states": [
            {
                "name": "Alabama",
                "abbreviation": "AL"
            },
            {
                "name": "Alaska",
                "abbreviation": "AK"
            },
            {
                "name": "Arizona",
                "abbreviation": "AZ"
            },
            {
                "name": "Arkansas",
                "abbreviation": "AR"
            },
            {
                "name": "California",
                "abbreviation": "CA"
            },
            {
                "name": "Colorado",
                "abbreviation": "CO"
            },
            {
                "name": "Connecticut",
                "abbreviation": "CT"
            },
            {
                "name": "Delaware",
                "abbreviation": "DE"
            },
            {
                "name": "Florida",
                "abbreviation": "FL"
            },
            {
                "name": "Georgia",
                "abbreviation": "GA"
            },
            {
                "name": "Hawaii",
                "abbreviation": "HI"
            },
            {
                "name": "Idaho",
                "abbreviation": "ID"
            },
            {
                "name": "Illinois",
                "abbreviation": "IL"
            },
            {
                "name": "Indiana",
                "abbreviation": "IN"
            },
            {
                "name": "Iowa",
                "abbreviation": "IA"
            },
            {
                "name": "Kansas",
                "abbreviation": "KS"
            },
            {
                "name": "Kentucky",
                "abbreviation": "KY"
            },
            {
                "name": "Louisiana",
                "abbreviation": "LA"
            },
            {
                "name": "Maine",
                "abbreviation": "ME"
            },
            {
                "name": "Maryland",
                "abbreviation": "MD"
            },
            {
                "name": "Massachusetts",
                "abbreviation": "MA"
            },
            {
                "name": "Michigan",
                "abbreviation": "MI"
            },
            {
                "name": "Minnesota",
                "abbreviation": "MN"
            },
            {
                "name": "Mississippi",
                "abbreviation": "MS"
            },
            {
                "name": "Missouri",
                "abbreviation": "MO"
            },
            {
                "name": "Montana",
                "abbreviation": "MT"
            },
            {
                "name": "Nebraska",
                "abbreviation": "NE"
            },
            {
                "name": "Nevada",
                "abbreviation": "NV"
            },
            {
                "name": "New Hampshire",
                "abbreviation": "NH"
            },
            {
                "name": "New Jersey",
                "abbreviation": "NJ"
            },
            {
                "name": "New Mexico",
                "abbreviation": "NM"
            },
            {
                "name": "New York",
                "abbreviation": "NY"
            },
            {
                "name": "North Carolina",
                "abbreviation": "NC"
            },
            {
                "name": "North Dakota",
                "abbreviation": "ND"
            },
            {
                "name": "Ohio",
                "abbreviation": "OH"
            },
            {
                "name": "Oklahoma",
                "abbreviation": "OK"
            },
            {
                "name": "Oregon",
                "abbreviation": "OR"
            },
            {
                "name": "Pennsylvania",
                "abbreviation": "PA"
            },
            {
                "name": "Rhode Island",
                "abbreviation": "RI"
            },
            {
                "name": "South Carolina",
                "abbreviation": "SC"
            },
            {
                "name": "South Dakota",
                "abbreviation": "SD"
            },
            {
                "name": "Tennessee",
                "abbreviation": "TN"
            },
            {
                "name": "Texas",
                "abbreviation": "TX"
            },
            {
                "name": "Utah",
                "abbreviation": "UT"
            },
            {
                "name": "Vermont",
                "abbreviation": "VT"
            },
            {
                "name": "Virginia",
                "abbreviation": "VA"
            },
            {
                "name": "Washington",
                "abbreviation": "WA"
            },
            {
                "name": "West Virginia",
                "abbreviation": "WV"
            },
            {
                "name": "Wisconsin",
                "abbreviation": "WI"
            },
            {
                "name": "Wyoming",
                "abbreviation": "WY"
            }
        ]
    }
    '''
    data = json.loads(state_string) #ladowanie pliku json do json string
    # print(type(data['states'])) # tak sprawdzamy czym jest co

    usd_rates = dict()
    # to jest specjalnie dla przykladu
    #chodzi o to ze mozemy pobrac 2 nowe rzeczy i wrzucic do dict()
    #przyklad kilka linijek nizej

    for states in data['states']: #mozemy tez isc "glebiej" np ['states']['name']['costam']
        print(states['name'], states['abbreviation'])

        # ważne jesli idziemy glebiej, to w princie nie wywalamy juz states tylko
        # ['name']['costam'] zamiast ['states']['name']['costam']

        # zamiast print mozemy to zapisac do zmiennej, np name= states['name']
        # wazne zeby states bylo to samą nazwa co jest za for,
        # czyli jesli za for mamy np item, to name=item['name']

        # zalozmy ze mamy dwie nowe zmienne np name oraz price
        # mozemy stworzyc nowy dict np: usd_rates[name]= price

        #name = item['resources']['fields']['name']
        #price = item['resources']['fields']['price']
        #usd_rates[name] = price
        #pamietajmy że jest to w pentlui
    #wiec aby sprawdzic co wyszlo robimy tak
    #print(usd_rates['USD/EUR'])  lub inna wartosc, sprawdzwa
    # a jak chce sprawdzic ile 50 $ to po prostu
    # print(50* float(usd_rates['USD/EUR']))

        #del states['name'] #to usunie wszystkie name z jsona
        #j esli chcemy isc glebiej to np states['name']['costam']
    new_string = json.dumps(data, indent=2, sort_keys=True)


    #tworzenie nowego json string z tego co zrobilismy, indent - ladnie wyglafa

    # dumps - json string, dump json file
    #sort_keys - opcjonalnie, ale porzadek
    #print(new_string)

    # przyklad zapisania do pliku
    with open('new_states.json', 'w') as f:
        json.dump(data,f, indent=2)
    # urllib - jakas alternatywa dla request

def json_testing2():
    with open('states.json') as f:
        data = json.load(f)
        # zaladowanie pliku z kompa do json string

def __main__():
    #download_page()
    #testing_get()
    #testing_post()
    json_testing()

if __name__ == "__main__":
    __main__()