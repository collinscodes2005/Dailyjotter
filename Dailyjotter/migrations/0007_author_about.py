# Generated by Django 4.1.6 on 2023-02-21 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Dailyjotter", "0006_author_image_alter_post_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="about",
            field=models.CharField(max_length=170, null=True),
        ),
    ]
