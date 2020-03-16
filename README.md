# poker-with-bayes-service
a poker with Bayes service

```
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
