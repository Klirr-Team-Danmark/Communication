from django.views.generic import DetailView, ListView, RedirectView, TemplateView, View

class Main(TemplateView):
    template_name = "index.html"

class Login(TemplateView):
    template_name = "login.html"
