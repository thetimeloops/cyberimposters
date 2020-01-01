# Generated by Django 2.2 on 2020-01-01 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_game_regis_points'),
    ]

    operations = [
        migrations.CreateModel(
            name='winner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=40)),
                ('points_game', models.CharField(max_length=10)),
                ('tier', models.CharField(max_length=20)),
            ],
        ),
    ]
