"""hollymovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from viewer.views import MovieCreateView, create_genre, hello_view, MoviesView, MovieUpdateView, MovieDeleteView, SubmitableLoginView



urlpatterns = [
    path('accounts/login/', SubmitableLoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls'), name='logout'),
    path('accounts/profile/logout/', admin.site.urls, name='a' ),
    path('accounts/profile/', admin.site.urls, name='a'),
    path('admin/', admin.site.urls, name='a'),
    path('hello/<s0>', hello_view),
    path('', MoviesView.as_view(), name='index'),
    path('create-genre/', create_genre, name="new-genre"),
    path('movie/create', MovieCreateView.as_view(), name="movie_create"),
    path('movie/update/<pk>', MovieUpdateView.as_view(), name="movie_update"),
    path('movie/delete/<pk>', MovieDeleteView.as_view(), name="movie_delete"),
    
    
    
    
]
