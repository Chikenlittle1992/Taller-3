from django.db import models

# Create your models here.
class Shows(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    puntuation = models.IntegerField(default=5)

    def __str__(self):
        return self.title