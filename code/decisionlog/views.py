from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from decisionlog.models import DecisionLogEntry

# Create your views here.
class DecisionLogListView(ListView):
    template_name = "list.html"
    model = DecisionLogEntry
