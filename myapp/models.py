from django.db import models

class MyItem(models.Model):  # Renamed class
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
