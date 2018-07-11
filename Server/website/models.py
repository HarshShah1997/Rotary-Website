from django.db import models


class Event(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    fb_event_id = models.IntegerField(default=-1)
    fb_album_id = models.IntegerField(default=-1)

    def __str__(self):
        return self.title


class Announcement(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=1000)
    file_link = models.CharField(max_length=2000)

    def __str__(self):
        return self.text


class BoardMember(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    profile_picture_link = models.CharField(max_length=2000)

    def __str__(self):
        return self.name


class Photo(models.Model):
    fb_id = models.IntegerField(db_index=True, primary_key=True)
    fb_album_id = models.IntegerField()
    album_name = models.CharField(max_length=100)
    fb_link = models.CharField(max_length=2000)

    def __str__(self):
        return "{}: {}".format(self.album_name, self.fb_id)
