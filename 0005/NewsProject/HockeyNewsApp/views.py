from django.shortcuts import render,HttpResponse
# Create your views here.
def hockey_news(request):
    return HttpResponse('<h1> Canada players celebrate with their gold medals after defeating Sweden in the mens ice hockey gold </h1>')