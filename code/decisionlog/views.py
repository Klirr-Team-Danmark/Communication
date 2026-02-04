from django.shortcuts import render
from django.views.generic import ListView

from django.shortcuts import redirect
from django.urls import reverse

from datetime import datetime

from decisionlog.models import DecisionLogEntry

from decisionlog.forms import DecisionLogEntryForm


# Create your views here.
class DecisionLogListView(ListView):
    """Shows the list of entries in the decision log.

    Also allows users who are logged in to add new entries."""

    template_name = "list.html"
    model = DecisionLogEntry

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["form"] = DecisionLogEntryForm

        return context

    def post(self, request, *args, **kwargs):
        # Only users who are logged in can add entries to the decision log
        if not self.request.user.is_anonymous:
            req = request.POST
            now = datetime.now()
            username = self.request.user.username
            content = req["content"]
            DecisionLogEntry.objects.create(
                author=username, content=content, created_time=now
            )

        return redirect(reverse("decision_log"))
