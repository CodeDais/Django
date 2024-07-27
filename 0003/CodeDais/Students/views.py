from django.shortcuts import render,HttpResponse

# Create your views here.
def student_view(request):
    return HttpResponse('<h1>Hello you are in the student section of code dais </h1>')