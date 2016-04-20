from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

import subprocess
import os, sys

from related_company import write_related_company

from mainapp.models import ArticleTable, CompanyTable

def index(request):

    my_target = request.GET.get("search-company")
    if my_target:
        raw_news_list = ArticleTable.objects.filter(target__contains=my_target)
        write_related_company(my_target)
        if not raw_news_list:
            process = subprocess.Popen(['/home/vagrant/.virtualenvs/FYPENV/bin/python', '/home/vagrant/FYP/crawling.py'], 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.STDOUT)
        my_target = "News for %s" % my_target
    else:
        raw_news_list = ArticleTable.objects.all()
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
        news.content = news.content.replace("\n", "\n\n");

    return render(request, 'test.html', {"news_list": news_list, "company_list": company_list, "target": my_target})
    
def chart(request):

    return render(request, 'test2.html')