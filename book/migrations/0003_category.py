# Generated by Django 4.2.1 on 2023-05-25 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_author_book_borrow_inventory_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('limit', models.IntegerField(default=5)),
                ('cost_per_day', models.FloatField(default=10.0)),
            ],
            options={
                'indexes': [models.Index(fields=['name'], name='book_catego_name_0178c4_idx')],
            },
        ),
    ]