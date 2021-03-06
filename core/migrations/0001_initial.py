# Generated by Django 2.0.7 on 2018-07-20 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('files', models.FileField(upload_to='media/')),
                ('document', models.ImageField(upload_to='')),
                ('thumbnail', models.ImageField(upload_to='thumbnail_media/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
