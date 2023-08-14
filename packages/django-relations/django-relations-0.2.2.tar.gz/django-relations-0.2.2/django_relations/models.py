from django.db import models
from .managers import DjangoRelationsManager


class AbstractDefaultClass(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = DjangoRelationsManager()

    class Meta:
        abstract = True
