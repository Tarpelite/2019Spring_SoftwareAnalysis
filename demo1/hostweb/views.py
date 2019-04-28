from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from hostweb.models import  *
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from hostweb.Se import *

json_config = {
    'ensure_ascii': False,
}

def User_list(request):

    if request.method == "GET":
        Users = User.objects.all()
        se = Userserializer(Users, many=True)
        return JsonResponse(se.data, safe=False, json_dumps_params=json_config)

def resource_list(request):

    if request.method == "GET":
        resouces = Resource.objects.all()
        se = ResourceSerializer(resouces, many=True)
        return JsonResponse(se.data, safe=False)

def login(request):

    username = request.GET.get('username')
    passwd = request.GET.get('passwd')
    is_expert = False
    status = True
    #print("{0}-{1}".format(username, passwd))
    try:
        user = User.objects.get(username=username, passwd=passwd)
        print(user)
        if user.is_expert():
            is_expert = True
        status = True
    except ObjectDoesNotExist:
        status = False

    result = {
        "status": status,
        "is_expert": is_expert,
    }

    return JsonResponse(result, json_dumps_params=json_config)

def register(request):

    username = request.GET.get('username')
    passwd = request.GET.get('passwd')
    telephone = request.GET.get('telephone')

    status = False
    ans = User.objects.filter(username = username)
    if len(ans) == 0:
        try:
            User.objects.create(username=username, passwd=passwd, telephone=telephone, Type="U")
            status = True
        except ObjectDoesNotExist:
            status = False

    result = {
        "status": status,
    }

    return JsonResponse(result, json_dumps_params=json_config)


@api_view(['GET'])
def index(request):

    '''
    return the main page
    :param request: json contains 1 field:username
    :return:
    '''

    if request.method == "GET":
        resouces = Resource.objects.all()
        se = ResourceSerializer(resouces, many=True)
        return JsonResponse(se.data, safe=False)


@api_view(['GET'])
def search(request):

    if request.method == "GET":
        keywords = request.GET.get('keywords')
        keywords = str(keywords).strip()
        #print(keywords)
        ans = Resource.objects.filter(title__contains=keywords)
        se = ResourceSerializer(ans, many=True)
        return JsonResponse(se.data, safe=False)

