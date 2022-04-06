"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self,*args, **kwargs):
        context = super(Home, self).get_context_data(*args,**kwargs)
        context['title'] = 'Home Page'
        context['year'] = datetime.now().year
        return context


class Contact(TemplateView):
    template_name = 'app/contact.html'

    def get_context_data(self,*args, **kwargs):
        context = super(Contact, self).get_context_data(*args,**kwargs)
        context['title'] = 'Contacto'
        context['message'] = 'Your contact page'
        context['year'] = datetime.now().year
        return context


class About(TemplateView):
    template_name = 'app/about.html'

    def get_context_data(self,*args, **kwargs):
        context = super(About, self).get_context_data(*args,**kwargs)
        context['title'] = 'About'
        context['message'] = 'Your aplication description page page'
        context['year'] = datetime.now().year
        return context
