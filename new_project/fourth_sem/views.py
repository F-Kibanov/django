from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from .forms import GameTypeForm, AuthorAddForm, PostAddForm, ImageForm
from first_sem.views import logger
from third_sem.models import Author, Post
from third_sem.views import coin, dice, hundred


def choice_game_type(request):
    if request.method == 'POST':
        form = GameTypeForm(request.POST)
        if form.is_valid():
            game_type = form.cleaned_data['game_type']
            throw_number = form.cleaned_data['throw_number']
            logger.info(f'Game: {game_type=}, Throws: {throw_number=}')
            if game_type == 'C':
                return coin(request, count=throw_number)
            elif game_type == 'D':
                return dice(request, count=throw_number)
            elif game_type == 'H':
                return hundred(request, count=throw_number)
            else:
                raise ValueError(f'Invalid game type: {game_type=}')
    else:
        form = GameTypeForm()
    return render(request, 'fourth_sem/games.html', {'form': form})


def add_author(request):
    if request.method == 'POST':
        form = AuthorAddForm(request.POST)
        message = 'Data error'
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            bio = form.cleaned_data['bio']
            birthday = form.cleaned_data['birthday']
            logger.info(f'Author: {name=}, {surname=}, {email=}, {bio=}, {birthday=}')
            author = Author.objects.create(name=name, surname=surname, email=email, bio=bio, birthday=birthday)
            author.save()
            return render(request, 'fourth_sem/author_form.html', {'author': author})
    else:
        form = AuthorAddForm()
        message = 'Fill the form!'
    return render(request, 'fourth_sem/author_form.html', {'form': form})


def add_post(request):
    if request.method == 'POST':
        form = PostAddForm(request.POST)
        message = 'Data error'
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            author = form.cleaned_data['author']
            post = Post.objects.create(title=title, content=content, author=author)
            post.save()
            return render(request, 'fourth_sem/author_form.html', {'post': post})
    else:
        form = PostAddForm()
        message = 'Fill the form!'
    return render(request, 'fourth_sem/author_form.html', {'form': form})


# Домашнее задание к семинару №4
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'fourth_sem/upload_image.html', {'form': form})
