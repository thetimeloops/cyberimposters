from django.db import models

# Create your models here.


class linux_data(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    para1 = models.CharField(max_length=5000, default="")
    para2 = models.CharField(max_length=5000, default="")
    para3 = models.CharField(max_length=5000,default="")
    pub_date = models.DateField()
    blog_pic = models.ImageField(upload_to='blog_images', default="")

    def __str__(self):
        return self.title
