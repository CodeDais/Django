from django.shortcuts import render,HttpResponse

# Create your views here.
def course_view(request):
    return HttpResponse('<h1>Hello you are in the course section of code dais </h1>')