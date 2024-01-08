from collections import defaultdict
from operator import attrgetter


class Player:
	def __init__(self):
		self.hand = []

	def clear(self):
		self.hand = []

	def draw(self, card):
		self.hand.append(card)
		self.hand.sort()

	def play(self, valid_moves):
		raise NotImplementedError

	def chose_color(self):
		raise NotImplementedError

	def print_hand(self):
		print(", ".join(str(card) for card in self.hand))


class Von(Player):
	def play(self, valid_moves):
		color_counts = defaultdict(int)
		for card in self.hand:
			color_counts[card.color] += 1

		largest_color = max(color_counts, key=color_counts.get)

		for card in valid_moves:
			if card.color == largest_color:
				self.hand.remove(card)
				return card

		self.hand.remove(valid_moves[0])
		return valid_moves[0]

	def chose_color(self):
		color_counts = defaultdict(int)
		for card in self.hand:
			color_counts[card.color] += 1

		return max(color_counts, key=color_counts.get)


def get_moves(top, hand, chosen_color):
	valid = []

	for card in hand:
		if card.color is None:
			if card.type == "wild" or not valid:
				valid.append(card)
		elif card.type == top.type:
			valid.append(card)
		elif top.color:
			if card.color == top.color:
				valid.append(card)
		elif chosen_color == card.color:
			valid.append(card)

	return valid
