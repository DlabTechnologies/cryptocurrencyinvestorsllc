# Generated by Django 3.0.5 on 2020-10-17 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0021_user_referer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='referer_name',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
