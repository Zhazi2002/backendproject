# Generated by Django 4.0.2 on 2022-02-28 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kumuz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True)),
            ],
        ),
    ]
