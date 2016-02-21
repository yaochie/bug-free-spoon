from django.db import models

# Create your models here.
class Hotels(models.Model):
    parent = models.ForeignKey('Itinerary')
    WALK = 'w'
    PUBLIC_TRANS = 'p'
    CAR = 'c'
    MED_TRANS = 'm'
    LONG_TRANS = 'l'
    TRANSPORT = ((WALK,u"Walk"),
                 (PUBLIC_TRANS,u"Bus/Tram"),
                 (CAR,u"Car"),
                 (MED_TRANS,u"Train"),
                 (LONG_TRANS,u"Plane"))
                 
    YES = 'y'
    NO = 'n'
    RECOM = ((YES,u"yes"),
             (NO,u"no"))
    name = models.CharField(max_length=50)
    travel = models.CharField(max_length=20, choices=TRANSPORT)
    recom = models.TextField(max_length=10, choices=RECOM)

class Meals(models.Model):
    parent = models.ForeignKey('Itinerary')
    
    WALK = 'w'
    PUBLIC_TRANS = 'p'
    CAR = 'c'
    MED_TRANS = 'm'
    LONG_TRANS = 'l'
    TRANSPORT = ((WALK,u"Walk"),
                 (PUBLIC_TRANS,u"Bus/Tram"),
                 (CAR,u"Car"),
                 (MED_TRANS,u"Train"),
                 (LONG_TRANS,u"Plane"))
                 
    m10 = 'a'
    m30 = 'b'
    h1 = 'c'
    h2 = 'd'
    h3 = 'e'
    h4 = 'f'
    h5 = 'g'
    h6 = 'h'
    h7 = 'i'
    TIMES = ((m10,u"10 minutes"),
             (m30,u"30 minutes"),
             (h1,u"1 hour"),
             (h2,u"2 hours"),
             (h3,u"3 hours"),
             (h4,U"4 hours"),
             (h5,U"5 hours"),
             (h6,U"6 hours"),
             (h7,U"7+ hours"))
             
    YES = 'y'
    NO = 'n'
    RECOM = ((YES,u"yes"),
             (NO,u"no"))
             
    BFAST = 'b'
    LUNCH = 'l'
    TEA = 't'
    DINNER = 'd'
    SUPPER = 's'
    SNACK = 'n'
    FOODTYPES = ((BFAST,u"Breakfast"),
                 (LUNCH,u"Lunch"),
                 (TEA,u"Tea"),
                 (DINNER,u"Dinner"),
                 (SUPPER,u"Supper"),
                 (SNACK,U"Snack"))
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=FOODTYPES)
    time = models.CharField(max_length=20, choices=TIMES)
    travel = models.CharField(max_length=20, choices=TRANSPORT)
    desc = models.CharField(max_length=200)
    recomm = models.TextField(max_length=10, choices=RECOM)

class Attrs(models.Model):
    parent = models.ForeignKey('Itinerary')
    
    WALK = 'w'
    PUBLIC_TRANS = 'p'
    CAR = 'c'
    MED_TRANS = 'm'
    LONG_TRANS = 'l'
    TRANSPORT = ((WALK,u"Walk"),
                 (PUBLIC_TRANS,u"Bus/Tram"),
                 (CAR,u"Car"),
                 (MED_TRANS,u"Train"),
                 (LONG_TRANS,u"Plane"))
                 
    m10 = 'a'
    m30 = 'b'
    h1 = 'c'
    h2 = 'd'
    h3 = 'e'
    h4 = 'f'
    h5 = 'g'
    h6 = 'h'
    h7 = 'i'
    TIMES = ((m10,u"10 minutes"),
             (m30,u"30 minutes"),
             (h1,u"1 hour"),
             (h2,u"2 hours"),
             (h3,u"3 hours"),
             (h4,U"4 hours"),
             (h5,U"5 hours"),
             (h6,U"6 hours"),
             (h7,U"7+ hours"))
    name = models.CharField(max_length=50)
    time = models.CharField(max_length=20, choices=TIMES)
    travel = models.CharField(max_length=20, choices=TRANSPORT)


class Itinerary(models.Model):

    pass
    
    
'''
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
                 (PUBLIC_TRANS,u"Bus/Tram"),
                 (CAR,u"Car"),
                 (MED_TRANS,u"Train"),
                 (LONG_TRANS,u"Plane"))
                 
    RECOM = ((YES,u"yes"),
             (NO,u"no"))
             
    TIMES = ((BFAST,u"Breakfast"),
             (LUNCH,u"Lunch"),
             (TEA,u"Tea"),
             (DINNER,u"Dinner"),
             (SUPPER,u"Supper"),
             (SNACK,U"Snack"))
             
    FOODTYPES = ((BFAST,u"Breakfast"),
                 (LUNCH,u"Lunch"),
                 (TEA,u"Tea"),
                 (DINNER,u"Dinner"),
                 (SUPPER,u"Supper"),
                 (SNACK,U"Snack"))
    
    name = models.CharField(max_length=100)
    placeType = models.CharField(max_length=20, choices=PLACE_TYPES)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    time = models.CharField(max_length=20, choices=TIME_PERIODS)
    date = models.DateField()
    transportType = models.CharField(max_length=20, choices=TRANSPORT)
    #google maps place API placeID
    placeID = models.CharField(max_length=30)
 '''   
    