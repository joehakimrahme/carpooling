from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Ad(models.Model):
    origin = models.ForeignKey(Location, related_name="ads_origin")
    destination = models.ForeignKey(Location, related_name="ads_destination")
    departure_date = models.DateTimeField('departure date')
    publication_date = models.DateTimeField('date published')

    def __unicode__(self):
        return "From {} to {} at {}".format(self.origin,
                                            self.destination,
                                            self.departure_date)
