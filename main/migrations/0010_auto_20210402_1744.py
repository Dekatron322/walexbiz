# Generated by Django 3.1.7 on 2021-04-02 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210402_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='added_bonus_five',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='added_bonus_four',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='added_bonus_six',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='added_bonus_three',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='added_bonus_two',
            field=models.TextField(blank=True, null=True),
        ),
    ]
