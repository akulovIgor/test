from django.shortcuts import render, render_to_response
from .scripts.translate import *


def index(request):
    return render(request, 'index.html', {'text': '', 'translated': ''})


def translate(request):
    if request.GET:
        text = str(request.GET.get('q'))
        translated = str(detect_text(text)['lang'])
        if translated == 'en':
            translated = get_translate(text, 'ru')['text']
        elif translated == 'ru':
            translated = get_translate(text, 'en')['text']
        else:
            translated = 'Я тебя не понимаю'
        args = {'text': text, 'translated': translated}
        return render(request, 'index.html', args)
    return render_to_response('index.html', {'text': '', 'translated': ''})
