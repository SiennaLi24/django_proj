# Generated by Django 4.0.2 on 2022-05-26 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0019_alter_type_foodtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='foodType',
            field=models.CharField(choices=[('dessert', 'Dessert'), ('main course', 'Main Course'), ('appetizer', 'Appetizer')], default='dessert', max_length=50),
        ),
    ]