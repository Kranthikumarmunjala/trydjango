
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

#create your views here
def article_search_view(request):
    #print(dir(request))
    print(request.GET)
    query_dict=dict(request.GET)
    #query=query_dict.get("q")

    try:
        query=int(query_dict.get("q"))
    except:
        query=None
    article_obj=None
    if query is not None:
        article_obj=Article.objects.get(id=query)
    context={
        "object": article_obj
    }
    return render(request,"articles/search.html", context=context)

def article_create_view(request, id=None):
    context={}
    return render(request, "articles/create.html",
    context=context)


def article_detail_view(request):
    article_obj=None
    if id is not None:
        article_obj=Article.objects.get(id=id)
    context={
        "object":article_obj,
    }
    return render(request, "articles/detail.html",
    context=context)
