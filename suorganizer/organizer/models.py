# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=31)
    slug = models.SlugField()

class Startup(models.Model):
    pass

class NewsLink(models.Model):
    pass
