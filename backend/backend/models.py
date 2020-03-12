from django.db import models


class Response(models.Model):
    dir = models.CharField(max_length=100)
    choice = models.CharField(max_length=1)  # 'A' or 'B'
    session = models.CharField(max_length=36)
