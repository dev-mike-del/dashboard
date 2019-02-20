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


class Feature(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    details = models.ManyToManyField(Detail, related_name='details')

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    features = models.ManyToManyField(Detail, related_name='features')

    def __str__(self):
        return self.title
