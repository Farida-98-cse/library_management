# Generated by Django 4.2.1 on 2023-05-25 13:36

import book.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_customuser_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[(book.models.Role['staff'], 'Staff'), (book.models.Role['member'], 'Member')], default='Member', max_length=10),
        ),
    ]
