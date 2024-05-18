# Generated by Django 5.0.4 on 2024-05-12 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_reservation_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='books', to='book.author'),
        ),
    ]
