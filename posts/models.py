from django.db import models

# Create your models here.

class Post(models.Model):
    author = models.CharField(max_length=100)
    caption = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.author
