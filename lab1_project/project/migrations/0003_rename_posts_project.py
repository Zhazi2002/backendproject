# Generated by Django 4.0.2 on 2022-02-25 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_posts_delete_project'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts',
            new_name='Project',
        ),
    ]
