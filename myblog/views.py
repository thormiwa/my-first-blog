from django.shortcuts import render
from django.utils import timezone
from .models import Blog

# Create your views here.
def post_list(request):
    blogs = Blog.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'myblog/post_list.html', {'blogs': blogs})