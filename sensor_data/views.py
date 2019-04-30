from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from user.models import Participant
import json
from . import models
from django.views.decorators.csrf import csrf_exempt
from user.views import RES_SUCCESS
from user.views import RES_FAILURE
from user.views import RES_BAD_REQUEST


# Create your views here.
def user_exists(username):
    return Participant.objects.filter(username=username).exists()


def is_user_valid(username, password):
    if user_exists(username):
        user = Participant.objects.get(username=username)
        return user.password == password
    return False


@csrf_exempt
@require_http_methods(['POST'])
def submit_api(request):
    req_body = request.body.decode('utf-8')
    json_body = json.loads(req_body)
    if 'username' in json_body and 'password' in json_body and is_user_valid(json_body['username'], json_body['password']):
        username = json_body['username']
        sensor_id = json_body['sensor_id']
        timestamp = json_body['timestamp']
        accuracy = json_body['accuracy']
        data = json_body['data']
        device = json_body['device']

        # Select whichever user you want to (any of these work)
        participant = Participant.objects.get(username=username)

        new_raw_data = models.Data(username=participant, sensor_id=sensor_id, timestamp=timestamp, accuracy=accuracy, data=data, device=device)
        new_raw_data.save()
        return JsonResponse(data={'result': RES_SUCCESS})
    else:
        return JsonResponse(data={'result': RES_BAD_REQUEST})

