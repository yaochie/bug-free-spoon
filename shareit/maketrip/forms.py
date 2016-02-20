from django import forms
from django.forms import formset_factory

class PreTripItineraryForm(forms.Form):
    periods = [(1,u"Dawn"), (2,u"Early Morning"), (3,u"Late Morning"),
               (4,u"Early Afternoon"), (5,u"Late Afternoon"), (6,u"Evening"),
               (7,u"Night"), (8,u"Late Night"), (9,u"Wee Hours")]
    travelOptions = [(1,u"Walk"), (2,u"Bus/Tram"), (3,u"Car"), (4,u"Train"),
                     (5,u"Plane")]
    place = forms.CharField(max_length=100)
    time = forms.ChoiceField(periods)
    travel = forms.ChoiceField(travelOptions)
    
PreTripItineraryFormSet = formset_factory(PreTripItineraryForm, min_num=1,
                                          extra=2)