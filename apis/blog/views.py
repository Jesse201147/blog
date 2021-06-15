import json

from django.http import HttpResponse
from rest_framework.decorators import api_view
from utils.returns import return_fail,return_succeed
from blog.models import ArticlePost


@api_view(["GET", "POST"])
def get_article(request):
    article = ArticlePost.objects.all()
    return return_succeed(data=[i.to_dict() for i in article])
