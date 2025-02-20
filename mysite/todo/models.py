from django.db import models

# Create your models here.
from django.db import models

class Item(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description
