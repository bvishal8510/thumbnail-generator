# Generated by Django 2.0.7 on 2018-07-18 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='document',
            name='thumbnail',
            field=models.FileField(upload_to='media'),
        ),
    ]
