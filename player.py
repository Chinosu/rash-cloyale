import pygame
import random
import copy

class Deck:
    def __init__(self, cards):
        self.cards = cards

class Card:
    def __init__(self, img_path):
        self.level = 1
        self.max_hp = 100
        self.curr_hp = self.max_hp
        self.dmg = 20
        self.attack_speed = 1.0     # attacks per second
        self.move_speed = 1.0       # tiles per second
        self.cost = 1               # elixir cost
        self.image = pygame.image.load(img_path).convert_alpha()
    
    def upgrade(self):
        self.max_hp *= 1.1
        self.dmg *= 1.1
        self.level += 1
        

class Player:
    def __init__(self):
        self.kingT_hp = 2000
        self.princessT_hp = 1000
        self.max_elix = 10
        self.current_elix = 0
        self.elix_regen = 0.5       # 0.5 elixir per second
        self.card_queue = []
        self.current_cards = []
    
    def addCardsToQueue(self, deck):
        shuffle_cards = copy.deepcopy(deck.cards)
        random.shuffle(shuffle_cards)
        self.card_queue.extend(shuffle_cards)
    
    def addCardsToHand(self):
        for i in range(4):
            card = self.card_queue.pop(0)
            self.current_cards.append(card)
    
    def nextCard(self, index):
        if self.card_queue:
            card = self.current_cards.pop(index)
            # Perform actions with the card (e.g., use it)
            # ...
            # After using the card, add it back to the end of the queue
            self.card_queue.append(card)
            new_card = self.card_queue.pop(0)
            self.current_cards.insert(index, new_card)