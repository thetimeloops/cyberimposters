# Generated by Django 2.1 on 2020-01-25 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_solvedctf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solvedctf',
            name='bulkctf',
        ),
        migrations.DeleteModel(
            name='solvedctf',
        ),
    ]