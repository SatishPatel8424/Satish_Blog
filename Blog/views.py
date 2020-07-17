from django.shortcuts import render

# Create your views here.


from django.views import generic
from .models import Blog, BlogAuthor, BlogComment
from django.contrib.auth.models import User

def index(request):
    """
    View function for home page of site.
    """
    # Render the HTML template index.html
    return render(
        request,
        'index.html',
    )



