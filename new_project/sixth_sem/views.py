from django.shortcuts import render


def index(request):
    hello = 'Приветствую на моем сайте!'
    return render(request, 'base.html', context={
        'title': 'Мой сайт',
        'content': hello,
        'footer': 'На этом пока всё...',
    })
