from django.shortcuts import render
from django.http import HttpResponse
##creating a simple view
## request have to be the parameter
def hello(request):
    text = "<h1> hello world </h2>"
    return HttpResponse(text)

def hellorender(request):
    return render('hello.html')

def hello_with_param(request,username):
    return HttpResponse('your username is '%username)
