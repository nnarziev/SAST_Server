from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from . import models


# Create your views here.
@csrf_exempt
@require_http_methods(['POST'])
def register_api(request):
    req = json.loads(request.body.decode('utf-8'))
    if models.Participant.objects.filter(username=req['username']).exists():
        return JsonResponse(data={
            'result': 'fail',
            'reason': 'username is taken'
        })
    else:
        new_participant = models.Participant(username=req['username'], password=req['password'])
        new_participant.save()
        return JsonResponse(data={
            'result': 'success'
        })
