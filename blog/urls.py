from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name="index"),
    path('tt', views.IndexPage.as_view(), name="index1"),
]