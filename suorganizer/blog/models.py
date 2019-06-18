# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from organizer.models import Startup, Tag

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(
        max_length=63,
        help_text='A label for URL config',
        unique_for_month='pub_date')
    text = models.TextField()
    pub_date = models.DateField(
        'date published',
        auto_now_add=True)
    tags = models.ManyToMany(
        Tag,
        related_name='blog_posts')
    startups = models.ManyToMany(
        Startup, related_name='blog_posts')
