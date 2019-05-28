from django.db import models
from django.urls import reverse

from user.models import Profile


class Trip(models.Model):
    start = models.CharField(max_length=250)
    end = models.CharField(max_length=250)
    date = models.DateField(auto_now=False, auto_now_add= False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    price = models.PositiveIntegerField(default=None)
    empty_seats = models.PositiveIntegerField(default=None)
    user = models.ForeignKey(Profile, related_name='trips', on_delete=models.CASCADE)

    def __str__(self):
        return self.start + '->' + self.end

    def get_absolute_url(self):
        return reverse('trip-detail', kwargs={'id':self.id})

