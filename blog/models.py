from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    objects = models.Manager() #default Manager
    published = PublishedManager()
    title = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=250, unique_for_date='publish', null=True)
    author = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='blog_posts',
                                null=True)
    body = models.TextField(null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    views = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")

    def get_absolute_url(self):
        return reverse('blog:post_details', args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug])

    class Meta:
        ordering = ('-publish',)    

    def __str__(self):
        return self.title