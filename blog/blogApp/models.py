from dataclasses import fields
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PublishedManager(models.Manager):
    """
    model manager for the Post model including only PUBLISHED posts
    """
    
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    """
    blog post model
    """

    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(max_length=250)
    body = models.TextField()
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author', default=None)
    created = models.DateTimeField(default=timezone.now)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, default=Status.PUBLISHED, choices=Status.choices)

    objects = models.Manager()
    published_manager = PublishedManager()

    class Meta:
        ordering = ["-published"]
        indexes = [
                models.Index(fields=["-published"])
        ]
    
    def __str__(self):
        return self.title