@api_view(['GET', 'PUT'])
def profile(request, pk):
    print(request.GET)
    try:
        user = User.objects.get(user_ID=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == "GET":
        se = Userserializer(user)
        return JsonResponse(se.data, safe=False)
    elif request.method == "PUT":
        print(request.data)
        se = Userserializer(user, data=request.data)
        if se.is_valid():
            se.save()
            return JsonResponse(se.data)
        return JsonResponse(se.errors, status=400)

@api_view(['POST', 'DELETE'])
def star(request, pk):
    if request.method == 'POST':
       data = request.data
       data["created_time"]=timezone.datetime.now() 
       serializer = starFormSerializer(data=request.data)
       if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
       return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        try:
            s1 = starForm.objects.get(form_ID=pk)
        except starForm.DoesNotExist:
            return HttpResponse(status=404)
        s1.delete()
        return HttpResponse(status=204)

@api_view(['GET'])
def my_collections(request, pk):
    ans = starForm.objects.filter(user_ID=pk)
    num = len(ans)
    resource_list = []
    cnt = 0
    for obj in ans:
        record = {}
        resource_ID = obj.resource_ID
        r1 = Resource.objects.get(resource_ID=resource_ID)
        record['resource_ID'] = resource_ID
        record['rank'] = cnt
        record['title'] = r1.title
        record['intro'] = r1.introduction
        record['price'] = r1.price
        record['authors'] = r1.authors
        record['url'] = r1.url
        cnt += 1
        resource_list.append(record)

        buyed_record = Resource.objects.filter(user_ID=u1, resource_ID=r1)
        if len(buyed_record) > 0:
            record["buyed"] = True
        else:
            record["buyed"] = False
    result = {
        "num": num,
        "resource_list": resource_list
    }

    return JsonResponse(result, json_dumps_params=json_config)


def my_account(request):

    username = request.GET.get('username')
    u1 = User.objects.get(username=username)
    result = {
        'balance': u1.balance,
    }
    return JsonResponse(result, json_dumps_params=json_config)


def buyed_resource(request):

    username = request.GET.get('username')
    u1 = User.objects.get(username=username)
    res = Transaction.objects.filter(user_ID=u1)
    resource_list = []
    cnt = 0
    for resource in res:
        record = {}
        r1 = Resource.objects.get(resource_ID=resource)
        record['rank'] = cnt
        cnt += 1
        record['title'] = r1.title
        record['type'] = r1.Type
        record['intro'] = r1.intro
        record['authors'] = r1.authors
        record['url'] = r1.url
        record['price'] = r1.price
        resource_list.append(record)

    result = {
        "num": cnt,
        "resouce_list": resource_list
    }

    return JsonResponse(result, json_dumps_params=json_config)



def expert_home(request):

    username = request.GET.get('username')
    u1 = User.objects.get(username=username)
    au1 = Author.objects.get(bind=u1)
    articles = []

    res = A2R.objects.filter(author_ID =au1)
    cnt = 0
    for item in res:
        record = {}
        r1 = Resource.objects.get(resource_ID=item.resource_ID)
        record['rank'] = cnt
        cnt += 1
        record['title'] = r1.title
        record['type'] = r1.Type
        record['intro'] = r1.intro
        record['authors'] = r1.authors
        record['url'] = r1.url
        record['price'] = r1.price
        articles.append(record)
        if cnt > 10:
            break

    result = {
        "num":cnt,
        "articles": articles,
        "name": au1.name,
        "institute": au1.institute,
        "domain": au1.domain,
        "citation_times": au1.citation_times,
        "article_numbers": au1.article_numbers,
        "h_index": au1.h_index,
        "g_index": au1.g_index,
    }

    return JsonResponse(result, json_dumps_params=json_config)


def add_item_list(request):

    resource_ID_list = request.GET.get("resource_ID_list")
    username = request.GET.get('username')
    u1 = User.objects.get(username=username)
    status = False
    try:
        for resource_ID in resource_ID_list:
            ItemCart.objects.create(user_ID = u1, resource_ID=resource_ID)
            status = True
    except ObjectDoesNotExist:
        status = False

    result = {
        "status":status,
    }

    return JsonResponse(result, json_dumps_params=json_config)


def remove_item_list(request):

    resource_ID_list = request.GET.get("resource_ID_list")
    username = request.GET.get('username')
    u1 = User.objects.get(username=username)
    status = False
    try:
        for resource_ID in resource_ID_list:
            item = ItemCart.objects.get(user_ID=u1, resource_ID=resource_ID)
            item.delete()
            status = True
    except ObjectDoesNotExist:
        status = False
    result = {
        "status": status,
    }

    return JsonResponse(result, json_dumps_params=json_config)


def item_cart(request):

    username = request.GET.get('username')
    u1 = User.objects.get(username=username)
    status = False
    res = ItemCart.objects.filter(user_ID=u1)
    cnt = 0
    item_list = []
    for item in res:
        record = {}
        r1 = Resource.objects.get(resource_ID=item.resource_ID)
        record['rank'] = cnt
        cnt += 1
        record['title'] = r1.title
        record['type'] = r1.Type
        record['intro'] = r1.intro
        record['authors'] = r1.authors
        record['url'] = r1.url
        record['price'] = r1.price
        item_list.append(record)

    result = {
        "num": cnt,
        "item_list": item_list
    }

    return JsonResponse(result, json_dumps_params=json_config)


def purchase(request):

    username = request.GET.get('username')
    item_list = request.GET.get('item_list')
    total_cost = request.GET.get('total_cost')
    u1 = User.objects.get(username=username)
    status = False

    if total_cost > u1.balance:
        staus = False
    else:
        try:
            for item in item_list:
                resouce_ID = item['resource_ID']
                Transaction.objects.create(user_ID=u1, resouce_ID=resouce_ID)
            u1.balance -= total_cost
            status = True
        except ObjectDoesNotExist:
            status = False

    result = {
        "status": status
    }

    return JsonResponse(result, json_dumps_params=json_config)


def apply_for_expert(request):

    username = request.GET.get('username')
    name = request.GET.get('name')
    sex = request.GET.get('sex')
    institute = request.GET.get('institute')
    domain = request.GET.get('domain')
    u1 = User.objects.get(username=username)
    try:
        U2E_apply_form.objects.create(user_ID=u1,
                                      approved=False,
                                      name=name,
                                      sex=sex,
                                      institute=institute,
                                      domain = domain,
                                      )
        status = True
    except ObjectDoesNotExist:
        status = False

    result = {
        "status": status
    }

    return JsonResponse(result, json_dumps_params=json_config)


def has_published(request):

    username = request.GET.get('username')
    u1 = User.objects.get(username=username)
    item_list = []
    cnt = 0
    if u1.author_ID:
        res = A2R.objects.filter(user_ID=u1)
        for item in res:
            record = {}
            r1 = Resource.objects.get(resource_ID=item.resource_ID)
            record['rank'] = cnt
            cnt += 1
            record['title'] = r1.title
            record['type'] = r1.Type
            record['intro'] = r1.intro
            record['authors'] = r1.authors
            record['url'] = r1.url
            record['price'] = r1.price
            item_list.append(record)

    result = {
        "cnt": cnt,
        "item_list": item_list
    }

    return JsonResponse(result, json_dumps_params=json_config)


def publish_item_application(request):

    cnt = 0
    item_list = []
    try:
        ans = publish_item_application_form.objects.filter(passed=False)
        for item in ans:
            record = {}
            record['rank'] = cnt
            cnt += 1
            record['applicant'] = Author.objects.get(item.author_ID).name
            record['title'] = item.title
            record['intro'] = item.intro
            item_list.append(record)
            status = True
    except ObjectDoesNotExist:
        status = False

    result = {
        "num": cnt,
        "item_list": item_list
    }

    return JsonResponse(result, json_dumps_params=json_config)


def U2E_pass(request):

    username = request.GET.get("username")
    u1 = User.objects.get(username=username)
    form = U2E_apply_form.objects.get(user_ID=u1)
    status = False
    try:
        u1.Type = 'E'
        u1.name = form.name
        u1.introduction = form.intro
        u1.institute = form.institute
        u1.domain = form.domain
        u1.save()
        Author.objects.create(name=form.name,
                              sex='M',
                              institute=form.institute,
                              domain=form.domain,
                              bind=u1)
        form.delete()
    except ObjectDoesNotExist:
        status = False

    result = {
        "status": status
    }

    return JsonResponse(result, json_dumps_params=json_config)


def PUB_pass(request):

    username = request.GET.get("username")
    u1 = User.objects.get(username=username)
    f_ID = request.GET.get("")
    form = publish_item_application_form.get(f_ID=f_ID)
    status = False

    try:
        Resource.objects.create(title = form.title,
                                authors = form.authors,
                                intro = form.intro,
                                url = form.url,
                                price = form.price,
                                Type = form.Type)
        form.passed = True
        form.save()

    except ObjectDoesNotExist:
        status = True

    result = {
        "status":status
    }

    return JsonResponse(result, json_dumps_params=json_config)






































