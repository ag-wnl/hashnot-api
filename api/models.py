from django.db import models

# Create your models here.

#create hashnot model -> user data
class Hashnot(models.Model):

    #might change user_id to email of user
    user_id = models.AutoField(primary_key=True)
    user_mail = models.CharField(max_length=255, default='None')
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=40, default=user_id)
    location = models.CharField(max_length=30)
    about = models.TextField()
    type = models.CharField(max_length=100, choices =   (('Programmer', 'Programmer'), ('Developer', 'Developer')))
    date_created = models.DateTimeField(auto_now=True)
    fav_techstack = models.TextField(default='None')
    community_respect = models.IntegerField(default = 100)

    def __str__(self):
        return self.username


#user model -> user content, posts etc
class HashnotUser(models.Model):
    post_subject = models.TextField(null=True)
    post_content = models.TextField(null=True)
    required_skills = models.TextField(null=True)
    contest_link = models.URLField(null=True)
    op_user = models.ForeignKey(Hashnot, on_delete=models.CASCADE, null=True)


    