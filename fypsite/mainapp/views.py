from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from mainapp.models import ArticleTable, CompanyTable, SelectedArticleTable

from related_company import write_related_company

import subprocess
import os, sys

PYTHON_PATH = '/home/vagrant/.virtualenvs/FYPENV/bin/python'
CRAWLER_PATH = '/home/vagrant/FYP/crawling.py'

def index(request):

    my_target = request.GET.get("search-company")

    if my_target:

        # change target company to user's target (call related company extension)
        write_related_company(my_target)

        # select from processed article table
        raw_news_list = SelectedArticleTable.objects.filter(target__contains=my_target)

        # similarity comparison processed not available, select raw article table as second choice
        if not raw_news_list:
            raw_news_list = ArticleTable.objects.filter(target__contains=my_target)

        # not any company news available in database, initiate an immediate crawling process (resource intensive)
        # Python path and crawling script path are HARD CODED
        if not raw_news_list:
            process = subprocess.Popen([PYTHON_PATH, CRAWLER_PATH],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)

        # string to show in webpage
        my_target = "News for %s" % my_target

    else:

        # select all latest news in database
        raw_news_list = SelectedArticleTable.objects.all()

        if not raw_news_list:
            raw_news_list = ArticleTable.objects.all()

        # string to show in webpage
        my_target = "Latest News"


    company_list = CompanyTable.objects.all()
    paginator = Paginator(raw_news_list, 15)

    page_num = request.GET.get('page',1)

    try:
        news_list = paginator.page(page_num)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news_list = paginator.page(paginator.num_pages)

    for news in news_list:
        if news.content=="" or news.content=="\n":
            news.content = "No available detail, check original page...\n\n"
            continue
            
        # Replace \n with double \n, to let template in django to automatically seperate paragraphs
        news.content = news.content.replace("\n", "\n\n");

    return render(request, 'index.html', {"news_list": news_list, "company_list": company_list, "target": my_target})

def chart(request):

    # TODO: this shows detailed chart for a company, finally decided not to implement it.
    return render(request, 'chart.html')