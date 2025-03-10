from django.conf import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def success(request):
    request.session[settings.BASKET_SESSION_ID] = {}
    return HttpResponse("payment completed")


def fail(request):
    return HttpResponse("payment failed")
