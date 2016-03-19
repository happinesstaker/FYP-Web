from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from mainapp.models import ArticleTable

def index(request):

    news_list = ArticleTable.objects.filter(source='NYT')
    title_list = [x.title for x in news_list]

    return render(request, 'test.html', {"news_list": title_list})