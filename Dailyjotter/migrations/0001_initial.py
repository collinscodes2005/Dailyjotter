# Generated by Django 4.1.6 on 2023-02-03 16:16

import Dailyjotter.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=120)),
                ('user_name', models.CharField(max_length=300)),
                ('password', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('excerpt', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=Dailyjotter.models.image)),
                ('content', models.TextField(max_length=400)),
                ('slug', models.SlugField(unique=True)),
                ('date', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dailyjotter.author')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
