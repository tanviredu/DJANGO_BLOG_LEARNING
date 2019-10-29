from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
##creating a simple view
## request have to be the parameter
#def hello(request):
#    text = "<h1> hello world </h2>"
#    return HttpResponse(text)

#def hellorender(request):
#    return render(request,'hello.html')

#def hello_with_param(request,username):
#    return HttpResponse('your username is '+str(username))

#def hello_with_multiple_param(request,id=None,name=None):
#    text = "id "+str(id)+" "+"name "+str(name)
#    return HttpResponse(text)

#def hello_again(request,id=None,name=None,department=None):
#    text = "id "+str(id)+" "+"name "+str(name)+" "+"Department "+str(department)
#    return HttpResponse(text)

## now from this we render the html page
# the page have to be in the template folder
#def render_index(request):
#    id = 143000410
#    name = "Tanvir Rahman"
#    department = "EEE"
    
    ## adding an element to adding the turncate
    ## filter    
    
#    raw_content = "excepteur consectetur cupidatat ullamco aliquip consecteturr cupidatat ullamco aliquip consecteturr cupidatat ullamco aliquip consecteturr cupidatat ullamco aliquip consecteturr cupidatat ullamco aliquip consectetur non nostrud excepteur minim"
    ## you have to send  adictionary to
    ## you have to impot datetime first
#    value = datetime.datetime.now()
#    emaillist = ['ornobtanvir@gmail.com','tanviredu2018@gmail.com','mlhearbeat007@gmail.com']
    
    ## suppose sending a list of things
    
#    link = ['www.google.com','www.yahoo.com','www.amazon.com']
    
#    fruit = ['apple','banana','coconut','mango']
#    context = {'id':id,'name':name,'department':department,'raw_content':raw_content,'value':value,'fruit':fruit,'emaillist':emaillist,'link':link}
    #return render(request,'first.html',context)
    ## adding the raw content
#    return render(request,"public/first.html",context)

## this second.html will be extended from the layoyt base file
#def render_index(request):
#    return render(request,'public/second.html',{})

## page redirection


def hello(request):
    return redirect("https://www.google.com")

def viewArticle(request,articleId):
    text = "Displaying article number "+str(articleId)
    #return redirect('https://www.test.com')
    # redirect will take a function and other parameter
    #return HttpResponse(text)
    ## redirect can take a full url 
    ## or it will take function and the function parameter
    return redirect(viewArticles,"2015","02")

    
    
def viewArticles(request,year,month):
    text = "Display articles of "+str(year)+" "+str(month)
    return HttpResponse(text)