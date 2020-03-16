import graphene
from bson.json_util import dumps
from evaluators.models import Hand
from .models import Board, Player, PlayerScore
from .types import HandType
from .mutations import Mutations

class Query(graphene.ObjectType):
    all_hands = graphene.List(HandType)
    hand = graphene.Field(HandType,
                              id=graphene.Int())

    def all_hands(self, info):
        return Hand.objects.mongo_find({},{'_id': False})

schema = graphene.Schema(query=Query, mutation=Mutations)
