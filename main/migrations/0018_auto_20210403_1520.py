# Generated by Django 3.1.7 on 2021-04-03 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20210403_0642'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='home_body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='home_header',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='home_icon',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
