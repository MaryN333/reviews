# Generated by Django 5.0.1 on 2024-01-15 11:35

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('note', models.CharField(max_length=900)),
                ('reviews_qty', models.IntegerField()),
                ('image', models.ImageField(upload_to='restaurant/images/')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=300)),
                ('stars', models.IntegerField()),
                ('expenses', models.IntegerField()),
                ('visit_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='restaurant.restaurant')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='restaurant',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='restaurant.type'),
        ),
    ]
