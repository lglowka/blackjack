import random


class Card(object):

    def __init__(self, suit, value, weight):
        self.suit = suit
        self.value = value
        self.weight = weight

    def show_cards(self):
        print("{} of {}".format(self.value, self.suit))

    def ret_value(self):
        return self.weight


class Deck(object):

    def __init__(self):
        self.cards = []
        self.build()

    # build deck of cards
    def build(self):
        num_of_decks = 5
        for n in range(num_of_decks):
            # to each suit
            for s in ["S", "C", "D", "H"]:
                # add value
                for v in ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]:
                    if v in ["K", "Q", "J", "T"]:
                        weight = 10
                    elif v == "A":
                        weight = 11
                    elif v == "9":
                        weight = 9
                    elif v == "8":
                        weight = 8
                    elif v == "7":
                        weight = 7
                    elif v == "6":
                        weight = 6
                    elif v == "5":
                        weight = 5
                    elif v == "4":
                        weight = 4
                    elif v == "3":
                        weight = 3
                    elif v == "2":
                        weight = 2
                    # append to deck of cards a card object
                    self.cards.append(Card(s, v, weight))

    def show(self):
        for c in self.cards:
            c.show_cards()

    def shuffle(self):
        # from end of deck to beginning
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            # change places of [i] card with random card in a deck
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        return self.cards.pop()

def check_deck(deck):
    if len(deck.cards) == 0:
        deck.build()
        deck.shuffle()


class Dealer(object):

    def __init__(self):
        self.name = "Dealer"
        self.hand = []
        self.d_v = 0

    def draw(self, deck):
        print(self.name + " hand: ")
        self.hand.append(deck.draw())

    def show_hand(self):
        for c in self.hand:
            c.show_cards()

    def show_value(self, d_hand_value):
        for c in self.hand:
            d_hand_value += c.ret_value()
        return d_hand_value

    def discard(self):
        return self.hand.clear()

    def action(self):
        self.d_v = 0
        play = True
        d_hand_value = 0
        num_of_loops = 0
        while play:
            if dealer.show_value(d_hand_value) == 21:
                print("Dealer got 21!")
                play = False
            elif dealer.show_value(d_hand_value) < 17:
                check_deck(deck)
                dealer.draw(deck)
                dealer.show_hand()
                print(dealer.show_value(d_hand_value))
            elif dealer.show_value(d_hand_value) > 21:
                num_of_loops += 1
                if contains(dealer.hand, lambda x: x.value == "A"):
                    if num_of_loops <= nums(dealer.hand, lambda x: x.value == "A"):
                        d_hand_value -= 10
                        print("Ace = 1")
                        print(dealer.show_value(d_hand_value))
                    else:
                        print("Dealer bust")
                        play = False
                else:
                    print("Dealer bust")
                    play = False
            else:
                print("Dealer stay on", dealer.show_value(d_hand_value))
                play = False
        self.d_v = dealer.show_value(d_hand_value)


