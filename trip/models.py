from django.db import models


class Trip(models.Model):
    start = models.CharField(max_length=250)
    end = models.CharField(max_length=250)
    date = models.DateField(auto_now=False, auto_now_add= False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    price = models.PositiveIntegerField(default=0)
    empty_seats = models.PositiveIntegerField(default=0)

    def str(self):
        return self.start + '->' + self.end

