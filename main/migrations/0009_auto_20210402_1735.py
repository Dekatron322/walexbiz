# Generated by Django 3.1.7 on 2021-04-02 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210402_1718'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='how_it_works_five',
            new_name='added_bonus_five',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='how_it_works_five_icon',
            new_name='added_bonus_five_icon',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='how_it_works_four',
            new_name='added_bonus_four',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='how_it_works_four_icon',
            new_name='added_bonus_four_icon',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='how_it_works_one_icon',
            new_name='added_bonus_one_icon',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='how_it_works_one',
            new_name='added_bonus_six',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='how_it_works_six_icon',
            new_name='added_bonus_six_icon',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='how_it_works_six',
            new_name='added_bonus_three',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='how_it_works_three_icon',
            new_name='added_bonus_three_icon',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='how_it_works_three',
            new_name='added_bonus_two',
        ),
        migrations.RemoveField(
            model_name='product',
            name='how_it_works_two',
        ),
        migrations.AddField(
            model_name='product',
            name='added_bonus_a',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='added_bonus_b',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='added_bonus_c',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='added_bonus_d',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='added_bonus_e',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='added_bonus_f',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='added_bonus_one',
            field=models.TextField(blank=True, null=True),
        ),
    ]