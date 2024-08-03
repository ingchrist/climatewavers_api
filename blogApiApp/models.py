from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='blogApiApp/')
    is_public = models.BooleanField(default=True, null=False, blank=False)
    reply = models.ManyToManyField("self")
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    type = models.IntegerField(default=0, null=False, blank=False, editable=False)
    likes_count = models.IntegerField(default=0, null=False, blank=False, editable=False)
    

    def __str__(self):
        return self.title