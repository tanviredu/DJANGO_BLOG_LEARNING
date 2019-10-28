"""    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
## add the include in the file we use it to redirect
from django.urls import path,include
from . import views
#3 inclide the views

urlpatterns = [
    #path('hello/',views.hello,name='hello'),
    #path('hellorender/',views.hellorender,name='hellorender'),
    #path('hello_with_param/<str:username>',views.hello_with_param,name='hello_with_param'),
    #path('hello_with_multiple_param/<str:id>/<str:name>',views.hello_with_multiple_param,name='hello_with_multiple_param'),
    #path('hello_again/<str:id>/<str:name>/<str:department>',views.hello_again,name='hello_again'),
    path('render_index/',views.render_index,name='render_index')
    
]
