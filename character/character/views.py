from . import home, search, anime, characters, error
from django.http import HttpResponse

def home_page(request):
    return HttpResponse(home.main())

def search_page(request, query='f'):
    return HttpResponse(search.main(query))

def anime_page(request, id):
    return HttpResponse(anime.main(id))

def characters_page(request, id):
    return HttpResponse(characters.main(id))

def error_page(request):
    return HttpResponse(error.main())