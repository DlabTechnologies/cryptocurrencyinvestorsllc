# Generated by Django 3.0.5 on 2020-10-17 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0024_user_id_card_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_id_card_upload',
            name='confirmed',
        ),
    ]