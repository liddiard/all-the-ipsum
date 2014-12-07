import re
import json
import urllib
import urllib2

from bs4 import BeautifulSoup

from django.http import HttpResponse, Http404
from django.views.generic.base import View, TemplateView


API_URL = "http://en.wikiquote.org/w/api.php?"


# views

class FrontView(TemplateView):
    template_name = 'front.html'


# abstract base classes

class AjaxView(View):

    def json_response(self, **kwargs):
        return HttpResponse(json.dumps(kwargs), content_type="application/json")

    def success(self, **kwargs):
        return self.json_response(result=0, **kwargs)

    def error(self, error_type, message):
        return self.json_response(result=1, error=error_type, message=message)

    def authentication_error(self):
        return self.error("AuthenticationError", "User is not authenticated.")

    def access_error(self, message):
        return self.error("AccessError", message)

    def key_error(self, message):
        return self.error("KeyError", message)

    def does_not_exist(self, message):
        return self.error("DoesNotExist", message)

    def validation_error(self, message):
        return self.error("ValidationError", message)


# api

class GenerateIpsumView(AjaxView):

    def get(self, request):
        page = request.GET['page']
        num_words = request.GET['words']
        params = urllib.urlencode({
            'format': 'json',
            'action': 'parse',
            'pageid': page
        })
        page_text = urllib2.urlopen(API_URL + params).read()
        soup = BeautifulSoup(page_text)
        lines = []
        for tag in soup.find_all('dd'):
            text = tag.get_text()
            cleaned = re.sub(r'(^.*: )|(\[.*\])', "", text)
            lines.append(cleaned)
        return self.success(page=page, words=num_words, lines=lines)
