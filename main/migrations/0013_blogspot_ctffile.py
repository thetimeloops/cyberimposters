# Generated by Django 2.1 on 2020-02-20 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200125_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogspot',
            name='ctffile',
            field=models.FileField(null=True, upload_to='ctfs/'),
        ),
    ]
