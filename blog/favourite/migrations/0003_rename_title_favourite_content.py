# Generated by Django 4.0.6 on 2022-09-07 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favourite', '0002_alter_favourite_post_alter_favourite_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favourite',
            old_name='title',
            new_name='content',
        ),
    ]
