from Deck.Deck import *
from main import cls


def winner(player, croupier):
    bet = player.bet
    prize = bet * 2
    player_pts = calculateValue(player.cards)
    croupier_pts = calculateValue(croupier.cards)

    if croupier_pts < player_pts <= 21:
        player.winBalance(prize)
        print(f'\nResult: Win ${prize}!')
    elif 21 >= croupier_pts > player_pts:
        print(f'\nResult: Lose ${bet}!')
    elif croupier_pts > 21 >= player_pts:
        player.winBalance(prize)
        print(f'\nResult: Win ${prize}!')
    elif player_pts > 21 >= croupier_pts:
        print(f'\nResult: Lose ${bet}!')
    else:
        player.winBalance(bet)
        print('\nResult: Tie!')


def calculateValue(cards):
    value = 0
    has_ace = False

    for card in cards:
        rank = card.split()[1]

        if rank.isdigit():
            value += int(rank)
        elif rank in ['Jack', 'Queen', 'King']:
            value += 10
        elif rank == 'Ace':
            has_ace = True
            value += 11

    if has_ace and value > 21:
        value -= 10

    return value


class Player:

    def __init__(self, balance, bet, deck):
        self.balance = balance
        self.bet = bet
        self.deck = deck
        self.cards = []

    def winBalance(self, amount):
        self.balance += amount

    def setBet(self, amount):
        while amount <= 0:
            print('Not possible!')
            print(f'Your current balance: ${self.balance}')
            print('To exit enter 0')
            print('To bet enter 1')
            choice = int(input())
            if choice == 0:
                cls()
                print('Closing..')
                exit()
            elif choice == 1:
                print('Bet amount:')
                amount = int(input())

        while amount > self.balance:
            print('Insufficient balance.')
            print(f'Your current balance: ${self.balance}')
            print('Bet again:')
            amount = int(input())
        else:
            self.balance -= amount
            self.bet = amount

    def assignCards(self):
        assigned_cards = [random.choice(self.deck) for _ in range(0, 2)]
        self.cards = assigned_cards
        for card in self.cards:
            try:
                self.deck.remove(card)
            except ValueError:
                pass

    def drawCard(self):
        random_card = random.choice(self.deck)
        self.cards.append(random_card)
        try:
            self.deck.remove(random_card)
        except ValueError:
            pass

    def showPlayerCards(self):
        print(*self.cards, end='\n', sep=', ')

    def showCroupierCards(self):
        print('?', *self.cards[1:], end='\n', sep=', ')
