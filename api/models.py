from django.db import models

# Create your models here.


class Note(models.Model):
    title = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    changed = models.DateTimeField(auto_now=True)


def __str__(self):
    return self.body[0:50]

