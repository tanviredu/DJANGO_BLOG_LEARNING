from django.db import models

# Create your models here.
## this is the database its where you write your database
#3 every table starts witha  class
class Dreamreal(models.Model):
    ## this is where you wuite the column
    website =models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phonenumber = models.IntegerField()
    
    ##adding the foreign key
    ## first write the class online and then add it with the table
    ## who wants to connrct to the table
    online = models.ForeignKey('Online',default=1,on_delete=models.CASCADE)
    
    
    ## now we give the table name it will be inside 
    ## meta class
    class Meta:
        db_table = "dreamreal"
        
        ## apply this command in the browser
        #->python3 manage.py makemigrations
        #->python3 manage.py migrate
        
    ##aplying one to many relationsip
## adding the table which store which will show 
## the website which is online

class Online(models.Model):
    domain = models.CharField(max_length=50)
    
    ##give it a name
    class Meta:
        db_table = "online"
