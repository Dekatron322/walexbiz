# Generated by Django 3.1.7 on 2021-04-02 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('keywords', models.CharField(max_length=350, null=True)),
                ('description', models.CharField(max_length=350, null=True)),
                ('address', models.CharField(blank=True, max_length=150)),
                ('company', models.CharField(blank=True, max_length=150)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('fax', models.CharField(blank=True, max_length=20)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('smtpserver', models.CharField(blank=True, max_length=50)),
                ('smtpemail', models.CharField(blank=True, max_length=50)),
                ('smtppassword', models.CharField(blank=True, max_length=50)),
                ('smtpport', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('facebook', models.CharField(blank=True, max_length=50)),
                ('instagram', models.CharField(blank=True, max_length=50)),
                ('twitter', models.CharField(blank=True, max_length=50)),
                ('aboutus', models.TextField(blank=True)),
                ('contact', models.TextField(blank=True)),
                ('footer_text', models.TextField(blank=True, null=True)),
                ('references', models.TextField(blank=True)),
            ],
        ),
    ]