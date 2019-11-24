from django.db import models

# Create your models here.

class buginfo(models.Model):
    post_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=500)
    link = models.CharField(max_length=30)
    scope_description = models.CharField(max_length=500)
    scope_link = models.CharField(max_length=50)
    outscope_description = models.CharField(max_length=500)
    P1 = models.CharField(max_length=50)
    P2 = models.CharField(max_length=50)
    P3 = models.CharField(max_length=50)
    P4 = models.CharField(max_length=50)
    points = models.CharField(max_length=50)

    def __str__(self):
        return self.link
