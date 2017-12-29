from django.db import models

# Post model
# Field types as defined in https://docs.djangoproject.com/en/1.8/ref/models/fields/
from django.utils import timezone
from django.contrib.auth.models import User
class Post(models.Model):
  STATUS_CHOICES = (
      ('draft', 'Draft'),
      ('published', 'Published'),
  )
  title = models.CharField(max_length=250)
# slug is a unique field used for clean urls
  slug = models.SlugField(max_length=250,
                          unique_for_date='publish')
# author field using a foreign key. related_name says author can write many posts
  author = models.ForeignKey(User,
                             related_name='blog_posts')
  body = models.TextField()
  publish = models.DateTimeField(default=timezone.now)
# auto_now_add - date will be saved automatically when creating an object
  created = models.DateTimeField(auto_now_add=True)
# auto_now - date will be updated automatically when saving an object.
  updated = models.DateTimeField(auto_now=True)
# choices provides radio list that limits user to pick from select list
  status = models.CharField(max_length=10,
                            choices=STATUS_CHOICES,
                            default='draft')
# Meta - Metadata     
class Meta:
# Sort results by the publish. We specify descending order designated by prefix
     ordering = ('-publish',)
def __str__(self):
    return self.title