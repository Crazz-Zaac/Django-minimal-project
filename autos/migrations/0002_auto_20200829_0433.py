# Generated by Django 3.1 on 2020-08-29 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auto',
            old_name='coomments',
            new_name='comments',
        ),
    ]
