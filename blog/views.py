from django.shortcuts import render
# Create your views here.


posts = [
    {
        'author': 'itachi',
        'title': 'Blog Post 1',
        'content': 'This is the first post content',
        'date_posted': 'Oct 24, 2019'
    },
    {
        'author': 'uchiha',
        'title': 'Blog Post 2',
        'content': 'This is the Second post content',
        'date_posted': 'Oct 25, 2019'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
