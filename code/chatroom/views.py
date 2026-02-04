from django.views.generic import ListView, TemplateView, View, CreateView
from .models import Message

class Join(TemplateView):
    template_name = "join.html"


class Main(ListView):
    template_name = "chat.html"
    model = Message

    def get_queryset(self):
        qs = reversed(Message.objects.all()[:50])

        return qs

    # Technically superfluous currently
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class SendMessage(CreateView):
    template_name = "message_list.html"
    model = Message
    fields = ["author", "content"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["object_list"] = reversed(Message.objects.all()[:50])

        return context

    # def form_valid(self, form):
    def post(self, request, *args, **kwargs):
        content = request.POST["content"]
        author = request.POST["author"]

        # Handle saving of data
        #super().post(request, *args, **kwargs)

        Message.objects.create(author=author, content=content)
        response = self.get(request, *args, **kwargs)

        return response
