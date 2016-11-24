from django.shortcuts import render,HttpResponse,Http404
from assign1.blog.models import *

# Create your views here.
def data_show(request):
    return render(request, "my_tamplet.html", {"my_languages": my_languages})


def data_get(request, id):
    try:
        return HttpResponse(my_languages[int(id)])
    except IndexError:
        raise Http404("We don't have any.")

def show_home(request):
    return render(request, "my_home.html")
