# Generated by Django 3.0.5 on 2021-03-14 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0035_user_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWithdrawRequestBankTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=500)),
                ('account_name', models.CharField(max_length=500)),
                ('account_number', models.CharField(max_length=500)),
                ('iban_swift', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=300)),
                ('withdraw_amount', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('withdraw_method', models.CharField(default='Bank Transfer', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='UserWithdrawRequestBtc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet_address', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=300)),
                ('withdraw_amount', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('withdraw_method', models.CharField(default='Bitcoin', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='UserWithdrawRequestOtherMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=300)),
                ('withdraw_amount', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('withdraw_method', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='UserWithdrawRequest',
        ),
    ]
