from chatroom import views

from django.urls import include, path

urlpatterns = [
    path("", views.Main.as_view(), name="chat_index"),
]
