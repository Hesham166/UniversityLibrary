# Generated by Django 5.0.4 on 2024-05-12 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_remove_book_author_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
