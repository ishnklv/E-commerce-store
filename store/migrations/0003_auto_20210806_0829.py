# Generated by Django 3.1.5 on 2021-08-06 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210806_0821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='regular',
            new_name='price',
        ),
    ]
