from django.urls import path

from api import views

urlpatterns = [
    path("", views.HomePage.as_view(), name="home-page"),
]
