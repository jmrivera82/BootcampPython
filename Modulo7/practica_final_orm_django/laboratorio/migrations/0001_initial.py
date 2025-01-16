# Generated by Django 4.1.1 on 2025-01-13 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'laboratorio',
            },
        ),
        migrations.CreateModel(
            name='DirectorGeneral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('laboratorio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='laboratorio.laboratorio')),
            ],
            options={
                'db_table': 'director_general',
            },
        ),
    ]