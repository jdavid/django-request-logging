from django.conf.urls import url
from django.http import HttpResponse
from django.views import View
from request_logging.decorators import no_logging


def general_resource(request):
    return HttpResponse(status=200, body='Generic repsonse entity')

class TestView(View):
    @no_logging()
    def post(self, request):
        return HttpResponse(status=200)


@no_logging()
def view_func(request):
    return HttpResponse(status=200, body="view_func with no logging")


@no_logging('Custom message')
def view_msg(request):
    return HttpResponse(status=200, body="view_msg with no logging with a custom reason why")


@no_logging('Empty response body')
def dont_log_empty_response_body(request):
    return HttpResponse(status=201)


urlpatterns = [
    url(r'^somewhere$', general_resource),
    url(r'^test_class$', TestView.as_view()),
    url(r'^test_func$', view_func),
    url(r'^test_msg$', view_msg),
    url(r'^dont_log_empty_response_body', dont_log_empty_response_body),
]
