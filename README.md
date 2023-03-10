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

authenticate user with their username and password -> auth.authenticate

`user = auth.authenticate(username = "" , password= "" )`

if user exist then try logging in with auth.login

`auth.login(request, user)`


##### Logout
`auth.logout(request)`

also add a decorators to main home page, once logout, it should ask for login page

use following before def index(request) and logout(request):

`from django.contrib.auth.decorators import login_required`

`@login_required(login_url='signin')`


##### Account Setting

views.py -> signup function -> once user is signed up ->
redirect to setting page

`user_login = auth.authenticate(username, passwd)`
`auth.login(request, user_login)`

models->user -> views.py-> setting(request)


`user_profile = Profile.objects.get(user=request.user)`

''''
"multipart/form-data" is the encoding type used in HTML forms to upload files to a server
''''

user_profile = Profile.objects.get(user=request.user)

    `if request.method == 'POST':
        if request.FILES.get('image') is None:
            image = user_profile.profileImg
            bio = request.POST['bio']
            location = request.POST['location']
            
            # save data for user_profile -> img, bio, location
            user_profile.profileImg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()`


##### Uploading posts
Create Model -> in models.py

do `python manage.py makemigrations`

then `python manage.py migrate`

add this to admin panel
`admin.site.register(Post)`

add to urls.py path:
`path('upload', views.upload, name='upload')`

under views.py:
---------------

`
if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']
        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()
        return redirect('/')
    else:
        return redirect('/')
`