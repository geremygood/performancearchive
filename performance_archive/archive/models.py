from django.db import models

class Performance(models.Model):
    title = models.CharField(max_length=200)
    add_date = models.DateTimeField('date added to archive')

class Performer(models.Model):
#    performance = models.ForeignKey(Performance)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
