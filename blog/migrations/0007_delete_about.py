# Generated by Django 4.2.7 on 2023-11-19 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_about'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About',
        ),
    ]