# Generated by Django 3.1.7 on 2021-04-05 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_servicefeature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicefeature',
            name='process_icon',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]