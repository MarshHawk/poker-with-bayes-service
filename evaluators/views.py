from django.shortcuts import render
from bson.json_util import dumps
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from evaluators.models import Hand, Some
from evaluators.game import deal
from evaluators.serializers import SomeSerializer

# Create your views here.

@api_view(['POST'])
def create(request):
    hand = deal()
    hand.save()
    return Response(Hand.objects.mongo_find_one({"_id": hand._id},{'_id': False}))

@api_view(['GET'])
def create(request): 
    hand = Hand.objects.all()[0]
    return Response(Hand.objects.mongo_find_one({},{'_id': False}), content_type=('Content-Type', 'application/json'))
