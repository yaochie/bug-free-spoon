from django.shortcuts import redirect, render_to_response
from django.views import generic
from django.template import RequestContext

from django.forms import formset_factory
from .forms import PreTripItineraryForm, HotelForm

# Create your views here.
def create_itin(request):
    HotelFormSet = formset_factory(HotelForm, min_num=0, extra=1)
    PreTripItineraryFormSet = formset_factory(PreTripItineraryForm, min_num=1,
                                              extra=2)
    if request.method == 'POST':
        attract_formset = PreTripItineraryFormSet(request.POST,
                                                  prefix='attractions')
        hotel_formset = HotelFormSet(request.POST, prefix='hotels')
        
        if attract_formset.is_valid() and hotel_formset.is_valid():
            for form in attract_formset.forms:
                print(form.cleaned_data['place'])
            return redirect('/maketrip/save_success')
    else:
        attract_formset = PreTripItineraryFormSet(prefix='attractions')
        hotel_formset = HotelFormSet(prefix='hotels')
        
    return render_to_response('maketrip/pretrip_itin.html',
                              {'att_formset': attract_formset, 'hot_formset':
                              hotel_formset},
                              context_instance=RequestContext(request))

    
class SaveSuccess(generic.DetailView):
    template_name = "polls/save_success.html"
    
    def get_queryset(self):
        pass