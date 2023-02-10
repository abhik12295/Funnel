from django.db import models
from django.contrib.auth import get_user_model

# current login user
User = get_user_model()
# Create your models here.
'''
Django provides a convenient API for working with the data in the database, 
including support for creating, reading, updating, and deleting records. 
Creating profile models
'''


class Profile(models.Model):
    # many-to-one relationship for multiple users
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileImg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
