# Generated by Django 2.0 on 2020-03-23 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_auto_20200323_1006'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Area',
            new_name='AreaD',
        ),
        migrations.AlterModelTable(
            name='aread',
            table='aread',
        ),
    ]
