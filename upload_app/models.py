from django.db import models


class Student(models.Model):

    name = models.CharField(max_length= 20)
    image = models.ImageField(upload_to='images')
    profile = models.FileField(upload_to='profiles')

    def __str__(self):
        return self.name
