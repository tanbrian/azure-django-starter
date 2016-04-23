from django.db import models
from django.contrib.auth.models import User


class Site(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    description = models.TextField()
    subdomain = models.CharField(max_length=30)
    logo_url = models.CharField(max_length=255)

    def __str__(self):
        return "%s %s" % (self.title, self.description)
