# Generated by Django 4.0.5 on 2022-12-13 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wepromo_main', '0004_post_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='sname',
        ),
        migrations.AddField(
            model_name='post',
            name='senderId',
            field=models.IntegerField(default=23),
        ),
    ]