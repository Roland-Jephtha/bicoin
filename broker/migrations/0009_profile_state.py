# Generated by Django 4.2.7 on 2024-05-03 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0008_rename_first_name_profile_full_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
