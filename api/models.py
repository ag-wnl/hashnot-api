from django.db import models

# Create your models here.

#create hashnot model -> user data
class Hashnot(models.Model):

    #might change user_id to email of user
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    about = models.TextField()
    type = models.CharField(max_length=100, choices =   (('Programmer', 'Programmer'), ('Developer', 'Developer')))
    date_created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default = True)


#user model -> user content, posts etc
class HashnotUser(models.Model):
    post_subject = models.TextField()
    post_content = models.TextField()
