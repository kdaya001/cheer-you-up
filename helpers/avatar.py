from random import randint

def generate_random_number():
    return randint(0,100000)

def generate_avatar():
    response =  f'https://avatars.dicebear.com/api/bottts/:{generate_random_number()}.svg'
    return response