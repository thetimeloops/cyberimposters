# Generated by Django 2.2.7 on 2019-11-25 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20191123_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogspot',
            name='thumbnail',
        ),
    ]
