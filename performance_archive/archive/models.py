from django.db import models

class Performance(models.Model):
    title = models.CharField(max_length=200)
    add_date = models.DateTimeField('date added to archive')
    # type

class Venue(models.Model):
    add_date = models.DateTimeField('Date the venue was added')
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    website = models.URLField()

class Showtime(models.Model):
    performance = models.ForeignKey(Performance)
    venue = models.ForeignKey(Venue)
    add_date = models.DateTimeField('Date of show')
    cost = models.SmallIntegerField()

class Group(models.Model):
    add_date = models.DateTimeField('Date this group was added')
    name = models.CharField(max_length=200)
    website = models.URLField()
    venue = models.ForeignKey(Venue)

class Performer(models.Model):
    performance = models.ForeignKey(Performance)
    group = models.ForeignKey(Group)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    website = models.URLField()
    email = models.EmailField(max_length=200)
    bio = models.TextField()

