# Generated by Django 4.2 on 2024-05-16 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desafioadl', '0002_rename_eliminada_subtarea_estado_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subtarea',
            old_name='estado',
            new_name='eliminada',
        ),
    ]
