# Generated by Django 4.2.1 on 2023-05-23 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click Link above to read snippets', max_length=255),
        ),
    ]