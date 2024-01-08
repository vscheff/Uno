from random import shuffle


COLORS = ("Red", "Yellow", "Blue", "Green")


class Card:
	def __init__(self, color, c_type):
		self.color = color
		self.type = c_type

	def __str__(self):
		return f"{self.color} {self.type}" if self.color else self.type

	def __lt__(self, other):
		if self.color is None:
			if other.color is not None:
				return False

			return self.type < other.type

		if other.color is None:
			return True

		if self.color == other.color:
			return self.type < other.type

		return self.color < other.color

class Deck:
	def __init__(self):
		self.deck = []
		self.discard = []
		self.top = None
		self.construct()

	def construct(self):
		self.deck = []

		for color in COLORS:
			self.deck.append(Card(color, '0'))

			for i in range(1, 10):
				self.deck.append(Card(color, str(i)))

			for _ in range(2):
				self.deck.append(Card(color, "skip"))
				self.deck.append(Card(color, "reverse"))
				self.deck.append(Card(color, "draw2"))

		for _ in range(4):
			self.deck.append(Card(None, "wild"))
			self.deck.append(Card(None, "wild+4"))

		shuffle(self.deck)

	def draw(self):
		if not self.deck:
			self.deck = self.discard[:-1]
			self.discard = [self.discard[-1]]
			shuffle(deck)

		return self.deck.pop()

	def flip_top(self):
		self.discard.append(self.draw())
		self.top = self.discard[0]

	def play(self, card):
		self.discard.append(card)
		self.top = card
