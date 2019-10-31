from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime

### adding the mail packages
from django.core.mail import BadHeaderError,send_mail
from django.http import HttpResponseRedirect

##################### form section
## now import the form
from .forms import LoginForm


## we use the generic viwe module for supporting 
## just the static file and the easy use of the template
## rendering
## lets make just a static file in the templates
## normal approcach need a url pattern a view layer and 
## also the html file to do that
## file so less code

#from django.views.generic import TemplateView



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


#def hello(request):
#    return redirect("https://www.google.com")

#def viewArticle(request,articleId):
#    text = "Displaying article number "+str(articleId)
    ## you can find the exact year and month 
    ## of the post by fetching the data here
    ## then redirect this
    ## redirect can take a full url 
    ## or it will take function and the function parameter
#    return redirect(viewArticles,"2015","02")

    
    
#def viewArticles(request,year,month):
#    text = "Display articles of "+str(year)+" "+str(month)
#    return HttpResponse(text)

#def send_mail(request):
    ## take the subject
    ## message
    ## and the sender email
    ## this POST.get() is stil  a post request 
    ## but it will take a string first then the content 
    # which gives you define 
    # the header 
    # or you can use just post if you want
    
#    subject = rquest.POST.get('subject','')
#    message = request.POST.get('messgae','')
#    from_email = request.POST.get('from_email','')
#    if subject and message and from_email:
#        try:
#            send_mail(subject,messgae,from_email,['tanviredu2018@gmail.com'])
#        except:
#            return HttpResponse('something wrong')
    
    ### this use a POST from to send mail
    ## we do that in from request
    ## use shell first from sending email
    ## and you have to add the email settings in the project settings
#class StaticView(TemplateView):
#    template_name = "public/static.html"

#######################################3
## first make a form template
###### create the form logic

def login(request):
    username  = "not logged in"
    if request.method == "POST":
        ## get all the posted data at once
        MyLoginForm = LoginForm(request.POST)
        ## validate by one command
        if MyLoginForm.is_valid():
            ## fetch the username
            username = MyLoginForm.cleaned_data['username']
        else:
            ## initiate without the credential
            MyLoginForm = Loginform()
    ## then just render username in the 
    ## loggedin.html
    return render(request,'loggedin.html',{'username':username})