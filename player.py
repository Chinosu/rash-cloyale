import pygame
import random
import copy

class Deck:
    def __init__(self, cards):
        self.cards = cards

class Card:
    def __init__(self, img_path):
        self.max_hp = 100
        self.curr_hp = 100
        self.dmg = 20
        self.attack_speed = 1.0     # attacks per second
        self.move_speed = 1.0       # tiles per second
        self.cost = 1
        self.image = pygame.image.load(img_path)
        

class Player:
    def __init__(self):
        self.kingT_hp = 2000
        self.princessT_hp = 1000
        self.max_elixir = 10
        self.current_elixir = 0
        self.card_queue = []
    
    def addCardsToQueue(self, deck):
        shuffle_cards = copy.deepcopy(deck.cards)
        random.shuffle(shuffle_cards)
        self.card_queue.extend(shuffle_cards)
    
    def nextCard(self):
        if self.card_queue:
            next_card = self.card_queue.pop(0)
            # Perform actions with the next_card (e.g., use it)
            # ...
            # After using the card, add it back to the end of the queue
            self.card_queue.append(next_card)