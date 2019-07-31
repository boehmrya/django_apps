# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect, render
from django.contrib.messages import success
from django.views.generic import View
from .forms import ContactForm

class ContactView(View):
    form_class = ContactForm
    template_name = 'contact/contact_form.html'

    def get(self, request):
        return render(request,
                    self.template_name,
                    {'form': self.form_class()})
