# Generated by Django 3.1.4 on 2021-03-04 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210304_1326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userconfig',
            old_name='useremail',
            new_name='useraccount',
        ),
    ]