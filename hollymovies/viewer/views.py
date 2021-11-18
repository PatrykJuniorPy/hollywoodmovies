from django.shortcuts import render
from django.http import HttpResponse
from viewer.models import Movie, Genre
from django.views.generic import ListView

def hello_view(request, s0):
    s1 = request.GET.get('s1', '')
    return render (
        request,
        template_name="hello.html",
        context={'adjectives': [s0,s1, 'beatiful', 'wonderful']}
    )

class CreateGenre(ListView):
    template_name="create-genre.html"
    model = Genre


class MoviesView(ListView):
    template_name="movies.html"
    model = Movie
    # def get(self, request):
    #     return render(
    #         request, 
    #         template_name='movies.html',
    #         context={"movies": Movie.objects.all()}
    #     )

    
# def movies(request):
#     return render (
#         request,
#         template_name='movies.html',
#         context={'movies': Movie.objects.all()}
#     )

def create_genre(request):
    new_genre_name= request.GET.get('new-name', None)
    if new_genre_name is None:
        return render(request, template_name='create-genre.html')
    else:
        Genre.objects.create(name=new_genre_name)
        return HttpResponse(f"{new_genre_name} added to database!")