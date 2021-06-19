from django.db import models

from .coarse_model import Coarse


class Food(models.Model):
    name = models.CharField(
        max_length=30,
    )
    type = models.ForeignKey(
        Coarse,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        upload_to='static/images',
        verbose_name='food image',
        null=True,
    )

    def __str__(self):
        return self.name

