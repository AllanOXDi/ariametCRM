from django.db import models


class Schedule(models.Model):
    date = models.DateField(max_length=100)
    time = models.TimeField(max_length=100)
    def __str__(self):
        return self.date
