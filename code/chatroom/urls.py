from chatroom import views

from django.urls import path

urlpatterns = [
    path("", views.Join.as_view(), name="chat_join"),
    path("chat/", views.Main.as_view(), name="chat_index"),
    path("post/", views.SendMessage.as_view(), name="chat_post"),
]
