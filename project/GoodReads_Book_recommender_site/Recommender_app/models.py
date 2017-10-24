# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ImageUpload(models.Model):
   book_id = models.IntegerField()
   book_title =models.CharField(max_length=100)
   image_url =models.CharField(max_length=100)

   class Meta:
      db_table = "ImageUpload"


class UserRating(models.Model):
   book_id=models.IntegerField()
   user_id =models.IntegerField(default=60000)
   rating=models.IntegerField()

   class Meta:
      db_table = "UserRating"   