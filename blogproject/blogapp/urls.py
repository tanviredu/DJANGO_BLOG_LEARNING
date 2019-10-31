
from django.contrib import admin
## add the include in the file we use it to redirect
from django.urls import path,include
from . import views
#from .views import StaticView



## we use the generic viwe module for supporting 
## just the static file and the easy use of the template
## rendering
## lets make just a static file in the templates
## normal approcach need a url pattern a view layer and 
## also the html file to do that
# file so less code
#3 inclide the views
# static view is one way to do that
## lets do it with Template view
#from django.views.generic import TemplateView
## if you use the Template View you dont need 
## any views.py logic layer to render the static file

######################################################
##generic view with database direct rendering starts here
## we can directly return database model and send it ti the
## view directly using generic class like .NET we can dorectly
## return the database (model)
from django.views.generic import ListView
## you have to rnder the database 
from .models import Dreamreal
##########################################################

urlpatterns = [
    #path('hello/',views.hello,name='hello'),
    #path('hellorender/',views.hellorender,name='hellorender'),
    #path('hello_with_param/<str:username>',views.hello_with_param,name='hello_with_param'),
    #path('hello_with_multiple_param/<str:id>/<str:name>',views.hello_with_multiple_param,name='hello_with_multiple_param'),
    #path('hello_again/<str:id>/<str:name>/<str:department>',views.hello_again,name='hello_again'),
    #path('render_index/',views.render_index,name='render_index')
    #path('redirect_page/',views.redirect_page,name='redirect_page')
    #path('article/<str:articleId>',views.viewArticle,name='viewArticle'),
    #path('articles/<str:year>/<str:month>',views.viewArticles,name='viewArticles')
    #path('static/',StaticView.as_view() ),
    #path('static/',TemplateView.as_view(template_name='public/static.html'))
    ## add a path for the database direct rendering with ListView
    path('dreamreals/',ListView.as_view(model=Dreamreal,context_object_name="dreamreal_objects",template_name="public/listview_databse.html"))    
    
    
]
