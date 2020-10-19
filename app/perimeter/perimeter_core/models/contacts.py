from django.core import serializers
from django.db import models

TITLES = [
    ("Mr.", "Mr."),
    ("Mrs.", "Mrs."),
    ("Miss.", "Miss."),
]

class Contact(models.Model):
    global TITLES

    title = models.CharField(
        max_length=12,
        choices = TITLES,
        blank=True,
        null=True,
    )

    alias = models.CharField(
        max_length=50,
    )

    first_name = models.CharField(
        max_length=50,
    )

    last_name = models.CharField(
        max_length=50,
    )

    middle_name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    job_post = models.CharField(
        max_length=60,
        blank=True,
        null=True,
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    updated_on = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.alias.__str__()

    def to_json(self):
        json_encoding = serializers.serialize('json', [self])
        return json_encoding

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'alias': self.alias,
            'first_name': self.first_name,
            'middle_name': self.last_name,
            'job_post': self.job_post,
            'created_on': self.created_on,
            'updated_on': self.updated_on,
        }

class ContactPhoneNumber(models.Model):

    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
    )

    phone_number = models.CharField(
        max_length=20,
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    updated_on = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.phone_number.__str__()

    def to_json(self):
        json_encoding = serializers.serialize('json', [self])
        return json_encoding

    def to_dict(self):
        return {
            'id': self.id,
            'created_on': self.created_on,
            'updated_on': self.updated_on,
            'email_address': self.email_address,
        }

class ContactEmail(models.Model):
    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
    )

    email_address = models.EmailField(
        max_length=60,
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    updated_on = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.email_address.__str__()

    def to_json(self):
        json_encoding = serializers.serialize('json', [self])
        return json_encoding

    def to_dict(self):
        return {
            'id': self.id,
            'email_address': self.email_address,
            'created_on': self.created_on,
            'updated_on': self.updated_on,
        }
    