from django.db import models

class Makale(models.Model):
    baslik = models.CharField(max_length=200)
    icerik = models.TextField()

    def __str__(self):
        return self.baslik