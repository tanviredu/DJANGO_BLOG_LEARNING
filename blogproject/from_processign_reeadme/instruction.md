you can make a form in two way
1st-> 
    ->make a databse model in models.py
    -> add functionality in views.py
    -> not recomended
2nd->
    add form models in forms.py that is by default
    and add give you some extra functionality
    then add the functionality to the views.py

in both way you have to make a form template first


we are making this form in forms.py
if you dont find the file just create the file inside your app



you may have a question that there is no migration
then how this app is storing data

actually it isn used the default login database that same 
databse is used to enter the admin panel

if you want separate you have to use the first method
and to use the first method after creating databse you have to
migrate