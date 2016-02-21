from django.shortcuts import redirect, render_to_response
from django.views import generic
from django.template import RequestContext

from django.forms import formset_factory
from .forms import PreTripItineraryForm, HotelForm, MealForm, AttractionForm
from django.views.generic.edit import FormView

# Create your views here.
def create_itin(request):
    HotelFormSet = formset_factory(HotelForm, min_num=0, extra=1)
    PreTripItineraryFormSet = formset_factory(PreTripItineraryForm, min_num=1,
                                              extra=2)
    MealFormSet = formset_factory(MealForm)
    AttractionFormSet = formset_factory(AttractionForm)
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

class Itin():
    def __init__(self):
        self.formList = [[AttractionForm()],
                         [AttractionForm()],
                         [AttractionForm()],
                         [AttractionForm()],
                         [AttractionForm()]]
        self.current = 0
        
    def all_valid(self):
        forms_valid = True
        for form in self.formList:
            forms_valid &= form.is_valid()
        return forms_valid
        
    def create_itin(self, request):
        if request.method == 'POST':
            if request.POST['action']:
                #TODO: Stop and give message if too many forms added.
                if len(self.formList) > 10:
                    pass
                else:
                    if request.POST['action'] == "hotel":
                        self.formList[self.current].append(HotelForm())
                    elif request.POST['action'] == "attr":
                        self.formList[self.current].append(AttractionForm())
                    elif request.POST['action'] == "meal":
                        self.formList[self.current].append(MealForm())
                    elif request.POST['action'] == "0":
                        self.current = 0
                    elif request.POST['action'] == "1":
                        self.current = 1
                    elif request.POST['action'] == "2":
                        self.current = 2
                    elif request.POST['action'] == "3":
                        self.current = 3
                    elif request.POST['action'] == "4":
                        self.current = 4
            else:
                #validate and send info
                if self.all_valid():
                    pass
                
        return render_to_response('maketrip/pretrip_itin3.html',
                                  {'forms': self.formList[self.current]},
                                  context_instance=RequestContext(request))

a = Itin()
                                  
def create_itin_ext(request):
    global a
    return a.create_itin(request)
                                 
class SaveSuccess(generic.DetailView):
    template_name = "maketrip/save_success.html"
    
    def get_queryset(self):
        pass
        
    def get_object(self):
        pass