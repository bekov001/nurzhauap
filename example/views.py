from django.shortcuts import render
from django.views.generic import TemplateView
from main.models import *


def page_not_found_view(request, exception):
    context = {
        'page_title': "404"
    }
    return render(request, 'ERROR/index.html', status=404)


def server_error(request):
    context = {
        'page_title': "500"
    }
    return render(request, 'ERROR/index.html', context)


class SitemapXmlView(TemplateView):
    template_name = 'search/sitemap.xml'
    content_type = "application/xml"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.order_by("-id")
        context['categories'] = Category.objects.order_by("-id")
        context['profiles'] = Profile.objects.order_by("-id")
        return context

