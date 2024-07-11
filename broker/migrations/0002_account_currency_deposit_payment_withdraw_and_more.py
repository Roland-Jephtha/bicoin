# Generated by Django 4.2.7 on 2024-04-29 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, null=True)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('profit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('referral', models.DecimalField(decimal_places=2, max_digits=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=255, null=True)),
                ('payment_slip', models.FileField(null=True, upload_to='payment_slip')),
                ('currency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='broker.currency')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet_address', models.CharField(max_length=255, null=True)),
                ('qr_code', models.FileField(null=True, upload_to='qr_code')),
            ],
        ),
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('withdraw_from', models.CharField(choices=[('Profit', 'Profit'), ('Balance', 'Balance'), ('Referral Bonus', 'Referral Bonus')], max_length=255, null=True)),
                ('wallet_address', models.CharField(max_length=255, null=True)),
                ('qr_code', models.CharField(max_length=255, null=True)),
                ('amount', models.CharField(max_length=255, null=True)),
                ('currency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='broker.currency')),
            ],
        ),
        migrations.CreateModel(
            name='Withdraw_bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=255, null=True)),
                ('bank_name', models.CharField(max_length=255, null=True)),
                ('name_of_account', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='ref_id',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='ref_id',
            field=models.CharField(default=0, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='referral',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='withdrawal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.DeleteModel(
            name='Profit',
        ),
        migrations.AddField(
            model_name='withdraw_bank',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='withdraw',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='deposit',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
