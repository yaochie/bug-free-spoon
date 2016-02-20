from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.create_itin, name='plan_itinerary_form'),
    url(r'^save_success', views.SaveSuccess.as_view(), name='success'),
]