class Player(object):

    def __init__(self, name):
        self.hand = []
        self.hand1 = []
        self.name = name
        self.winnings = 0
        self.p_v = 0
        self.bet = 0

    def draw(self, deck):
        self.hand.append(deck.draw())

    def show_hand(self):
        print(self.name + " hand: ")
        for c in self.hand:
            c.show_cards()

    def show_value(self, p_hand_value):
        for c in self.hand:
            p_hand_value += c.ret_value()
        return p_hand_value

    def action(self, bet):
        self.p_v = 0
        self.bet = bet
        play = True
        p_hand_value = 0
        num_of_loops = 0
        print(player.show_value(p_hand_value))
        while play:
            if player.show_value(p_hand_value) == 21:
                print("You got 21!")
                play = False
            elif player.show_value(p_hand_value) < 21:
                dec = input("Dealer: Action on player\nType [h] to hit, [s] to stay,[d] to double")
                if dec == "h":
                    check_deck(deck)
                    player.draw(deck)
                    player.show_hand()
                    print(player.show_value(p_hand_value))

                elif dec == "s":
                    print("Player stay on", player.show_value(p_hand_value))
                    play = False

                elif dec == "d":
                    player.double(self.bet, p_hand_value)
                    print("Bet: ", self.bet)
                    play = False

            elif player.show_value(p_hand_value) > 21:
                num_of_loops += 1
                if contains(player.hand, lambda x: x.value == "A"):
                    if num_of_loops <= nums(player.hand, lambda x: x.value == "A"):
                        p_hand_value -= 10
                        print("Ace = 1")
                        print(player.show_value(p_hand_value))
                    else:
                        print("Bust")
                        play = False
                else:
                    print("Bust")
                    play = False
        self.p_v = player.show_value(p_hand_value)

    def discard(self):
        return self.hand.clear()

    def double(self, bet, p_hand_value):
        self.winnings -= bet
        self.bet = bet * 2
        #
        check_deck(deck)
        player.draw(deck)
        player.show_hand()
        if player.show_value(p_hand_value) > 21:
            if contains(player.hand, lambda x: x.value == "A"):
                p_hand_value -= 10
                print("Ace = 1")
                print(player.show_value(p_hand_value))

            else:
                print(player.show_value(p_hand_value))
                print("Bust")
        else:
            print("Player stay on", player.show_value(p_hand_value))
        self.p_v = player.show_value(p_hand_value)

    def can_split(self, hand):
        if hand[0].value == hand[1].value:
            return True
        else:
            return False

    def split(self):
        player.hand1.append(player.hand.pop())
        player.draw(deck)
        player.show_hand()


def contains(list, filter):
    for x in list:
        if filter(x):
            return True
    return False


def nums(list, filter):
    num = 0
    for x in list:
        if filter(x):
            num += 1
    return num


def winner(p_v, d_v, bet):
    if p_v <= 21 and d_v <= 21:
        if p_v > d_v:
            win = bet * 2
            print("You won", win)
        elif p_v == d_v:
            win = bet
            print("Draw. You got back", win)
        else:
            win = 0
            print("You lost")
    elif p_v > 21 and d_v > 21:
        win = bet
        print("Draw. You got back", win)
    elif p_v > 21 >= d_v:
        win = 0
        print("You lost")
    else:
        win = bet * 2
        print("You won", win)
    return win


def start_game():
    global player, dealer, deck, a
    deck = Deck()
    dealer = Dealer()
    deck.shuffle()
    name = input("Dealer: Hi! We are playing Blackjack.\nThere is 5 decks in play.\nWhat's Your name? ")
    player = Player(name)


def deal_hand():
    exep = True
    while exep:
        try:
            player.bet = int(input("Dealer: New hand, place Your bet: "))
            exep = False
        except ValueError:
            print("Oops!  That was no valid bet.  Try again...")
    player.winnings -= player.bet
    check_deck(deck)
    dealer.draw(deck)
    dealer.show_hand()
    check_deck(deck)
    player.draw(deck)
    check_deck(deck)
    player.draw(deck)
    player.show_hand()
    # players hand loop
    while player.can_split(player.hand):
        if player.can_split(player.hand):
            d = input("To split type [s]")
            if d == "s":
                player.split()
            else:
                player.show_hand()
                break

    player.action(player.bet)
    dealer.action()
    print()
    player.winnings += winner(player.p_v, dealer.d_v, player.bet)
    player.discard()
    dealer.discard()
    print()
    while player.hand1:
        player.winnings -= player.bet
        dealer.draw(deck)
        dealer.show_hand()
        player.hand.append(player.hand1.pop(0))
        player.draw(deck)
        player.show_hand()
        while player.can_split(player.hand):
            if player.can_split(player.hand):
                d = input("To split type [s]")
                if d == "s":
                    player.split()

                else:
                    player.show_hand()
                    break
        player.action(player.bet)
        dealer.action()
        print()
        player.winnings += winner(player.p_v, dealer.d_v, player.bet)
        player.discard()
        dealer.discard()
        print()


def res():
    if player.winnings == 0:
        print("You broke even")
    elif player.winnings > 0:
        print("Profit: " + str(player.winnings))
    else:
        print(("Lost: " + str(player.winnings * (-1))))


def main_loop():
    start_game()
    running = True
    while running:
        deal_hand()
        stop = input("Next hand? To stop type [n]")
        if stop == "n":
            running = False
    res()


main_loop()
