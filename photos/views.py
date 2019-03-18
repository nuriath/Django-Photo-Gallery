from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image

# Create your views here.
def welcome(request):
     
    photos = Image.objects.all()
    return render(request, 'all-photos/welcome.html', {"photos":photos})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_image = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"image": searched_image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})

    if 'location' in request.GET and request.GET["location"]:
        search_term = request.GET.get("location")
        searched_image = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"image": searched_image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})   

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/image.html", {"image":image})
