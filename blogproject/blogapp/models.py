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
    
    ## now we give the table name it will be inside 
    ## meta class
    class Meta:
        db_table = "dreamreal"
