# Generated by Django 4.0.2 on 2022-05-16 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0003_alter_type_totalcal'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddCal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='type',
            old_name='name',
            new_name='foodType',
        ),
        migrations.AddField(
            model_name='type',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='calculator.addcal'),
            preserve_default=False,
        ),
    ]