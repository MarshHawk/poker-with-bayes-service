from django.shortcuts import render
from bson.json_util import dumps
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from evaluators.models import Hand
from evaluators.game import deal

# Create your views here.

@api_view(['POST'])
def create(request):
    hand = deal()
    hand.save()
    return Response(Hand.objects.mongo_find_one({"_id": hand._id},{'_id': False}))

@api_view(['GET'])
def get_all_hands(request):
    return Response(Hand.objects.mongo_find({},{'_id': False}))