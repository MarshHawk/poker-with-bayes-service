from django.utils.timezone import now

import graphene

from .models import Hand
from .types import HandType
from evaluators.game import deal

class CreateHand(graphene.Mutation):

    class Arguments:
        pass

    hand = graphene.Field(HandType)
    def mutate(self, info):
        hand = deal()
        hand.save()
        return CreateHand(hand=hand)

class Mutations(graphene.ObjectType):
    create_hand = CreateHand.Field()
