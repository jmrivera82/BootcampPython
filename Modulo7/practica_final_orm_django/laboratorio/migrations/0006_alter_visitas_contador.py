# Generated by Django 4.1.1 on 2025-01-16 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0005_visitas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitas',
            name='contador',
            field=models.IntegerField(default=0),
        ),
    ]
