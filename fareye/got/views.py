# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView
from django.shortcuts import render , redirect
from .models import Battles, King
import requests

class KidsDetailView(DetailView):
    """View to handle form rendering and update for question additon."""

    model = Battles
    template_name = 'kingslist.html'

    def get_context_data(self):
        context = {}
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        Battles.objects.values('attacker_king').distinct()
        return render(
            request, self.template_name, context)

class KingsListView(ListView):
    model = Battles
    template_name = 'kingslist.html'

    def get_context_data(self):
        context = {}
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        page = request.GET.get('page') if request.GET.get('page') else 0
        r = requests.get('http://localhost:8000/api/v1/kings-list/?page='+str(page))
        context = r.json()
        context['count'] = King.objects.all().count()
        return render(
            request, self.template_name, context)