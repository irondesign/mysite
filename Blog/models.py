from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateField(auto_now=True)
    author = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, max_length=200)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Posts, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Pages(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    slug = models.SlugField(unique=True, blank=True, max_length=200)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Pages, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
