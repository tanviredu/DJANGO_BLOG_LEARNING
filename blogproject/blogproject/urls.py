
from django.contrib import admin
## add the include in the file we use it to redirect
from django.urls import path,include




urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogapp/',include('blogapp.urls') ),
    
    
]
