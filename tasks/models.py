from django.db import models


class Task(models.Model):
    text = models.CharField(max_length=300)
    is_complete = models.BooleanField(default=False)
