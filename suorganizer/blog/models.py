# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from organizer.models import Startup, Tag

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField()
    text = models.TextField()
    pub_data = models.DateField()
    tags = models.ManyToMany(Tag)
    startups = models.ManyToMany(Startup)
