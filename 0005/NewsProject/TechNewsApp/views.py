from django.shortcuts import render,HttpResponse

# Create your views here.
def tech_view(request):
    return HttpResponse('<h1>Independence Day sale on Amazon, Flipkart: Best deals on smartphones, laptops, smart TVs here</h1>')