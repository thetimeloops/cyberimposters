from django.db import models

# Create your models here.

class Blogspot(models.Model):
    post_id = models.AutoField(primary_key=True)
    serial = models.CharField(max_length=10,default="")
    title = models.CharField(max_length=200)
    habody = models.CharField(max_length=200 , default="")
    hint = models.CharField(max_length=200 , default="")
    hint2 = models.CharField(max_length=200 , default="")
    body = models.CharField(max_length=5000, default="")
    flags = models.CharField(max_length=200,default="")
    cat = models.CharField(max_length=200,default="")
    points = models.CharField(max_length=50 , default="")
    pub_date = models.DateField()
    ctffile=models.FileField(upload_to='ctfs/',null=True)
    is_solved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class exclusive(models.Model):
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    gender = models.CharField(max_length=30)
    points = models.CharField(max_length=10,default="0")
    password = models.CharField(max_length=50,default="")
    low_points = models.CharField(max_length=10,default="10")
    try_points = models.CharField(max_length=10,default="50")
    avg_points = models.CharField(max_length=10,default="150")
    pro_points = models.CharField(max_length=10,default="300")
    master_points = models.CharField(max_length=10,default="500")
    is_normal = models.BooleanField(default=True)
    


    solvedctfid = models.ManyToManyField("self")

    @property
    def solvedids(self):
        id = models.CharField(max_length=20,default="")
        return list(self.id.all())

    def __str__(self):
        return self.username









class notification(models.Model):
    pub_date = models.DateField()
    body = models.CharField(max_length=5000)

    def __str__(self):
        return self.body
