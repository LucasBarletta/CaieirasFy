# Generated by Django 2.2.5 on 2019-09-13 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0003_auto_20190913_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musica',
            name='genero',
            field=models.CharField(max_length=255, verbose_name='genero'),
        ),
    ]
