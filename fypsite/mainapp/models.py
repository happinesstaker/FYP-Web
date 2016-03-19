from __future__ import unicode_literals

from django.db import models

class ArticleTable(models.Model):
    title_hash = models.CharField(primary_key=True, max_length=56)
    title = models.CharField(max_length=300)
    link = models.CharField(max_length=300, blank=True, null=True)
    source = models.CharField(max_length=50)
    content = models.CharField(max_length=6000, blank=True, null=True)
    date = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_table'

