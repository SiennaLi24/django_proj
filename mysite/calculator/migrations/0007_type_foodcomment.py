# Generated by Django 4.0.2 on 2022-05-26 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0006_alter_comment_ratepost'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='foodComment',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
