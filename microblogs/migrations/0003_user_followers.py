# Generated by Django 3.2.8 on 2021-12-03 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microblogs', '0002_auto_20211122_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(related_name='followees', to='microblogs.User'),
        ),
    ]