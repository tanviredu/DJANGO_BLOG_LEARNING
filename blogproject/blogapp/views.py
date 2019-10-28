from django.shortcuts import render
from django.http import HttpResponse
##creating a simple view
## request have to be the parameter
def hello(request):
    text = "<h1> hello world </h2>"
    return HttpResponse(text)

def hellorender(request):
    return render(request,'hello.html')

def hello_with_param(request,username):
    return HttpResponse('your username is '+str(username))

def hello_with_multiple_param(request,id=None,name=None):
    text = "id "+str(id)+" "+"name "+str(name)
    return HttpResponse(text)

def hello_again(request,id=None,name=None,department=None):
    text = "id "+str(id)+" "+"name "+str(name)+" "+"Department "+str(department)
    return HttpResponse(text)
