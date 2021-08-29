from django.http import HttpResponse
import pymongo
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def insert(request):
    shopclient = pymongo.MongoClient("mongodb://localhost:27017/")
    shopdb = shopclient["shopdatabase"]
    shopcol = shopdb["products"]
    product = json.loads(request.body.decode())
    x = shopcol.insert_one(product)
    return HttpResponse(x.inserted_id)

@csrf_exempt
def insert_array(request):
    shopclient = pymongo.MongoClient("mongodb://localhost:27017/")
    shopdb = shopclient["shopdatabase"]
    shopcol = shopdb["products"]
    products = json.loads(request.body.decode())
    x = shopcol.insert_many(products)
    print(request.body.decode())
    return HttpResponse(request.body.decode())

@csrf_exempt
def find_by_id(requset):
    shopclient = pymongo.MongoClient("mongodb://localhost:27017/")
    shopdb = shopclient["shopdatabase"]
    shopcol = shopdb["products"]
    product_id = int(requset.body.decode())
    shopquery = {"ID": product_id}
    shopdoc = shopcol.find(shopquery, {'_id': 0, 'ID': 0})
    print(shopdoc)
    return HttpResponse(shopdoc)


@csrf_exempt
def sort_by_name(request):
    shopclient = pymongo.MongoClient("mongodb://localhost:27017/")
    shopdb = shopclient["shopdatabase"]
    shopcol = shopdb["products"]
    shopdoc = shopcol.find({}, {'ID': 1, 'name': 1}).sort("name")
    answer = []
    for x in shopdoc:
        print(x)
        answer.append(x)
    return HttpResponse(answer)


@csrf_exempt
def sort_by_param(request):
    shopclient = pymongo.MongoClient("mongodb://localhost:27017/")
    shopdb = shopclient["shopdatabase"]
    shopcol = shopdb["products"]
    param = request.body.decode()
    shopdoc = shopcol.find({}, {'ID': 1, 'name': 1}).sort("params." + param)
    comeback = []
    print(type(shopdoc))
    for x in shopdoc:
        comeback.append(x)
        print(x)
    return HttpResponse(comeback)
