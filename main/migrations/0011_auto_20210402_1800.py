# Generated by Django 3.1.7 on 2021-04-02 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210402_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='added_bonus_a',
        ),
        migrations.RemoveField(
            model_name='product',
            name='added_bonus_b',
        ),
        migrations.RemoveField(
            model_name='product',
            name='added_bonus_c',
        ),
        migrations.RemoveField(
            model_name='product',
            name='added_bonus_d',
        ),
        migrations.RemoveField(
            model_name='product',
            name='added_bonus_e',
        ),
        migrations.RemoveField(
            model_name='product',
            name='added_bonus_f',
        ),
        migrations.RemoveField(
            model_name='product',
            name='added_bonus_five',
        ),
        migrations.RemoveField(
            model_name='product',
            name='added_bonus_five_icon',
        ),
        migrations.RemoveField(
            model_name='product',
            name='added_bonus_four',
        ),
        migrations.RemoveField(
            model_name='product',
            name='added_bonus_four_icon',
        ),
        migrations.RemoveField(
            model_name='product',
            name='added_bonus_one',
        ),
        migrations.RemoveField(
            model_name='product',
            name='added_bonus_one_icon',
        ),
        migrations.RemoveField(
            model_name='product',
            name='added_bonus_six',
        ),
        migrations.RemoveField(
            model_name='product',
            name='added_bonus_six_icon',
        ),
        migrations.RemoveField(
            model_name='product',
            name='added_bonus_three',
        ),
        migrations.RemoveField(
            model_name='product',
            name='added_bonus_three_icon',
        ),
        migrations.RemoveField(
            model_name='product',
            name='added_bonus_two',
        ),
        migrations.RemoveField(
            model_name='product',
            name='bg_content',
        ),
        migrations.RemoveField(
            model_name='product',
            name='bg_header',
        ),
        migrations.RemoveField(
            model_name='product',
            name='how_it_works_two_icon',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sbg_content',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sbg_description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sgb_image',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]