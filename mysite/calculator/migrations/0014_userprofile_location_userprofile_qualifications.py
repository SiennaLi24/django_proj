# Generated by Django 4.0.2 on 2022-05-23 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0013_alter_type_foodtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='qualifications',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
