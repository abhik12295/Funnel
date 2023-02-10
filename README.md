Funnel
============

core:

It's a Django Application which contains views, urls, models and connectivity to the database.

`python manage.py makemigration`

This command will generate a set of migration files based on the changes you've made to your models.

Once you've generated the migrations, you can apply the changes to your database by running the following command:

`python manage.py migrate`

This will create the necessary tables in your database to match the models you've defined in your Django project.


==========
### Add model to the django administration

from app folder (core) -> admin.py


`from django.contrib import admin`

`from .models import Profile`
# Register your models here.
`admin.site.register(Profile)`

Create Superuser or Admin to Django

`python manage.py createsuperuser`

enter username:

enter address:

enter passoword:

login to admin panel using :

`http://127.0.0.1:8000/admin/`

====================

### Signup

core -> urls.py :

`path('signup', views.signup, name='signup'),`

then add to core -> views.py
``

`{% csrf_token %}` to signup.html

 Template tag used in Django to include a CSRF token in a form. 
 CSRF (Cross-Site Request Forgery) is a security vulnerability that can occur when a malicious website sends a request to your website using the credentials of a logged-in user. To prevent this vulnerability, Django requires that a unique token be included in each form submitted by a user. 
 This token is verified on the server to ensure that the form was actually submitted by the user who requested it.

### views.py

add all the required functions:

index.html
signup.html
signin.html

Provide access/auth to User model -> signin, signup

##### Sign up
save user details in method after signup.
`user.save()`
======================
#### Create profile
`from .models import Profile`

will use models.py -> class Profile

use username(User) -> new_profile(`Profile.objects.create(user=user_model, id_user=user_model.id)`)



##### Signin
