from django.shortcuts import render,HttpResponse

# Create your views here.
def display_id(request,id):
    return HttpResponse(id)

def display_name(request,name):
    return HttpResponse(name)

def display_sal(request,sal):
    sal=float(sal)
    print(type(sal))
    return HttpResponse(sal)
def display_roll_name(request,roll,name):
    return HttpResponse(f'Roll is : {roll} and Name is : {name}')