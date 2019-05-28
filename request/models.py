from django.db import models
from django.db.models import ForeignKey

from user.models import Profile
from trip.models import Trip

class Request(models.Model):
    name = models.CharField(max_length=100)
    tel_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    profile = ForeignKey(Profile, related_name='request', on_delete=models.CASCADE)
    trip = ForeignKey(Trip, related_name='trip', on_delete=models.CASCADE)

    SENT = 'S'
    APPROVED = 'A'
    CANCELLED = 'C'
    CHOICES = (
        (SENT, 'Отправлен'),
        (APPROVED, 'Одобрен'),
        (CANCELLED, 'Не одобрен'),
    )

    status = models.CharField(
        max_length=1,
        choices=CHOICES, default=None
    )


    def __str__(self):
        return f'{self.name}'


