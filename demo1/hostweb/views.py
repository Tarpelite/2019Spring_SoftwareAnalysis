# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from hostweb.models import  *
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
import json
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from hostweb.Se import *
import hashlib
import uuid

json_config = {
    'ensure_ascii': False,
}

@api_view(['GET'])
def User_list(request):

    if request.method == "GET":
        Users = User.objects.all()
        se = Userserializer(Users, many=True)
        return JsonResponse(se.data, safe=False, json_dumps_params=json_config)

def resource_list(request):

    if request.method == "GET":
        resources = Resource.objects.all()
        se = ResourceSerializer(resources, many=True)
        return JsonResponse(se.data, safe=False)

def login(request):

    username = request.GET.get('username')
    passwd = request.GET.get('passwd')
    is_expert = False
    status = True
    error_msg = ""
    #print("{0}-{1}".format(username, passwd))
    try:
        user = User.objects.get(username=username)
        
         # print(user)
        if user.is_expert():
            is_expert = True
        if user.passwd == passwd:
            status = True
        else:
            status = False
            error_msg = "密码错误"
    except ObjectDoesNotExist:
        status = False
        error_msg = "用户名不存在"

    try:
        url = user.avator.url
    except Exception as e:
        url = ""

    result = {
        "status": status,
        "is_expert": is_expert,
        "user_ID":user.user_ID,
        "avator_url":url
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
    :return: jsonresponse
    '''

    if request.method == "GET":
        resouces = Resource.objects.all()
        se = ResourceSerializer(resouces, many=True)
        return JsonResponse(se.data, safe=False)


@cache_page(15*60)
@api_view(['GET'])
def search(request, pk):
    '''
    return search results list

    params:pk: user_ID

    '''

    if request.method == "GET":
        keywords = request.GET.get('keywords')
        keywords = str(keywords).strip()
        #print(keywords)
        ans = Resource.objects.filter(title__contains=keywords)
        resource_list = []
        cnt = 0
        for obj in ans:
            author_IDs = []
            record = {}
            resource_ID = obj.resource_ID
            r1 = Resource.objects.get(resource_ID=resource_ID)
            record['resource_ID'] = resource_ID
            record['rank'] = cnt
            record['title'] = r1.title
            record['intro'] = r1.intro
            record['price'] = r1.price
            record['authors'] = r1.authors
            record['url'] = r1.url
            record['Type'] = r1.Type
            aus = r1.authors.split(",")
            for au in aus:
                res_dict = {}
                res_dict['name'] = au 
                try:
                    ids = Author.objects.get(name=au)
                    res_dict['author_ID'] = ids.author_ID
                except Author.DoesNotExist:
                    res_dict['author_ID'] = -1 
                author_IDs.append(res_dict)
            record['author_IDs'] = author_IDs    
            cnt += 1
            is_star = starForm.objects.filter(user_ID=pk, resource_ID=resource_ID)
            if len(is_star)> 0:
                is_star = True
            else:
                is_star = False
            record['is_star'] = is_star
            resource_list.append(record)
        return JsonResponse(resource_list, safe=False)

@api_view(['GET', 'PUT'])
def profile(request, pk):
    #print(request.GET)
    try:
        user = User.objects.get(user_ID=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == "GET":
        se = Userserializer(user)
        return JsonResponse(se.data, safe=False)
    elif request.method == "PUT":
        #print(request.data)
        se = Userserializer(user, data=request.data)
        if se.is_valid():
            se.save()
            return JsonResponse(se.data)
        return JsonResponse(se.errors, status=400)

@api_view(['PUT'])
def expert_profile_edit(request, pk):
    if request.method == 'PUT':
        try:
            au1 = Author.objects.get(author_ID=pk)
            data = request.data 
            au1.sex = request.data['sex']
            au1.name = request.data['name']
            au1.institute = request.data['institute']
            au1.domain = request.data['domain']
            au1.save()
        except Author.DoesNotExist:
            return HttpResponse(status=404)
        return HttpResponse(status=200)


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
            u1 = User.objects.get(user_ID=pk)
            r_ids = request.data['resource_ID']
            for r_id in r_ids:
                r1 = Resource.objects.get(resource_ID=r_id)
                s1 = starForm.objects.get(user_ID=u1, resource_ID=r1)
                s1.delete()
        except starForm.DoesNotExist:
            return HttpResponse(status=404)
        return HttpResponse(status=204)


@cache_page(15*60)
@api_view(['GET'])
def my_collections(request, pk):
    u1 = User.objects.get(user_ID=pk)
    ans = starForm.objects.filter(user_ID=pk)
    num = len(ans)
    resource_list = [] 
    cnt = 0
    for obj in ans:
        author_IDs = []
        record = {}
        r1 = obj.resource_ID
        #r1 = Resource.objects.get(resource_ID=resource_ID)
        record['resource_ID'] = r1.resource_ID
        record['rank'] = cnt
        record['title'] = r1.title
        record['intro'] = r1.intro
        record['price'] = r1.price
        record['authors'] = r1.authors
        record['url'] = r1.url
        aus = r1.authors.split(",")
        for au in aus:
           res_dict = {}
           res_dict['name'] = au
           try:
                ids = Author.objects.get(name=au)
                res_dict['author_ID'] = ids.author_ID
           except Author.DoesNotExist:
               res_dict['author_ID'] = -1 
           author_IDs.append(res_dict) 
        record['author_IDs']= author_IDs  
        cnt += 1
        resource_list.append(record)

        buyed_record = Transaction.objects.filter(user_ID=u1, resource_ID=r1)
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

@api_view(['GET'])
def buyed_resource(request, pk):

    u1 = User.objects.get(user_ID=pk)
    res = Transaction.objects.filter(user_ID=u1)
    resource_list = []
    cnt = 0
    for trans in res:
        author_IDs = []
        record = {}
        r1 = trans.resource_ID
        record['rank'] = cnt
        cnt += 1
        record['title'] = r1.title
        record['type'] = r1.Type
        record['intro'] = r1.intro
        record['authors'] = r1.authors
        record['url'] = r1.url
        record['price'] = r1.price
        aus = r1.authors.split(",")
        for au in aus:
           res_dict = {}
           res_dict['name'] = au
           try:
                ids = Author.objects.get(name=au)
                res_dict['author_ID'] = ids.author_ID
           except Author.DoesNotExist:
               res_dict['author_ID'] = -1 
           author_IDs.append(res_dict) 
        record['author_IDs'] = author_IDs      
        resource_list.append(record)

    result = {
        "num": cnt,
        "resouce_list": resource_list
    }

    return JsonResponse(result, json_dumps_params=json_config)

@api_view(['GET'])
def expert_relation_draw(request, pk):
    result = {}
    try:
        au1 = Author.objects.get(author_ID=pk)
    except Author.DoesNotExist:
        return HttpResponse(status=404)
    nodes = []
    name_list = [] 
    links = []
    au_pool = A2A.objects.filter(author1 = au1)
    main_node = {
        'name':au1.name,
        'symbol':'star'
    }
    nodes.append(main_node)
    for a2a in au_pool:
        au2 = a2a.author2
        if au2.name not in name_list:
            name_list.append(au2.name)
        link = {
            "source":au1.name,
            "target":au2.name,
            "weight":1,
            "name":"coworker"
        }
        links.append(link)

        au3_pool = A2A.objects.filter(author1 = au2)
        for a2a3 in au3_pool:
            au3  = a2a3.author2
            if au3.name in name_list:
                link = {
                    "source":au2.name,
                    "target":au3.name,
                    "weight":1,
                    "name":"coworker"
                }
                links.append(link)
    for name in name_list:
        node = {
            'name':name
        }
        nodes.append(node)
    result = {
        "nodes":nodes,
        "links":links
    }
    return JsonResponse(result, status = 200)

        


@api_view(['GET'])
def expert_home(request, pk):

    au1 = Author.objects.get(author_ID=pk)
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
    
    try:
        url = au1.avator.url
    except Exception as e:
        url = ""
    

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
        "avator": url
    }

    return JsonResponse(result, json_dumps_params=json_config)

@api_view(['POST', 'DELETE', 'GET'])
def add_item_list(request, pk):

    if request.method == "POST":
        resource_ID_list = request.data["item_list"]
        user = User.objects.get(user_ID=pk)

        status = False
        try:
            for resource_ID in resource_ID_list:
                r = Resource.objects.get(resource_ID=resource_ID)
                ItemCart.objects.create(user_ID = user, resource_ID=r)
                status = True
        except ObjectDoesNotExist:
            status = False

        result = {
            "status":status,
        }

        return JsonResponse(result, json_dumps_params=json_config)
    
    elif request.method == "DELETE":
       resource_ID_list = request.data["item_list"]
       user = User.objects.get(user_ID=pk)
       status = False

       for resource_ID in resource_ID_list:
               try:
                    r = Resource.objects.get(resource_ID=resource_ID)
                    item = ItemCart.objects.get(user_ID = user, resource_ID=r)
               except ItemCart.DoesNotExist:
                   print(resource_ID)
                   return HttpResponse(status=404)
               item.delete()
       status  = True
       result = {
            "status":status,
        } 
       return JsonResponse(result, json_dumps_params=json_config) 

@api_view(['GET'])
def item_cart(request, pk):

    status = False
    res = ItemCart.objects.filter(user_ID=pk)
    cnt = 0
    item_list = []
    for item in res:
        author_IDs = []
        record = {}
        r1 = item.resource_ID
        record['resource_ID'] = r1.resource_ID
        #r1 = Resource.objects.get(resource_ID=item.resource_ID.resource_ID)
        record['rank'] = cnt
        cnt += 1
        record['title'] = r1.title
        record['type'] = r1.Type
        record['intro'] = r1.intro
        record['authors'] = r1.authors
        record['type'] = r1.Type
        aus = r1.authors.split(",")
        print(aus)
        for au in aus:
           res_dict = {}
           res_dict['name'] = au
           try:
                ids = Author.objects.get(name=au)
                res_dict['author_ID'] = ids.author_ID
           except Author.DoesNotExist:
               res_dict['author_ID'] = -1 
           author_IDs.append(res_dict)          

        record['url'] = r1.url
        record['price'] = r1.price
        record['author_IDs'] = author_IDs
        item_list.append(record)

    result = {
        "num": cnt,
        "item_list": item_list
    }

    return JsonResponse(result, json_dumps_params=json_config)

@api_view(['GET', 'POST'])
def purchase(request, pk):
    if request.method == 'POST':
        item_list = request.data['item_list']
        total_cost = request.data['total_cost']
        u1 = User.objects.get(user_ID = pk)
        status = False

        if total_cost > u1.balance:
            staus = False
        else:
            try:
                for item in item_list:
                    resource_ID = Resource.objects.get(resource_ID=item)
                    Transaction.objects.create(user_ID=u1, resource_ID=resource_ID, created_time=timezone.now())
                    i1 = ItemCart.objects.get(user_ID=u1, resource_ID=resource_ID)
                    i1.delete()
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

@api_view(['GET', 'POST'])
def publish_item_application(request, pk):
    '''
        GET：获取该作者发布过的资源列表
            params:pk:用户ID
            return:cnt:资源总数
                   item_list:资源列表

        POST：发布资源
            params:pk:用户ID
            return:status：True表示发布成功，False表示发布失败
    '''
    if request.method == 'GET':
        u1 = User.objects.get(user_ID = pk)
        item_list = []
        cnt = 0
        if u1.is_expert():
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

    elif request.method == 'POST':
        data = request.data
        title = data['title']
        authors = data['authors']
        intro = data['intro']
        price = data['price']
        Type = data['Type']
        publisher = data['publisher']
        publish_date = data['publish_date']
        agency = data['agency']
        patent_number = data['patent_number']
        patent_application_number = data['patent_application_number']
        file = request.FILES.get("file")
        try:
            Resource.objects.create(
                title = title,
                authors = authors,
                intro = intro,
                price = price,
                Type = Type,
                publisher = publisher,
                publish_date = publish_date,
                agency = agency,
                patent_number = patent_number,
                patent_application_number = patent_application_number,
                file = file
            )
        except Exception as e:
            result = {
                "status":False
            }
            return JsonResponse(result, status=500)
        
        result = {
            "status":True,
        }

        return JsonResponse(result, status = 201, json_dumps_params=json_config)


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


@api_view(['GET', 'POST'])
def user_avator(request, pk):
    if request.method == 'GET':
        u1 = User.objects.get(user_ID=pk)
        try:
            avator = u1.avator.path
            avator_list = list(avator.split("\\"))
            avator = "user_avator/" + avator_list[-1]
        except Exception as e:
            avator = "user_avator/default.jpg"
        result = {
            'avator':avator
        }
        return JsonResponse(result)
    elif request.method == 'POST':
        data = request.data
        data = data['File']
        #uuid_name = uuid.uuid4().hex
        u1 = User.objects.get(user_ID=pk)
        u1.avator = data
        
        try:
            u1.save()
            return HttpResponse(status = 200)
        except Exception as e:
            return HttpResponse(status = 404)

@api_view(['GET', 'POST'])
def author_avator(request, pk):
    if request.method == 'GET':
        u1 = Author.objects.get(author_ID=pk)
        try:
            avator = u1.avator.path
            avator_list = list(avator.split("\\"))
            avator = "author_avator/" + avator_list[-1]
        except Exception as e:
            avator = "author_avator/default.jpg"
        result = {
            'avator':avator
        }
        return JsonResponse(result)
    elif request.method == 'POST':
        data = request.data
        data = data['File']
        print(type(data))
        #uuid_name = uuid.uuid4().hex
        u1 = User.objects.get(user_ID=pk)
        u1.avator = data
        
        try:
            u1.save()
            return HttpResponse(status = 200)
        except Exception as e:
            return HttpResponse(status = 404)









































