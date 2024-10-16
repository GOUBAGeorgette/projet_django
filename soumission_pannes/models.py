from django.db import models

class Panne(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    localisation = models.CharField(max_length=255)
    date_signalement = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
