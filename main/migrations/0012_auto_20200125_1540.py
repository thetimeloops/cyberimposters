# Generated by Django 2.1 on 2020-01-25 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200125_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exclusive',
            name='solvedctfid',
        ),
        migrations.AddField(
            model_name='exclusive',
            name='solvedctfid',
            field=models.ManyToManyField(related_name='_exclusive_solvedctfid_+', to='main.exclusive'),
        ),
    ]
