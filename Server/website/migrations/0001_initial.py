# Generated by Django 2.0.6 on 2018-06-28 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=1000)),
                ('file_link', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='BoardMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('profile_picture_link', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('fb_event_id', models.IntegerField(default=-1)),
                ('fb_album_id', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('fb_id', models.IntegerField(db_index=True, primary_key=True, serialize=False)),
                ('fb_album_id', models.IntegerField()),
                ('album_name', models.CharField(max_length=100)),
                ('fb_link', models.CharField(max_length=2000)),
            ],
        ),
    ]
