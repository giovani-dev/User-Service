# Generated by Django 3.1.7 on 2021-02-24 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile',
            new_name='login',
        ),
        migrations.AlterModelTable(
            name='profile',
            table='profile',
        ),
    ]
