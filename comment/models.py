from django.db import models
#from django.urls import reverse
from django.urls import reverse

from user.models import Profile


class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(Profile, related_name='comments', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.user} comment'

    def get_absolute_url(self):
        return reverse('comment-detail', kwargs={'id': self.id})
