# Generated by Django 3.1.5 on 2021-08-07 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='post_code',
            new_name='postal_code',
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(blank=True, max_length=255),
        ),
    ]