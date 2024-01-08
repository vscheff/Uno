from deck import Deck
from players import get_moves, Player, Von
from random import shuffle


VERBOSE_MODE = True
GAMES = 1
players = [Von() for _ in range(4)]

def main():
	for _ in range(GAMES):
		deck = Deck()

		for _ in range(7):
			for player in players:
				player.draw(deck.draw())

		shuffle(players)

		if VERBOSE_MODE:
			print("Starting hands:")
			for i in range(len(players)):
				print(f"Player {i}: ", end='')
				players[i].print_hand()
			print()

		turn = len(players) - 1
		turn_mod = 1
		chosen_color = None

		deck.flip_top()

		if VERBOSE_MODE:
			print(f"Starting with {deck.top}")

		while True:
			turn = get_next_turn(turn, turn_mod)
			current_player = players[turn]

			if not (valid_moves := get_moves(deck.top, current_player.hand, chosen_color)):
				drawn = deck.draw()

				if VERBOSE_MODE:
						print(f"Player {turn} draws {drawn}")

				if not (valid_moves := get_moves(deck.top, [drawn], chosen_color)):
					current_player.draw(drawn)
					
					continue
				
				played_card = drawn
			else:
				played_card = current_player.play(valid_moves)

			if VERBOSE_MODE:
				print(f"Player {turn} plays {played_card}")

			if not current_player.hand:
				if VERBOSE_MODE:
					print(f"\nPlayer {turn} wins!")

				break

			if played_card.type == "skip":
				turn = get_next_turn(turn, turn_mod)
			elif played_card.type == "reverse":
				turn_mod *= -1
			elif played_card.type == "draw2":
				next_player = get_next_turn(turn, turn_mod)

				for _ in range(2):
					players[next_player].draw(deck.draw())

				turn = get_next_turn(turn, turn_mod)
			elif played_card.type == "wild":
				chosen_color = player.chose_color()

				if VERBOSE_MODE:
					print(f"\tPlayer {turn} chose {chosen_color}")
			elif played_card.type == "wild+4":
				chosen_color = player.chose_color()

				if VERBOSE_MODE:
					print(f"\tPlayer {turn} chose {chosen_color}")

				next_player = get_next_turn(turn, turn_mod)

				for _ in range(4):
					players[next_player].draw(deck.draw())

				turn = get_next_turn(turn, turn_mod)

			deck.play(played_card)

def get_next_turn(turn, turn_mod):
	turn += turn_mod

	if turn == -1:
		return len(players) - 1

	return turn % len(players)


if __name__ == "__main__":
	main()