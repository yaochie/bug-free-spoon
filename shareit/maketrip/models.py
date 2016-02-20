from django.db import models

# Create your models here.
class Itinerary(models.Model):
    pass

class Place(models.Model):
    HOTEL = 'H'
    FOOD = 'F'
    ATTRACTION = 'A'
    PLACE_TYPES = ((HOTEL, u"Hotel"),
                   (FOOD, u"Food"),
                   (ATTRACTION, u"Attraction"))
    
    DAWN = 'D'
    EARLY_MORNING = "EM"
    LATE_MORNING = "LM"
    EARLY_AFTERNOON = "EA"
    LATE_AFTERNOON = "LA"
    EVENING = "E"
    NIGHT = "N"
    LATE_NIGHT = "LN"
    WEE_HOURS = "WH"
    TIME_PERIODS = ((DAWN,u"Dawn"),
                    (EARLY_MORNING,u"Early Morning"),
                    (LATE_MORNING,u"Late Morning"),
                    (EARLY_AFTERNOON,u"Early Afternoon"),
                    (LATE_AFTERNOON,u"Late Afternoon"),
                    (EVENING,u"Evening"),
                    (NIGHT,u"Night"),
                    (LATE_NIGHT,u"Late Night"),
                    (WEE_HOURS,u"Wee Hours"))
    
    WALK = "W"
    PUBLIC_TRANS = "PT"
    CAR = "C"
    TRANSPORT = ((WALK,u"Walk"),
                 (PUBLIC_TRANS,u"Public Transport"),
                 (CAR,u"Car"))
    
    name = models.CharField(max_length=100)
    placeType = models.CharField(max_length=20, choices=PLACE_TYPES)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    time = models.CharField(max_length=20, choices=TIME_PERIODS)
    date = models.DateField()
    transportType = models.CharField(max_length=20, choices=TRANSPORT)
    #google maps place API placeID
    placeID = models.CharField(max_length=30)
    
    