# Generated by Django 4.1.13 on 2024-06-24 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='author',
            table='authors',
        ),
        migrations.AlterModelTable(
            name='quote',
            table='quotes',
        ),
    ]