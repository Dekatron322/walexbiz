# Generated by Django 3.1.7 on 2021-04-05 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_header_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topfeature',
            old_name='detail',
            new_name='detail_one',
        ),
        migrations.AddField(
            model_name='topfeature',
            name='detail_two',
            field=models.TextField(blank=True, null=True),
        ),
    ]
