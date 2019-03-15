from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image


def photos_today(request):
    date = dt.date.today()
    photos = Image.objects.all()
    return render(request, 'all-photos/today-photos.html', {"date": date,"photos":photos})
# Create your views here.
def welcome(request):
     
    photos = Image.objects.all()
    return render(request, 'all-photos/welcome.html', {"photos":photos})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_image = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"image": searched_image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})


