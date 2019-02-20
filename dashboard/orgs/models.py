from django.db import models


class Point(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()

    def __str__(self):
        return self.title


class Detail(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    points = models.ManyToManyField(Point, related_name='points')

    def __str__(self):
        return self.title
