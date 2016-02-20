from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ItineraryListView.as_view(), name='disp_itinerary'),
]