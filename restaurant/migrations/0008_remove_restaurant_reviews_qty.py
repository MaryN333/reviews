# Generated by Django 3.2.20 on 2024-01-19 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_alter_review_restaurant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='reviews_qty',
        ),
    ]
