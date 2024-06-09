# Generated by Django 5.0.1 on 2024-06-09 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_tags'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(to='projects.tag'),
        ),
    ]
