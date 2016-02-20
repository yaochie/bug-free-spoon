from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.
class ItineraryListView(ListView):
    template_name = 'showtrip/view_itinerary.html'
    
    def get_queryset(self):
        pass