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
    needs_garnish = models.BooleanField(
        default=False,
    )
    vegetarian = models.BooleanField(
        default=False,
    )
    image = models.ImageField(
        upload_to='static/images',
        verbose_name='food image',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

