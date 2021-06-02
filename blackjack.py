"""
Blackjack game
"""

import random
import time
suits = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def value(self):
        return values[self.rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    def __init__(self):
        self.allcards = []
        for suit in suits:
            for rank in ranks:
                self.allcards.append(Card(rank, suit))

    def value(self):
        val = 0
        for cards in self.allcards:
            val += cards.value()
        return val

    def shuffle(self):
        random.shuffle(self.allcards)

    def deal_one(self):
        return self.allcards.pop()

    def __len__(self):
        return len(self.allcards)

    def __str__(self):
        mylist = [print(cards) for cards in self.allcards]
        return ''


class Player:
    player_num = 1
    def __init__(self, name=''):
        self.allcards = []
        self.balance = 0
        if name == '':
            name = 'Player' + str(Player.player_num)
            Player.player_num += 1
        self.name = name

    def value(self):
        val = 0
        ace_count = 0
        for cards in self.allcards:
            if cards.rank == 'Ace':
                ace_count += 1
            val += cards.value()
        while ace_count != 0:
            if val > 21:
                val -= 10
                ace_count -= 1
            else:
                break
        return val

    def add_card(self, new_cards):
        if type(new_cards) == list:
            self.allcards.extend(new_cards)
        else:
            self.allcards.append(new_cards)

    def remove_first(self):
        return self.allcards.pop(0)

    def remove_last(self):
        return self.allcards.pop()

    def remove_all(self):
        self.allcards = []

    def chips(self, amount=0):
        if self.balance + amount >= 0:
            self.balance += amount
            return self.balance
        else:
            return self.balance + amount

    def ip(self, imsg='input', arg=str):
        if imsg == 'input':
            msg = f'{self.name} - Please enter input: '
        if imsg == 'bet':
            msg = f'{self.name} - Please enter desired bet amount: '
        if imsg == 'hit':
            msg = f'{self.name} - Please enter "h" to hit, "s" to stand: '
        if imsg == 'replay':
            msg = f'{self.name} - Please enter "y" to replay, "n" to exit: '
        if arg != str:
            arg = int
        while True:
            val = input(msg)
            if arg == int:
                try:
                    if int(val) >= 0:
                        return int(val)
                    else:
                        print('Invalid entry. Please try again')
                        continue
                except:
                    print('Invalid entry. Please try again')
                    continue
            else:
                val = val.lower()
                if val == 'h':
                    return True
                if val == 's':
                    return False
                return val

    def hit(self):
        if self.name == 'Dealer':
            hit_point = 17
            if self.value() >= hit_point:
                hit_on = False
            else:
                hit_on = True
        else:
            hit_point = 21
            hit_on = self.ip('hit')
        while hit_on:
            self.add_card(deck.deal_one())
            if self.value() >= hit_point:
                if self.name == 'Dealer':
                    print(self)
                    print(self.name + ' point is: ' + str(self.value()))
                    return ''
                else:
                    print(dealer)
                    print(self)
                    print(self.name + ' point is: ' + str(self.value()))
                    # print('Player busted!')
                    return 'Dealer'
            print(self)
            print(self.name + ' point is: ' + str(self.value()))
            if self.name == 'Dealer':
                print('Dealer hitting again...')
                time.sleep(3)
                hit_on = True
            else:
                hit_on = self.ip('hit')
        return ''

    def show_except_one(self):
        print('\n' + self.name + ':')
        for index,cards in enumerate(self.allcards):
            if index == 0:
                print('***Card Hidden***')
            else:
                print(cards)

    def __str__(self):
        print('\n' + self.name + ':')
        mylist = [print(cards) for cards in self.allcards]
        return ''


deck = Deck()
dealer = Player('Dealer')
player = Player()
player.chips(100)

while True:
    print('Player chips remaining: ' + str(player.chips()))
    while True:
        bet = player.ip('bet', int)
        if bet <= player.chips():
            break
        else:
            print('Insufficient chips! Please try again.')
            continue

    deck.shuffle()
    dealer.add_card([deck.deal_one(), deck.deal_one()])
    player.add_card([deck.deal_one(), deck.deal_one()])

    dealer.show_except_one()
    # print(dealer.name + ' point is: ' + str(dealer.value()))
    print(player)
    # print(dealer)
    print(player.name + ' point is: ' + str(player.value()))

    player.hit()
    if player.value() > 21:
        print('Player busted! Dealer wins!')
        player.chips(-bet)
        print('Player chips remaining: ' + str(player.chips()))
        if player.chips() == 0:
            print('Insufficient chips! Please recharge and try again.')
            exit()
        replay = player.ip('replay')
        if replay == 'y':
            player.remove_all()
            dealer.remove_all()
            deck = Deck()
            continue
        else:
            exit()
    print(dealer)
    dealer.hit()
    if dealer.value() > 21:
        print('Dealer busted! Player wins!')
        player.chips(bet)
        print('Player chips remaining: ' + str(player.chips()))
        if player.chips() == 0:
            print('Insufficient chips! Please recharge and try again.')
            exit()
        replay = player.ip('replay')
        if replay == 'y':
            player.remove_all()
            dealer.remove_all()
            deck = Deck()
            continue
        else:
            exit()
    elif dealer.value() > player.value():
        print('Dealer has higher points! Dealer wins!')
        player.chips(-bet)
        print('Player chips remaining: ' + str(player.chips()))
        if player.chips() == 0:
            print('Insufficient chips! Please recharge and try again.')
            exit()
        replay = player.ip('replay')
        if replay == 'y':
            player.remove_all()
            dealer.remove_all()
            deck = Deck()
            continue
        else:
            exit()
    else:
        print('Player has higher points! Player wins!')
        player.chips(bet)
        print('Player chips remaining: ' + str(player.chips()))
        if player.chips() == 0:
            print('Insufficient chips! Please recharge and try again.')
            exit()
        replay = player.ip('replay')
        if replay == 'y':
            player.remove_all()
            dealer.remove_all()
            deck = Deck()
            continue
        else:
            exit()
