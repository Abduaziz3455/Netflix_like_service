# Generated by Django 4.1.2 on 2022-11-28 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0011_video_timestamp_video_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_id',
            field=models.CharField(max_length=220, unique=True),
        ),
    ]
