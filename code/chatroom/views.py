from django.views.generic import DetailView, ListView, TemplateView, View
from .models import Message
from .forms import MessageForm

class Main(ListView):
    template_name = "chat.html"
    model = Message

    def get_queryset(self):
        qs = Message.objects.all()[:50]

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = MessageForm()

        return context

