from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title