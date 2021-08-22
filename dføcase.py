import requests
import io


def get_flag(country):
    response = requests.get('https://restcountries.eu/rest/v2/name/'+country)
    if response.status_code == 200:
        return response.json()[0]['flag']
    return ""


response = requests.get("https://randomuser.me/api/?results=10")

if response.status_code == 200:
    with io.open("dfø.html", "w") as f:
        f.write('<!DOCTYPE html>\n<head><meta charset="UTF-8"></head><body>\n')

    with io.open("dfø.html", "a", encoding="utf-8") as f:

        for result in response.json()["results"]:
            print(result)
            name = '{} {} {}'.format(result['name']['title'], result['name']['first'], result['name']['last'])
            location = '{} {}, {}, {}, {} <img src="{}" width="20" height="12"/>'.format(
                                                  result['location']['street']['name'],
                                                  result['location']['street']['number'],
                                                  result['location']['city'],
                                                  result['location']['state'],
                                                  result['location']['country'],
                                                  get_flag(result['location']['country']))
            contact_info = 'email: {}, phone: {}, cell: {}'.format(result['email'], result['phone'], result['cell'])
            personal_info = 'age {}, {}'.format(result['dob']['age'], result['gender'])
            user_info = 'username: {}, registered: {}'.format(result['login']['username'], result['registered']['date'])

            f.write('<img src="{}"/><div>{}<br>{}<br>{}<br>{}<br>{}</div><hr>\n'.format(
                result['picture']['medium'], name, location, contact_info, personal_info, user_info))

        f.write("</body>")
else:
    print("Error", response.status_code)
