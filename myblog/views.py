from django.shortcuts import render
from django.utils import timezone
from .models import Blog
from django.shortcuts import get_object_or_404

# Create your views here.
def post_list(request):
    blogs = Blog.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'myblog/post_list.html', {'blogs': blogs})

def post_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'myblog/post_detail.html', {'blog': blog})