from django.core import serializers
from django.db import models

from datetime import datetime


class ServiceHandler(models.Model):
    name = models.CharField(
        max_length=100,
    )

    description = models.TextField()

    app_name = models.CharField(
        max_length=100,
    )

    on_created = models.DateField(
        auto_now_add=True,
    )

    on_updated = models.DateField(
        auto_now=True,
    )

    def __str__(self):
        return self.name

    def to_json(self):
        json_encoding = serializers.serialize('json', [self])
        return json_encoding
      
    def to_dict(self):
        return {
            'id': self.id,
            'created_on': self.created_on,
            'updated_on': self.updated_on,
            'name': self.name,
            'description': self.description,
            'app_name': self.app_name,
        }