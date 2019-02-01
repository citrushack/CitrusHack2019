# Generated by Django 2.1.5 on 2019-02-01 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_auto_20190130_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='learn_or_gain',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
