# Generated by Django 3.0.5 on 2020-08-13 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_auto_20200811_2217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phone_not_verified',
            new_name='email_not_verified',
        ),
    ]