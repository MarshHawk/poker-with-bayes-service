import graphene
from graphene_django import DjangoObjectType
from .models import Board, Player, PlayerScore

class PlayerType(DjangoObjectType):
    class Meta:
        model = Player

class PlayerByIdType(graphene.ObjectType):
    player = graphene.Field(PlayerType)
    hand = graphene.List(graphene.String)
    scores = graphene.List(graphene.Int)

class PlayerScoreType(DjangoObjectType):
    class Meta:
        model = PlayerScore

class BoardType(DjangoObjectType):
    class Meta:
        model = Board

class HandType(graphene.ObjectType):
    board = graphene.Field(BoardType)
    players = graphene.List(PlayerByIdType)
    river_player_scores = graphene.List(PlayerScoreType)
