# Generated by Django 3.1.2 on 2020-10-03 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_sender', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=250, null=True, unique_for_date='created'),
        ),
    ]
