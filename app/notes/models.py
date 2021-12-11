from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):

    title = models.CharField(max_length=128, null=True, blank=True)
    text = models.TextField()
    author = models.ForeignKey(to=User, related_name='notes', on_delete=models.CASCADE, null=True, blank=True)

    is_archived = models.NullBooleanField()
    is_deleted = models.NullBooleanField()

