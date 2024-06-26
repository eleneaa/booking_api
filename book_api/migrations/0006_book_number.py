# Generated by Django 5.0.4 on 2024-05-05 17:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_api', '0005_remove_book_id_book_book_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
