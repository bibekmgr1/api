from django.db import models


# Create your models here.
class HouseDetails(models.Model):
    #This class represents the house model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    power_consumption = models.IntegerField()

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

