from django.db import models

from cooking_project.food.models import Food, Meal, Garnish


class Choice(models.Model):
    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE,
    )

    meal = models.ForeignKey(
        Meal,
        on_delete=models.CASCADE,
    )

    garnish = models.ForeignKey(
        Garnish,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    due_date = models.DateField()

    def __str__(self):
        garnish = f" с {self.garnish.name}" if self.garnish else ''
        return f"{self.food.name}{garnish} - {self.due_date.__str__()}"
