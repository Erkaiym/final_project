from django.db import models
from django.db.models import ForeignKey

from user.models import Profile
from trip.models import Trip

class Proposal(models.Model):
    name = models.CharField(max_length=100)
    tel_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, related_name='proposal', on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, related_name='proposals', on_delete=models.CASCADE)

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
        choices=CHOICES, default=SENT
    )


    def __str__(self):
        return f'Запрос {self.name} на поездку {self.trip}'


