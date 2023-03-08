from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name="index"),
    path('contact/', views.ContactPage.as_view(), name="contact"),
    path('tt/', views.IndexPageTT.as_view(), name="index1"),

    path('article/all/', views.AllArticleAPIView.as_view(), name="all_article"),
    path('singleArticle/', views.SingleArticleAPIview.as_view(), name="single_article"),
    path('article/search/', views.SearchArticleAPIview.as_view(), name="search_article"),
    path('article/submit/', views.SubmitArticleAPIview.as_view(), name="submit_article"),
]