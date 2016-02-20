from django.shortcuts import redirect, render_to_response
from .forms import PreTripItineraryForm
from django.views.generic.edit import FormView
from django.views import generic
from django.http import HttpResponseRedirect
from django.template import RequestContext

# Create your views here.
class PreTripItineraryView(FormView):
    template_name = 'pretrip_itin.html'
    
    def form_valid(self, form):
        pass
    
def create_itin(request):
    form = PreTripItineraryForm(request.POST or None)
    if form.is_valid():
        for place in form.answers():
            print(place)
        return redirect("save_success")
        
    return render_to_response('maketrip/pretrip_itin.html', {'form': form},
                              context_instance=RequestContext(request))
    
class SaveSuccess(generic.DetailView):
    template_name = "polls/save_success.html"