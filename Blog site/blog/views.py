from re import template
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post
from django.db.models import Q
# Create your views here.

#def home(request):
    #return render(request,'index.html')

class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-id']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'post.html'

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def searchbar(request):
    if request.method=="GET":
        result = []
        search = request.GET.get('search')
        result = Post.objects.filter(Q(title__icontains=search) | Q(body__icontains=search) | Q(title_tag__icontains=search))
    return render(request,'searchbar.html',{'search': search, 'result' : result})

