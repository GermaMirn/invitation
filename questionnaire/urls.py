from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="request_form"),
    path('info', views.info, name="results")
]
