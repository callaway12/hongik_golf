# Generated by Django 2.1.7 on 2019-04-01 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190401_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gisu',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.TextField(max_length=10),
        ),
    ]
