from django import forms
from django.forms import formset_factory

class MealForm(forms.Form):
    meals = [("B", u"Breakfast"), ("BR", u"Brunch"), ("L", u"Lunch"),
             ("T", u"Tea"), ("D", u"Dinner"), ("S", u"Suppper"),
             ("SN", u"Snack")]
    lengths = [("10M",u"10 minutes"), ("30M",u"30 minutes"), ("1H",u"1 hour"),
               ("2H",u"2 hours"), ("3H",u"3 hours"), ("4H",u"4 hours"),
               ("5H",u"5 hours"), ("6H",u"6 hours"), ("7H",u"7+ hours")]
    travelOptions = [(1,u"Walk"), (2,u"Bus/Tram"), (3,u"Car"), (4,u"Train"),
                     (5,u"Plane")]
                     
    mealType = forms.ChoiceField(meals, label="Meal")
    name = forms.CharField(max_length=100)
    time = forms.ChoiceField(lengths)
    travel = forms.ChoiceField(travelOptions, label="Arrived Via")
    desc = forms.CharField(max_length=300, widget=forms.widgets.Textarea,
                           label="Description")

class PreTripItineraryForm(forms.Form):
    lengths = [("10M",u"10 minutes"), ("30M",u"30 minutes"), ("1H",u"1 hour"),
               ("2H",u"2 hours"), ("3H",u"3 hours"), ("4H",u"4 hours"),
               ("5H",u"5 hours"), ("6H",u"6 hours"), ("7H",u"7+ hours")]
    travelOptions = [(1,u"Walk"), (2,u"Bus/Tram"), (3,u"Car"), (4,u"Train"),
                     (5,u"Plane")]
    placeName = forms.CharField(max_length=100, label="Name")
    time = forms.ChoiceField(lengths)
    travel = forms.ChoiceField(travelOptions)
    
class AttractionForm(forms.Form):
    travelOptions = [(1,u"Walk"), (2,u"Bus/Tram"), (3,u"Car"), (4,u"Train"),
                     (5,u"Plane")]
    lengths = [("10M",u"10 minutes"), ("30M",u"30 minutes"), ("1H",u"1 hour"),
               ("2H",u"2 hours"), ("3H",u"3 hours"), ("4H",u"4 hours"),
               ("5H",u"5 hours"), ("6H",u"6 hours"), ("7H",u"7+ hours")]
               
    placeName = forms.CharField(max_length=100, label="Attraction Name")
    time = forms.ChoiceField(lengths, label="Time to spend")
    travel = forms.ChoiceField(travelOptions, label="Arrived Via")
    
class HotelForm(forms.Form):
    travelOptions = [(1,u"Walk"), (2,u"Bus/Tram"), (3,u"Car"), (4,u"Train"),
                     (5,u"Plane")]
    name = forms.CharField(max_length=150, label="Hotel Name")
    travel = forms.ChoiceField(travelOptions, label="Arrived Via")
    #startDate = forms.DateField(label="Start:")
    #endDate = forms.DateField(label="End:")