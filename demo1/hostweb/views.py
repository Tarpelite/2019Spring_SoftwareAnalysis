from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from hostweb.models import  *
from django.core.exceptions import ObjectDoesNotExist
import json
# Create your views here.

json_config={
    'ensure_ascii':False,
}




def login(request):

    username = request.GET.get('username')
    passwd = request.GET.get('password')
    is_expert = "0"
    status = "1"

    try:
        user = User.objects.get(username=username, passwd=passwd)
        if user.is_expert():
            is_expert = "1"
        status = "1"
    except ObjectDoesNotExist:
        status = "0"

    result = {
        "status": status,
        "is_expert": is_expert,
    }

    return JsonResponse(result, json_dumps_params=json_config)

def register(request):

    username = request.GET.get('username')
    passwd = request.GET.get('passwd')
    telephone = request.GET.get('telephone')

    status = "0"
    ans = User.objects.filter(username = username)
    if len(ans)  == 0:
     User.objects.create(username=username, passwd=passwd, telephone=telephone, Type="U")
     status = "1"

    result = {
        "status": status,
    }

    return JsonResponse(result, json_dumps_params=json_config)


def index(request):

    '''
    return the main page
    :param request: json contains 1 field:username
    :return:
    '''

    username = request.GET.get('username')
    ans = User.objects.get(username=username)
    avatar_url = ans.avatar_url





