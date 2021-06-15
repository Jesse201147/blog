import json

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from rest_framework import serializers


class ArticlePost(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def to_dict(self):
        return dict(
            id=self.id,
            author=self.author.username,
            title=self.title,
            body=self.body,
            created=str(self.created),
            updated=str(self.updated),
        )


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticlePost
        fields = ('id', 'title', 'author', 'updated')
