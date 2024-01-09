from collections import defaultdict
from deck import COLORS
from operator import attrgetter
from random import choice


class Player:
    def __init__(self):
        self.hand = []
        self.wins = 0

    def clear(self):
        self.hand = []

    def draw(self, card):
        if card:
            self.hand.append(card)
            self.hand.sort()

    def play(self, valid_moves):
        raise NotImplementedError

    def chose_color(self):
        raise NotImplementedError

    def print_hand(self):
        print(", ".join(str(card) for card in self.hand))

    def count_colors(self):
        color_counts = defaultdict(int)

        for card in self.hand:
            if card.color:
                color_counts[card.color] += 1
        
        return color_counts


class Von(Player):
    def play(self, valid_moves):
        if not (color_counts := self.count_colors()):
            self.hand.remove(valid_moves[0])
            return valid_moves[0]

        largest_color = max(color_counts, key=color_counts.get)

        for card in valid_moves:
            if card.color == largest_color:
                self.hand.remove(card)
                return card

        self.hand.remove(valid_moves[0])
        return valid_moves[0]

    def chose_color(self):
        if not (color_counts := self.count_colors()):
            return choice(COLORS)

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
