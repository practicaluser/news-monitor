from django.db import models

class Keyword(models.Model):
    word = models.CharField(max_length=100)

    def __str__(self):
        return self.word

# Create your models here.
