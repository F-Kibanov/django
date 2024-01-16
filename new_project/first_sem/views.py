import logging
from random import choice, randint
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def log(view_func):
    def wrapper(request):
        logger.info(f'Function {view_func.__name__} was called')
        return view_func(request)
    return wrapper


@log
def hello(request):
    return HttpResponse('Hello, world!')


@log
def about(request):
    return HttpResponse('About us')


@log
def coin(request):
    coin_list = ['head', 'tail']
    coin_state = choice(coin_list)
    logger.info(f'Function coin returns {coin_state}')
    return HttpResponse(coin_state)


@log
def dice(request):
    dice_ = randint(1, 6)
    logger.info(f'Function dice returns {dice_}')
    return HttpResponse(f'Dice gives {dice_}')


@log
def hundred(request):
    hundred_ = randint(0, 100)
    logger.info(f'Function hundred returns {hundred_}')
    return HttpResponse(f'Random number in range 0-100 is: {hundred_}')


@log
def main(request):
    html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Main</title>
    </head>
    <body>
        <h1>This is django project main page</h1>
    </body>
    </html>
    """
    return HttpResponse(html)


@log
def about_me(request):
    html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>About me</title>
    </head>
    <body>
        <h1>This is about me page</h1>
    </body>
    </html>
    """
    return HttpResponse(html)
