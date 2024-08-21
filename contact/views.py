from django.shortcuts import render
from .forms import ContactForm
from django.views import generic, View
from .models import ContactLink, About


class ContactView(View):
    def get(self, request):
        contacts = ContactLink.objects.all()
        form = ContactForm()
        return render(request, 'contact/contact.html', {'contacts': contacts, 'form': form})


class CreateContact(generic.CreateView):
    form_class = ContactForm
    success_url = '/'


class AboutView(View):
    def get(self, request):
        about = About.objects.last()
        return render(request, 'contact/about.html', {'about': about})
