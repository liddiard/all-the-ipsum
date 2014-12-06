from django.views.generic.base import TemplateView


class FrontView(TemplateView):
    template_name = 'front.html'
