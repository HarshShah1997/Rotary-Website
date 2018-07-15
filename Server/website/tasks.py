"""
Author: harsh
"""
from datetime import timedelta

from celery.task import periodic_task
from django.db import transaction

from clients.facebook import FacebookClient
from website.models import Photo


@periodic_task(run_every=timedelta(minutes=1))
def refresh_photos():
    update_database(fetch_photos())


def update_database(photos):
    with transaction.atomic():
        Photo.objects.all().delete()
        Photo.objects.bulk_create(photos)


def fetch_photos():
    client = FacebookClient.get_client()
    return parse_photos(client.get_photos())


def parse_photos(raw_photos):
    parsed_photos = [None] * len(raw_photos)
    for index, raw_photo in enumerate(raw_photos):
        parsed_photo = parse_photo(raw_photo)
        parsed_photos[index] = parsed_photo
    return parsed_photos


def parse_photo(raw_photo):
    photo = Photo()
    photo.fb_id = raw_photo['id']
    photo.fb_album_id = raw_photo['album']['id']
    photo.album_name = raw_photo['album']['name']
    photo.fb_link = raw_photo['picture']
    return photo
