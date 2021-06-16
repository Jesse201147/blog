import json

from django.http import HttpResponse
from rest_framework.decorators import api_view
from utils.returns import return_fail, return_succeed
from blog.models import ArticlePost


@api_view(["GET", ])
def get_article_list(request):
    article = ArticlePost.objects.all()
    return return_succeed(data=[i.to_dict() for i in article])


@api_view(["GET", ])
def get_article(request, article_id):
    article = ArticlePost.objects.get(id=article_id)
    print(article)
    return return_succeed(data=article.to_dict())
