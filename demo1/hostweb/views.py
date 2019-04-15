from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from hostweb.models import  *
from django.utils import timezone
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
    result = {
        "avatar_url": avatar_url,
        "news_cnt": 2,
        "news": [{
            "rank": 0,
            "title": "article_1",
            "url": "#",
            "author": "au1",
            "author_url": "au2",
        }, {
            "rank": 1,
            "title": "article_2",
            "url": "#",
            "author":"au2",
            "author_url": "au3",
        }],
        "ranking_cnt": 2,
        "ranking_list": [{
            "rank": 0,
            "title": "title1",
            "title_url": "title_url",
        }, {
            "rank": 1,
            "title": "title2",
            "title_url": "title_url",
        }]

    }
    return JsonResponse(result, json_dumps_params=json_config)


def search(request):
    keywords = request.GET.get('keywords')
    result = {
        "num": 0,
        "article_list":[]

    }
    return JsonResponse(result, json_dumps_params=json_config)


def profile(request):
    username = request.GET.get('username')
    user = User.objects.get(username=username)

    query_ans = U2E_apply_form.objects.filter(user_ID = user.user_ID)
    status = False
    if len(query_ans) > 0:
        status = True

    result = {
        "user_ID":user.user_ID,
        "username": username,
        "telephone": user.telephone,
        "email": user.mail,
        "is_expert": user.is_expert(),
        "intro": user.introduction,
        "domain": user.domain,
        "institute": user.institute,
        "is_applying": status

    }

    return JsonResponse(result, json_dumps_params=json_config)


def profile_edit(request):

    user_ID = request.POST.get('user_ID')
    user = User.objects.get(user_ID=user_ID)
    status = False
    try:
        user.username = request.POST.get('username')
        user.telephone = request.POST.get('telephone')
        user.mail = request.POST.get('email')
        user.institute = request.POST.get('institute')
        user.introduction = request.POST.get('intro')
        user.name = request.POST.get('username')
        user.domain = request.POST.get('domain')
        status = True
    except ObjectDoesNotExist:
        status = False

    result = {
        "status": status
    }

    return JsonResponse(result, json_dumps_params=json_config)

def star(request):

    username = request.GET.get("username")
    resource_ID = request.GET.get("resource_ID")

    u1 = User.objects.get(username=username)
    r1 = Resource.objects.get(resource_ID=resource_ID)

    try:
        starForm.objects.create(user_ID = u1, resource_ID=r1)
        status = True
    except ObjectDoesNotExist:
        status = False

    result = {
        "status":status
    }
    return JsonResponse(result, json_dumps_params=json_config)


def unstar(request):

    username = request.GET.get("username")
    resource_ID = request.GET.get("resource_ID")

    u1 = User.objects.get(username=username)
    r1 = Resource.objects.get(resource_ID=resource_ID)

    try:
        res = starForm.objects.filter(user_ID = u1, resource_ID=r1)
        for obj in res:
            obj.delete()
        status = True
    except ObjectDoesNotExist:
        status = False

    result = {
        "status": status
    }

    return JsonResponse(result, json_dumps_params=json_config)

def my_collections(request):

    username = request.GET.get("username")

    u1 = User.objects.get(username=username)

    ans = starForm.objects.filter(user_ID=u1)

    num = len(ans)



















