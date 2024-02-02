from django import forms

from third_sem.models import Author, Post


class GameTypeForm(forms.Form):
    game_type = forms.ChoiceField(choices=[('C', 'coins'), ('D', 'dice'), ('H', 'hundred')])
    throw_number = forms.IntegerField(min_value=1, max_value=64)


class AuthorAddForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'email', 'bio', 'birthday']


class PostAddForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'category', 'views', 'is_published']


class AddPostFormWidget(forms.Form):
    title = forms.CharField(max_length=50,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}))
    content = forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Text'})
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    category = forms.CharField(max_length=50)
    views = forms.IntegerField(initial=0)
    is_published = forms.BooleanField(required=False,
                                      widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))


# Домашнее задание к семинару №4
class ImageForm(forms.Form):
    image = forms.ImageField()
