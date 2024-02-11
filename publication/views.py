from django.shortcuts import render

from publication.models import Publication


# Create your views here.
def index(request):
    publications = Publication.objects.all
    return render(request, 'publication/index.html', context={"publications": publications})

