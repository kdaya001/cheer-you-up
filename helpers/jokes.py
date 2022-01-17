import requests

def get_rand_joke():
    response = requests.get(f'https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single')
    json = response.json()
    if json['error'] != False:
        return None
    else:
        return json['joke']