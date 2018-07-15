# Generated by Django 2.0.6 on 2018-07-15 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='fb_album_id',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='event',
            name='fb_event_id',
            field=models.BigIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='photo',
            name='fb_album_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='photo',
            name='fb_id',
            field=models.BigIntegerField(db_index=True, primary_key=True, serialize=False),
        ),
    ]
