from django.urls import path

from decisionlog.views import DecisionLogListView

urlpatterns = [
    path("",DecisionLogListView.as_view(), name="decision_log")
]
