# Generated by Django 3.2.7 on 2021-10-11 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211009_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='media/avatars/avatar.jpg', upload_to='media/avatars', verbose_name='Фото'),
        ),
    ]
