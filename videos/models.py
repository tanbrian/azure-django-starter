from django.db import models
from sites.models import Site


class Series(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return "%s %s" % (self.title, self.description)

class Video(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.CharField(max_length=255)
    rating = models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.title, self.description)