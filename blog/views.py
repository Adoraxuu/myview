from datetime import date
from django.views.generic import TemplateView

from django.template.response import TemplateResponse

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def example_view(request, arg, **kwargs):
    kwargs['today'] = date.today()
    return TemplateResponse(request, 'blog/example.html', { 'arg': arg, **kwargs })

def example_view_2(request, arg, **kwargs):
    kwargs['today'] = date.today()
    return HttpResponse(f'example 2 {arg}, today is { kwargs["today"] }')

def example_view_3(request, my_arg, **kwargs):
    kwargs['today'] = date.today()
    template = loader.get_template('blog/example3.html')
    context = {
        'my_arg': my_arg,
        **kwargs
    }
    return HttpResponse(template.render(context, request))

def example_view_4(request, arg, **kwargs):
    kwargs['today'] = date.today()
    return render(request, 'blog/example4.html', {'arg': arg, **kwargs})

def example_view_5(request, arg, **kwargs):
    kwargs['today'] = date.today()
    return TemplateResponse(request, 'example5.html', {'arg': arg, **kwargs})

class HomeView(TemplateView):
    template_name = "blog/index.html"

    def get_context_data(self, arg, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = date.today()
        context['arg'] = arg
        return context
    
