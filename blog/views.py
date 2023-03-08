import profile

from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from .models import *
# Create your views here.
"""class IndexPage(TemplateView): 
    template_name = "index.html"""

class IndexPage(TemplateView):
    def get(self, request, **kwargs):
        article_data = []
        all_articles = Article.objects. all()[:9]

        for article in all_articles:
            article_data.append({
                'title': article.title,
                'cover': article.cover.url,# is image used url
                'category': article.category.title,# category is object so used title
                'created_at': article.created_at.date(),
            })

        promote_data = []
        all_promote_article = Article.objects.filter(promote=True).order_by('created_at')
        for promote in all_promote_article:
            
            promote_data.append({
                'title': promote.title,
                'category': promote.category.title,
                'cover': promote.cover.url if promote.cover else None,
                #'author': promote.author.user.first_name[0]  + ' ' + promote.author.user.last_name[0], # for many to many
                #'author': User.objects.filter(id = promote.author.user.id)[:1] , # for many to many
                #'avatar': promote.author.avatar.url if  promote.author.avatar else None, # for many to many
                'created_at': promote.created_at.date(),
            })

        context = {
            'article_data' : article_data,
            'promote_article_data' :promote_data,
            'name_fave' : 'amin :)',
        }

        return render(request, 'index.html', context)

class ContactPage(TemplateView):
    template_name = 'page-contact.html'

class IndexPageTT(TemplateView):
    template_name = "tt/index1.html"


class AllArticleAPIView(APIView):
    def get(self, request, format=None):
        try:
            data = []
            all_Article = Article.objects.all().order_by('-created_at')
            for article in all_Article:
                data.append({
                    'title': article.title,
                    'cover': article.cover.url if article.cover else None,
                    'category': article.category.title, #serializable dont object
                    'created_at': article.created_at.date(),
                    'promote': article.promote
                })
            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'status': 'INTERNAL_SERVER_ERROR We\'ll later'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SingleArticleAPIview(APIView):
    def get(self, request, format=None):
        try:
            article_title = request.GET['article_title']
            articles = Article.objects.filter(title__contains=article_title)
            serializerd_data = serializers.SingleArticleSerializer(articles, many=True)
            data = serializerd_data.data

            return Response({'data':data}, status=status.HTTP_200_OK)

        except:
            return Response({'status':' Internal Eerver Error'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SearchArticleAPIview(APIView):
    def get(self, request, format=None):
        try:
            from django.db.models import Q
            query = request.GET['query']
            articels = Article.objects.filter(Q(contact__icontains=query))
            data = serializers.SingleArticleSerializer(articels, many=True).data
            return Response({'data':data}, status=status.HTTP_200_OK)
        except:
            return Response({'status': ' Internal Eerver Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SubmitArticleAPIview(APIView):
    def post(self, request, format=None):
        try:
            serializer = serializers.SubmitArticleSerializer(data=request.data)
            if serializer.is_valid():
                title = serializer.data.get('title')
                cover = request.FILES['cover']
                contact = serializer.data.get('contact')
                category_id = serializer.data.get('category_id')
                author_id = serializer.data.get('author_id')
                promote = serializer.data.get('promote')
            else:
                return Response({'status':'Bad Request'},status= status.HTTP_400_BAD_REQUEST)

            user = User.objects.get(id=author_id)
            author = UserProfile.objects.get(user=user)

            category = Category.objects.get(id=category_id)

            article = Article()
            article.title = title
            article.cover = cover
            article.contact = contact
            article.category = category
            article.promote = promote

            article.save()

            article.author.add(author)
            return Response({'status':'OK Save'} ,status=status.HTTP_200_OK)

        except:
            return Response({'status':'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)






















