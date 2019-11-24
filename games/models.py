from django.db import models

# Create your models here.

class about_game(models.Model):
    title = models.CharField(max_length=90)
    date = models.DateField()
    venue  = models.CharField(max_length=500)
    about = models.CharField(max_length=3000)

    def __str__(self):
        return self.title


class game_regis(models.Model):
    name = models.CharField(max_length=90)
    year = models.CharField(max_length=90)
    type = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name
