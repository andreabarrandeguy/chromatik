from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("outputh/", views.outputh, name="outputh"),
    path("outputv/", views.outputv, name="outputv"),
    path("test/", views.test, name="test")
]