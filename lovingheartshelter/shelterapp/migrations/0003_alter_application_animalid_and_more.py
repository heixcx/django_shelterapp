# Generated by Django 4.1.2 on 2022-10-31 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelterapp', '0002_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='animalid',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='application',
            name='animalname',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='application',
            name='driverlicense',
            field=models.CharField(max_length=128),
        ),
    ]
