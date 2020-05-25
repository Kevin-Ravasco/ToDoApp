from django.db import models


class ToDo(models.Model):
    added_time = models.DateTimeField()
    text = models.CharField(max_length=200)

