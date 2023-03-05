from django.shortcuts import render
from django.views.generic import TemplateView
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
