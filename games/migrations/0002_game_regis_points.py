# Generated by Django 2.2 on 2020-01-01 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game_regis',
            name='points',
            field=models.CharField(default='', max_length=50),
        ),
    ]
