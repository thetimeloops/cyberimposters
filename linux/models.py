from django.db import models

# Create your models here.


class linux(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    habody = models.CharField(max_length=200 , default="")
    body = models.CharField(max_length=5000, default="")
    flags = models.CharField(max_length=200,default="")
    cat = models.CharField(max_length=200,default="")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='up_images', default="")
    is_solved = models.BooleanField(default=False)
