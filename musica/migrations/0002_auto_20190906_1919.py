# Generated by Django 2.2.5 on 2019-09-06 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musica',
            name='artista',
            field=models.CharField(max_length=255, verbose_name='Artista'),
        ),
    ]
