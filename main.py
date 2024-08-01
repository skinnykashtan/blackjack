from Player.Player import *


def cls():
    print('\n' * 100)


if __name__ == '__main__':
    print('BLACKJACK')
    print('Type 1 to start')
    print('Type 0 to close')
    option = int(input())
    games = 0
    player = Player(2000, 0, deck=None)

    if option == 1:
        while True:
            if games > 0:
                print(f'Actual balance: ${player.balance}')
                print('Enter 1 to play again')
                print('Enter 0 to close')
                option = int(input())

                if option == 1:
                    deck = Deck()
                    player.deck = deck.game_deck
                    croupier = Player(0, 0, deck=deck.game_deck)
                else:
                    cls()
                    print('Closing..')
                    exit()

            else:
                deck = Deck()
                player.deck = deck.game_deck
                croupier = Player(0, 0, deck=deck.game_deck)

            print('Enter bet amount:')
            bet = int(input())
            player.setBet(bet)

            print('Dealing cards..\n')
            player.assignCards()
            croupier.assignCards()

            cls()

            while True:
                print('Your cards:')
                player.showPlayerCards()

                print('\nCroupier cards:')
                if calculateValue(croupier.cards) > 21:
                    croupier.showPlayerCards()
                    winner(player, croupier)
                    break
                elif calculateValue(player.cards) > 21:
                    croupier.showPlayerCards()
                    winner(player, croupier)
                    break
                else:
                    croupier.showCroupierCards()

                print("\n'd': draw a card | 'c': check")
                choice = input()

                cls()

                if choice == 'd':
                    player.drawCard()
                    if calculateValue(croupier.cards) < 17:
                        croupier.drawCard()
                    else:
                        pass

                elif choice == 'c':
                    print('Your cards:')
                    player.showPlayerCards()

                    print('\nCroupier cards:')
                    croupier.showPlayerCards()

                    winner(player, croupier)

                    games += 1
                    break

            games += 1
    else:
        cls()
        print('Closing..')
        exit()
