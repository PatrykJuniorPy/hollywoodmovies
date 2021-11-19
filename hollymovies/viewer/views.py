from django.shortcuts import render
from django.http import HttpResponse
from viewer.models import Movie, Genre
from django.views.generic import FormView, ListView
from viewer.forms import MovieForm
from logging import getLogger

from django.urls import reverse_lazy
from django.views.generic import FormView, ListView

from viewer.forms import MovieForm
from viewer.models import Movie

LOGGER = getLogger()

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
    

class MovieCreateView(FormView):
    
  template_name = 'forms.html'
  form_class = MovieForm
  success_url = reverse_lazy('movie_create')

  def form_valid(self, form):
    result = super().form_valid(form)
    cleaned_data = form.cleaned_data
    Movie.objects.create(
      title=cleaned_data['title'],
      genre=cleaned_data['genre'],
      rating=cleaned_data['rating'],
      released=cleaned_data['released'],
        description=cleaned_data['description']
    )
    return result

  def form_invalid(self, form):
    LOGGER.warning('User provided invalid data.')
    return super().form_invalid(form)