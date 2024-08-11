from django.shortcuts import render,HttpResponse

# Create your views here.
def cricket_view(request):
    return HttpResponse('<h1>Tahlia McGrath wraps series 3-0 for Australia A after India A batting crumbles</h1>')