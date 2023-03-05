from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name="index"),
    path('contact/', views.ContactPage.as_view(), name="contact"),

    path('tt/', views.IndexPageTT.as_view(), name="index1"),

]