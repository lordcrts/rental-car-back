# Generated by Django 4.2.4 on 2023-08-23 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specification',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internal.car', verbose_name='Car'),
        ),
    ]
