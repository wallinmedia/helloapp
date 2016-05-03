from django.db import models

class Aktiviteter(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Aktivitet'
        verbose_name_plural = 'Aktiviteter'


