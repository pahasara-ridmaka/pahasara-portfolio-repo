# Generated by Django 5.0.1 on 2024-06-14 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.FileField(default='', upload_to='uploads/'),
        ),
    ]