from django.db import models

# Create your models here.

class Blogspot(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    habody = models.CharField(max_length=200 , default="")
    body = models.CharField(max_length=5000, default="")
    flags = models.CharField(max_length=200,default="")
    cat = models.CharField(max_length=200,default="")
    pub_date = models.DateField()
    is_solved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class exclusive(models.Model):
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    gender = models.CharField(max_length=30)
    points = models.CharField(max_length=10,default="")
    password = models.CharField(max_length=50,default="")
    def __str__(self):
        return self.username
