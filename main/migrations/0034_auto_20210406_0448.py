# Generated by Django 3.1.7 on 2021-04-06 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_auto_20210405_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='keywords',
            field=models.TextField(blank=True, null=True),
        ),
    ]
