# Generated by Django 4.1.5 on 2023-02-07 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dailyjotter', '0002_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='posts'),
        ),
    ]
