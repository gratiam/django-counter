from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Count

# Create your views here.
def index(request):
    # count = get_object_or_404(Count, key="croissants")
    return render(request, "counter/template_counter.html", {"count": "count"})

def saveUser(request, username=str, count=int):
    return HttpResponse("<h1>Something happened</h1>")

