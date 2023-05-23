from django.urls import path
from . import views
from .views import HomeView,ArticleDetailView

urlpatterns = [

    #path('',views.home,name='home'),
    path('/about',views.about,name='about'),
    #path('/home',views.home,name='home'),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>',ArticleDetailView.as_view(), name='article-detail'),
    path('/contact',views.contact,name='contact'),
    path('searchbar/',views.searchbar,name='searchbar')
]