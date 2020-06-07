# poker-with-bayes-service
a poker with Bayes service

```
query {
  hands {
			board {
				flop
				turn
				river
			}
  }
}

mutation createHand {
	createHand {
		hand {
			board {
				flop
				turn
				river
			}
			players {
				hand
				player {
					uuid
					name
				}
			}
			riverPlayerScores {
				playerUuid
				score
				description
			}
		}
	}
}
```

### docker
```
docker run -d -p 27017-27019:27017-27019 --name mongodb mongo
```

### python
```
python manage.py migrate

```