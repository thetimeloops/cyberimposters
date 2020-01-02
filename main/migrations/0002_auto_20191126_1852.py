# Generated by Django 2.2.7 on 2019-11-26 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogspot',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='blogspot',
            name='cat',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='blogspot',
            name='flags',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='blogspot',
            name='is_solved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='exclusive',
            name='avg_points',
            field=models.CharField(default='150', max_length=10),
        ),
        migrations.AddField(
            model_name='exclusive',
            name='low_points',
            field=models.CharField(default='10', max_length=10),
        ),
        migrations.AddField(
            model_name='exclusive',
            name='master_points',
            field=models.CharField(default='500', max_length=10),
        ),
        migrations.AddField(
            model_name='exclusive',
            name='password',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='exclusive',
            name='points',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='exclusive',
            name='pro_points',
            field=models.CharField(default='300', max_length=10),
        ),
        migrations.AddField(
            model_name='exclusive',
            name='try_points',
            field=models.CharField(default='50', max_length=10),
        ),
        migrations.AlterField(
            model_name='blogspot',
            name='habody',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='blogspot',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]