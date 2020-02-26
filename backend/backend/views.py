import json

from django.http import JsonResponse
import os
import random

from django.views.decorators.csrf import csrf_exempt

from backend.models import Response
from backend.settings import STATIC_ROOT

BATCH_SIZE = 30


def list_folders(request):
    files = os.listdir(os.path.join(STATIC_ROOT, 'data'))
    files = random.sample(files, min(BATCH_SIZE, len(files)))
    return JsonResponse({'files': files})


@csrf_exempt
def response(request, dirname):
    result = json.loads(request.body)['result']
    Response.objects.create(dir=dirname, choice=result)
    return JsonResponse({})


def results(request):
    return JsonResponse({'results': list(Response.objects.all().values())})
