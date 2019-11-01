from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime

### adding the mail packages
from django.core.mail import BadHeaderError,send_mail
from django.http import HttpResponseRedirect

##################### form section
## now import the form
from .forms import LoginForm
from .models import Dreamreal

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



## this will render the form

#def gotologin(request):
#    return render(request,'public/form.html')



### this will handle the post request coming from the server
#def login(request):
    #return HttpResponse(request.method)
    
    
    
    #username  = "not logged in"
    
#    if request.method == "POST":
        ## create a login objetc
#        MyLoginForm = LoginForm(request.POST)
        #return HttpResponse(MyLoginForm.is_valid())
        
        ## if you dont create any user in the
        ## admin panel then it will show false
        ## you have to create user in the admin
        ## and the field name in the html and the forms
        ## should math
#        if MyLoginForm.is_valid(): ## this will check all the input data
#            username = MyLoginForm.cleaned_data['user']
#            dbuser = Dreamreal.objects.filter(name=username)
#            if not dbuser:
                #return HttpResponse("Its you")
#                return render(request,'public/loggedin.html',{'username':username})
            ## now check in the database
            
#        else:
#            MyLoginForm = LoginForm()
#            return HttpResponse("not you")



###############################file upload starts here #####################333

from .forms import ProfileForm
from .models import Profile


##### function dor saving profile

def SaveProfile(request):
    saved = False
    if request.method =="POST":
        ### get the data
        MyProfileForm = ProfileForm(request.POST,request.FILES) ## get the two paramenter
        ##check if valid
        if MyProfileForm.is_valid():
            #### create the database object to isave the data
            profile = Profile()  ## instantiate the class
            profile.name = MyProfileForm.cleaned_data['name'] 
            profile.picture = MyProfileForm.cleaned_data['picture']
            ### fetched the data
            ##now save the data
            profile.save()
            saved=True
    else:
        ##just create an empty object
        MyProfileForm = ProfileForm()
    return render(request,'saved.html',locals())

    ## what is locals()  ??
    # generally we send a dictionary
    # but if you want to send all the key value pair in the page that is created
    # not any specfic one you can use locals()
    # that will send all the value in a dict
    # you can use the regular dic also 

