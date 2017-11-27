from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.core.validators import URLValidator

# Create your models here.
categories = (
    (0,'--Aukeratu--'),
    ('Teknologia', 'Teknologia'),
    ('Albisteak', 'Albisteak'),
    ('Lanak', 'Lanak')
    )
class Article(models.Model):
        author = models.ForeignKey('auth.User')
        title = models.CharField(max_length=200)
        text = models.TextField()
        category = models.CharField(max_length=25, blank=True, null=True, choices = categories)
        url = models.URLField(validators=[URLValidator()], blank=True, null=True)
        drive_url = models.URLField(validators=[URLValidator()], blank=True, null=True)
        created_date = models.DateTimeField(default=timezone.now)
        published_date = models.DateTimeField(blank=True, null=True)
     
        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.title