import string, random, os
from django.shortcuts import render


def index(request):
    return render(request, 'generator/index.html')

def password(request):
    characters = list(string.ascii_lowercase)

    if request.GET.get('uppercase'):
        characters.extend(list(string.ascii_uppercase))
    if request.GET.get('numbers'):
        characters.extend(list(string.digits))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*(){}[]":><.,~-_'))

    length = int(request.GET.get('length', 12))

    password = ''
    for _ in range(length):
        password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': password})

