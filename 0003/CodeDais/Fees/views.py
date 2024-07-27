from django.shortcuts import render,HttpResponse

# Create your views here.
def fees_view(request):
    return HttpResponse('<h1>Hello you are in the fees section of code dais </h1>')