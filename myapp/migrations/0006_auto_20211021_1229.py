# Generated by Django 3.1 on 2021-10-21 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='pub_date',
            new_name='message_date',
        ),
    ]
