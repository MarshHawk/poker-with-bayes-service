from djongo import models
import uuid
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Player(models.Model):
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()

    class Meta:
        abstract = True
        
    def __str__(self):
        return self.name

class PlayerById(models.Model):
    player = models.EmbeddedModelField(
        model_container=Player
    )
    hand = ArrayField(models.CharField(max_length=2), size=2)
    #score = models.IntegerField(default=0)
    class Meta:
        abstract = True

class Board(models.Model):
    flop = ArrayField(models.CharField(max_length=2), size=3)
    turn = models.CharField(max_length=2)
    river = models.CharField(max_length=2)
    class Meta:
        abstract = True

class Hand(models.Model):
    _id = models.ObjectIdField()

    players = models.ArrayModelField(
        model_container=PlayerById,
    )

    board = models.EmbeddedModelField(
        model_container=Board
    )

    objects = models.DjongoManager()
    #TODO: scores = ArrayField(models.CharField(max_length=3, min_length=3), size=3)
    #TODO: all_player_ids and players_by_id, normalized,

class Some(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()

    