# Generated by Django 4.2.8 on 2023-12-25 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weConnectApp', '0003_rename_post_createpost'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CreatePost',
            new_name='Post',
        ),
    ]