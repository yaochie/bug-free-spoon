from django.shortcuts import redirect, render_to_response
from .forms import PreTripItineraryFormSet 
from django.views.generic.edit import FormView
from django.views import generic
from django.template import RequestContext

# Create your views here.
def create_itin(request):
    if request.method == 'POST':
        print("hi")
        formset = PreTripItineraryFormSet(request.POST)
        if formset.is_valid():
            for form in formset.forms:
                print(form.cleaned_data['place'])
            return redirect("save_success")
    else:
        formset = PreTripItineraryFormSet()
        
    return render_to_response('maketrip/pretrip_itin.html', {'formset': formset},
                              #{'formset': formset, 'empty': formset.empty_form},
                              context_instance=RequestContext(request))
    
#def add_form():
    
    
class SaveSuccess(generic.DetailView):
    template_name = "polls/save_success.html"