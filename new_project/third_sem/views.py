import logging
from random import choice, randint

from django.shortcuts import HttpResponse, render

from third_sem.models import Author, Coin, Post, Client, Product, Order

logger = logging.getLogger()


def coin(request, count):
    coin_res = []
    for i in range(count):
        coin_state = choice(['head', 'tail'])
        logger.info(f'Function coin returns {coin_state}')
        coin_res.append(coin_state)

    context = {
        'title': 'Coin flip game',
        'header': 'Coin gives:',
        'content': coin_res,
    }
    return render(request, template_name='third_sem/games_page.html', context=context)


def dice(request, count):
    res = []
    for i in range(count):
        dice_ = randint(1, 6)
        logger.info(f'Function dice returns {dice_}')
        res.append(dice_)
    context = {
        'title': 'Dice game',
        'header': 'Dice gives:',
        'content': res,
    }
    return render(request, template_name='third_sem/games_page.html', context=context)


def hundred(request, count):
    res = []
    for i in range(count):
        hundred_ = randint(0, 100)
        logger.info(f'Function hundred returns {hundred_}')
        res.append(hundred_)
    context = {
        'title': 'Hundred game',
        'header': 'Random number in range 0-100 is:',
        'content': res,
    }
    return render(request, template_name='third_sem/games_page.html', context=context)


def authors_view(request):
    authors = Author.objects.all()
    res_str = '<br>'.join([str(author) for author in authors])
    return HttpResponse(res_str)


def post_view(request):
    posts = Post.objects.all()
    res_str = '<br>'.join([str(post) for post in posts])
    return HttpResponse(res_str)


def author_posts(request, author_id):
    author = Author.objects.get(id=author_id)
    posts = Post.objects.filter(author=author)
    context = {'header': author, 'content': posts}
    return render(request, template_name='third_sem/author_post.html', context=context)


def post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'title': post.title, 'header': post.author, 'content': post.content}
    return render(request, template_name='third_sem/post.html', context=context)


# """Домашнее задание к семинару №3"""


def get_client_orders(request, client_id):
    orders_list = []
    orders = Order.objects.filter(client_id=client_id)
    orders_list.append([str(order) for order in orders])
    context = {
        'title': 'Orders list',
        'header': f'Orders list for client {client_id}',
        'content': orders_list,
    }
    return render(request, template_name='third_sem/orders_list.html', context=context)
