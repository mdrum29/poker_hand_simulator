import random
import copy
from src.utils import are_consecutive, count_dupes

class Deck:
    suit_convert = {"c": "clubs", "d": "diamonds", "h": "hearts", "s": "spades"}

    def __init__(self):
        ranks = [str(num) for num in range(2,10)] + ["T", "J", "Q", "K", "A"] # T is 10 so all cards can be 2 characters
        suits = ["clubs", "diamonds", 'hearts', 'spades']
        cards = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]

        for card in cards:
            if card['rank'] == 'A':
                card['value'] = 14
            elif card['rank'] == 'K':
                card['value'] = 13
            elif card['rank'] == 'Q':
                card['value'] = 12
            elif card['rank'] == "J":
                card['value'] = 11
            elif card['rank'] == "T":
                card['value'] = 10
            else:
                card['value'] = int(card['rank'])

        # assigning each card a unique integer to identify it more easily in the monte carlo simulation
        for id, card in enumerate(cards):
            card['id'] = id + 1


        self.deck = cards
        self.referenceDeck = copy.deepcopy(cards) # used for look ups so all cards are always in it.

    
    def shuffle_deck(self):
        # card_positions = [range(1,53)]
        # random.shuffle(card_positions) # would work. going to make my own shuffler instead.
        sorter = {random.uniform(0, 1): card for card in self.deck}
        order = list(sorter.keys())
        order.sort()

        shuffled_deck = [sorter[pos] for pos in order]
        self.deck = shuffled_deck

    
    def cut_the_deck(self, whereCut: int):
        if whereCut == 0:
            pass
        
        elif whereCut > 52:
            raise Exception("Cut position must be <= 52")
        
        else:
            top = self.deck[0:whereCut]
            bottom = self.deck[whereCut:]

            cut_deck = bottom + top
            self.deck = cut_deck

    
    def remove_card_from_deck(self, ID: int):
        for card in self.deck:
            if card['id'] == ID:
                self.deck.remove(card)        
    
    def hand_card_from_deck(self, IDs: [int]):
        
        for card in self.deck:
            if card['id'] in IDs:
                self.deck.remove(card)

    def deal_hand(self):
        hand_ids = [self.deck[0]['id'], self.deck[1]['id']]
        self.remove_card_from_deck(hand_ids[0])
        self.remove_card_from_deck(hand_ids[1])

        dealt_hand = [self.id_to_shorthand(hand_ids[0]), self.id_to_shorthand(hand_ids[1])]

        return hand_ids, dealt_hand
    
    def burn_card(self):
        self.deck.remove(self.deck[0])

    def flop(self):
        flop_ids = self.deck[0]['id'], self.deck[1]['id'], self.deck[2]['id']
        flop_cards = [self.id_to_shorthand(flop_ids[0]), self.id_to_shorthand(flop_ids[1]), self.id_to_shorthand(flop_ids[2])]
        self.remove_card_from_deck(flop_ids[0])
        self.remove_card_from_deck(flop_ids[1])
        self.remove_card_from_deck(flop_ids[2])

        return flop_ids, flop_cards
    
    def turn(self):
        turn_id = [self.deck[0]['id']]
        self.remove_card_from_deck(turn_id[0])

        turn_card = [self.id_to_shorthand(turn_id[0])]

        return turn_id, turn_card
    
    def river(self):
        river_id = [self.deck[0]['id']]
        self.remove_card_from_deck(river_id[0])

        river_card = [self.id_to_shorthand(river_id[0])]

        return river_id, river_card

# ---------- card finder functions
    def card_lookup_by_id(self, ID: int):
        for card in self.referenceDeck:
            if card['id'] == ID:
                return card
                
    
    def lookup_ID_by_shorthand(self, card: str):
        # example pass "Tc" for Ten of clubs
        rank, suit = card[0], card[1]
        
        for c in self.referenceDeck:
            if c['rank'] == rank and c['suit'] == self.suit_convert[suit]:
                return c["id"]
    
    
    def id_to_shorthand(self, card_id: int):
        for card in self.referenceDeck:
            if card_id == card['id']:
                s = card['suit']


                return card['rank'] + s[0]
          
           




if __name__ == "__main__":

    # running through deck operations
    d1 = Deck()
    # d1.create_cards()
    d1.shuffle_deck()
    d1.cut_the_deck(2)
    current_deck = d1.deck
    card = d1.card_lookup_by_id(2)
    # d1.remove_card_from_deck(52)
    id = d1.lookup_ID_by_shorthand('Ac')

    print("")