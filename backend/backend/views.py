import json
import uuid

from django.http import JsonResponse
import os
import random

from django.views.decorators.csrf import csrf_exempt

from backend.models import Response
from backend.settings import STATIC_ROOT

BATCH_SIZE = 10


def list_folders(request, start_index):
    out = {}
    if start_index == 0:
        out['session'] = uuid.uuid4()
    files = sorted(os.listdir(os.path.join(STATIC_ROOT, 'data')))
    out['total_files'] = len(files)
    if start_index >= len(files):
        return JsonResponse({'files': []})
    files = files[start_index:min(start_index + BATCH_SIZE, len(files))]
    out['files'] = files
    return JsonResponse(out)


@csrf_exempt
def response(request, dirname):
    body = json.loads(request.body)
    result = body['result']
    session = body['session']
    Response.objects.create(dir=dirname, choice=result, session=session)
    return JsonResponse({})


def results(request):
    return JsonResponse({'results': list(Response.objects.all().values())})
