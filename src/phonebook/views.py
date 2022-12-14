from django.views.generic import TemplateView, CreateView, DeleteView
from django.urls import reverse_lazy
from . import forms
from . import models

class HomePageView(TemplateView):
    template_name = 'phonebook/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['persones'] = models.Persona.objects.all()
        return context

class AddPhoneFormView(CreateView):
    template_name = 'phonebook/add_persone.html'
    form_class = forms.CreatePersoneFrom
    success_url = reverse_lazy('home')
    
    def get_success_url(self) -> str:
        phone_numbers = self.request.POST.get('phones')
        for phone_number in phone_numbers.split():
            models.Phone.objects.create(phone = phone_number, contack =self.object)
        return super().get_success_url()

class DelPhoneview(DeleteView):
    model = models.Persona
    template_name = 'phonebook/delete_persone.html'
    success_url = reverse_lazy('home')

