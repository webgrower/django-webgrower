from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Phone(models.Model):
    book = models.ForeignKey('Book')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    notes = models.TextField()
