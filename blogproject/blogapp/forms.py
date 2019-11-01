from django import forms 
from .models import Dreamreal


#################### by default form not custom ##############
class LoginForm(forms.Form):
    user = forms.CharField(max_length=150)
    password = forms.CharField(widget = forms.PasswordInput())
############################################################
    
    
    ## variablle name er sathe input filed er name match kore
    ## likhte hobe
    
    
    ## for user
    ## user
    ##<input type='text' ********name='user'********** placeholder='Enter username'>
    ## for password
    ## password
    ##<input type='password' *****name='password'********* placeholder='Enter password'>
    
   
   ###################### this is the file uploading starts #############

class ProfileForm(forms.Form):
    name = forms.CharField(max_length=150)
    picture = forms.ImageField()

       
    
    
        