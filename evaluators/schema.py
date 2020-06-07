import graphene
from bson.json_util import dumps
from evaluators.models import Hand
from .models import Board, Player, PlayerScore
from .types import HandType
from .mutations import Mutations

class Query(graphene.ObjectType):
    hands = graphene.List(HandType)

    def resolve_hands(self, info):
        return Hand.objects.all()

schema = graphene.Schema(query=Query, mutation=Mutations)
