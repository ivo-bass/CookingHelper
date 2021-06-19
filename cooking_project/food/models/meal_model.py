from django.db import models


class Meal(models.Model):
    type = models.CharField(
        max_length=10,
    )
    start_time = models.TimeField(
        null=True,
    )
    end_time = models.TimeField(
        null=True,
    )

    def __str__(self):
        return self.type

    def is_in_time_range(self, time):
        return self.start_time <= time <= self.end_time
