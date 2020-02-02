import math
import random
from .models import Player, Board, Hand, PlayerById

cards = ['Ac','Ad','Ah','As','2c','2d','2h','2s','3c','3d','3h','3s','4c','4d','4h','4s','5c','5d','5h','5s','6c','6d','6h','6s','7c','7d','7h','7s','8c','8d','8h','8s','9c','9d','9h','9s','Tc','Td','Th','Ts','Jc','Jd','Jh','Js','Qc','Qd','Qh','Qs','Kc','Kd','Kh','Ks']

def shuffle():
    sample = cards[:]
    for (i, x) in enumerate(cards):
        rand = math.floor((i + 1) * random.uniform(0, 1))
        temp = sample[i]
        sample[i] = sample[rand]
        sample[rand] = temp
    return sample

def gen_next_index():
  index = 0
  yield index
  while (True):
      index+=1
      yield index

def deal():
    negs = Player(uuid=uuid.uuid4(), name="Danieal Negraunu")
    ivy = Player(uuid=uuid.uuid4(), name="Phil Ivey")
    ant = Player(uuid=uuid.uuid4(), name="Patrick Antonius")
    helm = Player(uuid=uuid.uuid4(), name="Phil Helmuth")
    players = [negs, ivy, ant, helm]
    cards = shuffle()
    players_by_id = []
    nextn = gen_next_index()
    i = 0
    pl = len(players)
    for p in players:
        i = next(nextn)
        player_hand = hand=[cards[i],cards[i+len(players)]]
        pbi = PlayerById(player=p, hand=player_hand)
        players_by_id.append(pbi)
    flop=[cards[next(nextn)+pl], cards[next(nextn)+pl], cards[next(nextn)+pl]]
    turn=cards[next(nextn)+pl]
    river=cards[next(nextn)+pl]
    board = Board(flop=flop, turn=turn, river=river)
    return Hand(players=players_by_id, board=board)

