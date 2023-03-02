from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=50, blank=False, null=False)
    country = models.CharField(default='ligma', max_length=50, blank=False, null=False)
    city = models.CharField(default='bolsy', max_length=50, blank=False, null=False)

def __str__(self):
    return self.name