# Generated by Django 4.1.6 on 2023-02-17 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Dailyjotter", "0005_alter_post_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="posts"),
        ),
        migrations.AlterField(
            model_name="post", name="slug", field=models.SlugField(unique=True),
        ),
    ]
