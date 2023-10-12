from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article
import random
# Create your views here.

#HTML_STRING="""
#<h1>Hello World</h1>
#"""


def home_view(request,*args, **kwargs):
    """
    Take in a request (Django sends request)
    Return HTML as a response (we pick to return the response)
    """
    name="shiva"           #hard coded
    random_id=random.randint(1, 4)

    #from the databases?
    article_obj=Article.objects.get(id=random_id)
    article_queryset=Article.objects.all()

    context={
        "object_list":article_queryset,
        "object":article_obj,
        "title":article_obj.title,
        "id":article_obj.id,
        "content":article_obj.content
    }
    #django templates
    HTML_STRING=render_to_string("home-view.html",
    context=context)
    #H1_STRING = """
    #<h1> {title} (id: {id})!</h1>
    #<p>{content}!</p>
    #""".format(**context)

    return HttpResponse(HTML_STRING)
