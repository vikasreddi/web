# Generated by Django 3.1.1 on 2020-10-02 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_fav',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.CharField(max_length=2500),
        ),
    ]
