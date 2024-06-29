from django.db import models

# Create your models here.
class VideoId(models.Model):
    Id = models.CharField(max_length=100)

    def __str__(self):
        return self.name