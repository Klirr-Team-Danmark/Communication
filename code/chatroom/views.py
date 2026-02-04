from django.views.generic import ListView, TemplateView, View, CreateView
from .models import Message
from .forms import MessageForm

class Join(TemplateView):
    template_name = "join.html"


class Main(ListView):
    template_name = "chat.html"
    model = Message

    def get_queryset(self):
        qs = reversed(Message.objects.all()[:50])

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = MessageForm()

        return context


class SendMessage(CreateView):
    template_name = "chat.html"
    model = Message

    def get_queryset(self):
        qs = Message.objects.all()[:50]

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = MessageForm()

        return context
