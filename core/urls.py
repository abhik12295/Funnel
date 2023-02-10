from django.urls import path
from . import views

# view we have most coding part -> views file in same dir

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
]