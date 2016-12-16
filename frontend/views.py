from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Showing home/landing page contents
def home(request) :
    template = loader.get_template('frontend/home.html')
    context = {
        'title': 'Python Bangladesh Community',
    }

    return HttpResponse(template.render(context, request))
