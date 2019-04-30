from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from . import models

# region Constants
RES_SUCCESS = 0
RES_FAILURE = 1
RES_BAD_REQUEST = -1


# Create your views here.

def user_exists(username):
    return models.Participant.objects.filter(username=username).exists()


def is_user_valid(username, password):
    if user_exists(username):
        user = models.Participant.objects.get(username=username)
        return user.password == password
    return False


@csrf_exempt
@require_http_methods(['POST'])
def register_api(request):
    req_body = request.body.decode('utf-8')
    json_body = json.loads(req_body)
    if 'username' in json_body and 'password' in json_body:
        username = json_body['username']
        password = json_body['password']

        if user_exists(username):
            return JsonResponse(data={
                'result': RES_FAILURE, 'reason': 'username is taken'
            })
        else:
            new_participant = models.Participant(username=username, password=password)
            new_participant.save()
            return JsonResponse(data={'result': RES_SUCCESS})
    else:
        return JsonResponse(data={'result': RES_BAD_REQUEST, 'reason': 'either of username or password was not passed as a POST argument!'})


@csrf_exempt
@require_http_methods(['POST'])
def login_api(request):
    req_body = request.body.decode('utf-8')
    json_body = json.loads(req_body)
    if 'username' in json_body and 'password' in json_body:
        if is_user_valid(json_body['username'], json_body['password']):
            return JsonResponse(data={'result': RES_SUCCESS})
        else:
            return JsonResponse(data={
                'result': RES_FAILURE, 'reason': 'wrong credentials passed'
            })
    return JsonResponse(data={'result': RES_BAD_REQUEST, 'reason': 'Username or Password was not passed as a POST argument!'})


