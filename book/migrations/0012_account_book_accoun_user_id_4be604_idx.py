# Generated by Django 4.2.1 on 2023-05-26 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_remove_customuser_account_account_user'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='account',
            index=models.Index(fields=['user_id'], name='book_accoun_user_id_4be604_idx'),
        ),
    ]
