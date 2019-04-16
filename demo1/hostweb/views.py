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
    resource_list = []
    cnt = 0
    for obj in ans:
        record = {}
        resource_ID = obj.resource_ID
        r1 = Resource.objects.get(resource_ID=resource_ID)
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

    try:
        u1.Type = 'E'
        u1.name  = form.name
        u1.introduction = form.intro
        u1.institute = form.institute
        u1.domain = form.domain
        u1.save()
        Author.objects.create()




































