from django.shortcuts import render
from django.http  import HttpResponse


# Create your views here.
def welcome(request):
    return render(request, 'all-photos/welcome.html')

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_image = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"image": searched_image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-potos/search.html',{"message":message})


