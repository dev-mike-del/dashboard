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


class Category(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    items = models.ManyToManyField(Detail, related_name='items')

    def __str__(self):
        return self.title


class SubGroup(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    categories = models.ManyToManyField(Detail, related_name='categories')

    def __str__(self):
        return self.title


class Group(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    sub_Group = models.ManyToManyField(Detail, related_name='sub_Group')

    def __str__(self):
        return self.title


class SubProperty(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    group = models.ManyToManyField(Detail, related_name='group')

    def __str__(self):
        return self.title