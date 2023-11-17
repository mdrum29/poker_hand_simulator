import copy
from src.utils import are_consecutive, count_dupes

def isFlush(hand: [dict]):
    """
    returns True if hand is a flush. And value of high card or none if hand is not made.
    """
    suits = [card['suit'] for card in hand]
    suit_count = {s:suits.count(s) for s in ['clubs', 'diamonds', 'hearts', 'spades']}
    
    for k in suit_count.keys():
        if suit_count[k] >= 5:
            find_highcard = [card['value'] for card in hand if card['suit'] == k]
            highcard = max(find_highcard)
            flush_cards = sorted(find_highcard, reverse=True)[0:5]
            return True, highcard, flush_cards
    
    return False, None, None

        
def isStraight(hand: [dict], straightCards=None):
    """
    returns True if hand is a straight flush. And value of high card or none if hand is not made.
    """
    ranks = [card['value'] for card in hand]
    straight_cards = are_consecutive(ranks)

    if not straight_cards:
        return False, None, []
    
    else:
        if straight_cards:
            return True, straight_cards[-1], straight_cards
        
        else:
            return True, straight_cards[-1], []


def isStraightFlush(hand: [dict]):
    """
    returns True if hand is a straight flush. And value of high card or none if hand is not made.

    """
    if isFlush(hand)[0] == False:
        return False, None, None
    
    else:
        suits = [card['suit'] for card in hand]
        suit_count = {s:suits.count(s) for s in ['clubs', 'diamonds', 'hearts', 'spades']}
        flush_suit = max(suit_count, key=suit_count.get)
        flush_cards = [card for card in hand if card.get("suit") == flush_suit]
        if isStraight(flush_cards, True)[0] == True:
            highcards = [flush_cards[card]['value'] for card in range(len(flush_cards))]
            highcard = max(highcards)
            return True, highcard, sorted(highcards,reverse=True)
        
        else:
            return False, None, None

def isQuads(hand: [dict]):
    """
    returns True if hand is a Trips. And value of trips card or none if hand is not made. And kicker card.

    """
    quads_hand = copy.deepcopy(hand)
    vals = [card['value'] for card in hand]
    duplicate_cards = count_dupes(vals, occurences=4) # 4 means looking for quads.
    if not duplicate_cards:
        return False, None, None
    
    else:
        quad_card = max(duplicate_cards)
        leftover_cards = [value for value in vals if value != quad_card]
        highest = max(leftover_cards)
        kickers = [highest]
        return True, quad_card, kickers

def isTrips(hand: [dict]):
    """
    returns True if hand is a Trips. And value of trips card or none if hand is not made.

    """
    vals = [card['value'] for card in hand]
    duplicate_cards = count_dupes(vals, occurences=3) # 3 means looking for trips.
    if not duplicate_cards:
        return False, None, None
    
    else:
        trip_card = max(duplicate_cards)
        leftover_cards = [value for value in vals if value != trip_card]
        highest = max(leftover_cards)
        leftover_cards.remove(highest)
        second_highest = max(leftover_cards)
        kickers = [highest, second_highest]
        return True, trip_card, kickers
    
def isPair(hand: [dict]):
    vals = [card['value'] for card in hand]
    duplicate_cards = count_dupes(vals, occurences=2) # 2 means looking for a pair.
    if not duplicate_cards:
        return False, None, None
    else:
        pair_card = max(duplicate_cards)
        leftover_cards = [value for value in vals if value != pair_card]
        highest = max(leftover_cards)
        leftover_cards.remove(highest)
        second_highest = None if len(leftover_cards) == 0 else max(leftover_cards)
        if second_highest:
            leftover_cards.remove(second_highest)
        third_highest = None if len(leftover_cards) == 0 else max(leftover_cards)
        kickers = [highest, second_highest, third_highest]
        return True, pair_card, kickers
    
def isTwoPair(hand: [dict]):
    twoPair_hand = copy.deepcopy(hand)
    vals = [card['value'] for card in hand]
    pair_cards = count_dupes(vals, occurences=2) # 2 means looking for a pair.

    if not pair_cards: # no pairs.
        return False, None, None
    
    elif len(pair_cards) == 1: # only 1 pair
        return False, None, None
     
    else:
        pair_cards.sort()
        hi_pair = pair_cards[-1]
        lo_pair = pair_cards[-2]

        for i, card in enumerate(twoPair_hand):
            if twoPair_hand[i]['value'] in [hi_pair, lo_pair]:
                twoPair_hand.remove(card)
        
        kicker = max([card['value'] for card in twoPair_hand])

        return True, hi_pair, lo_pair, kicker
        
    


def isFullHouse(hand: [dict]):
    fullHouse_hand = copy.deepcopy(hand)
    
    vals = [card['value'] for card in fullHouse_hand]
    trips = isTrips(fullHouse_hand)
    if trips[0] == False:
        return False, None, None
    
    else: # if there are trips
        trip_card = trips[1]
        
        for card in reversed(fullHouse_hand):
            if card['value'] == trip_card:
                fullHouse_hand.remove(card)

        pair = isPair(fullHouse_hand)

        if pair[0] == False: # if trips but no pair
            return False, None, None
        
        else: # if trips and pair
            pair_card = pair[1]
            return True, trip_card, pair_card

def highCards(hand: [dict]):
    vals = [card['value'] for card in hand]
    sorted(vals, reverse=True)
    highcards = vals[0:5]

    return highcards



def get_hand_strength(hand: [dict]):
    # straight flush
    if isStraightFlush(hand)[0] == True:
        hand_type = "straight_flush"
        hand_rank = 9 # highest ranking hand

    # quads
    elif isQuads(hand)[0] == True:
        hand_type = "quads"
        hand_rank = 8 # highest ranking hand

    # full house
    elif isFullHouse(hand)[0] == True:
        hand_type = "full_house"
        hand_rank = 7 # highest ranking hand

    # flush
    elif isFlush(hand)[0] == True:
        hand_type = "flush"
        hand_rank = 6 # highest ranking hand

    # straight
    elif isStraight(hand)[0] == True:
        hand_type = "straight"
        hand_rank = 5 # highest ranking hand

    # trips
    elif isTrips(hand)[0] == True:
        hand_type = "trips"
        hand_rank = 4 # highest ranking hand

    # two pair
    elif isTwoPair(hand)[0] == True:
        hand_type = "two_pair"
        hand_rank = 3 # highest ranking hand

    # pair
    elif isPair(hand)[0] == True:
        hand_type = "pair"
        hand_rank = 2 # highest ranking hand
    
    # highcard
    else:
        hand_type = "highcard"
        hand_rank = 1 # highest ranking hand    

    return {"hand_type": hand_type, "hand_rank": hand_rank}

def compareTwoHands(hand1, hand2):
    hand1_rank = get_hand_strength(hand1)
    hand2_rank = get_hand_strength(hand2)

    if hand1_rank['hand_rank'] > hand2_rank['hand_rank']:
        return hand1
    
    elif hand1_rank['hand_rank'] < hand2_rank['hand_rank']:
        return hand2
    
    elif hand1_rank['hand_rank'] == hand2_rank['hand_rank']:
        if hand1_rank['hand_rank'] == 9: # straight flush tie. hi card all that matters.
            h1 = isStraightFlush(hand1)
            h2 = isStraightFlush(hand2)
            h1[1]
            if h1[1] > h2[1]:
                return hand1
            elif h1[1] < h2[1]:
                return hand2
            else:
                for card1, card2 in zip(h1[2], h2[2]):
                    if card1 > card2:
                        return hand1
                    elif card1 < card2:
                        return hand2
                return None


        elif hand1_rank['hand_rank'] == 8: # quad tie. higher quad card decides.
            h1 = isQuads(hand1)
            h2 = isQuads(hand2)
            
            if h1[1] > h2[1]:
                return hand1
            elif h1[1] < h2[1]:
                if h1[2] > h2[2]:
                    return hand1
                elif h1[2] < h2[2]:
                    return hand2
                else:
                    return None
            
        elif hand1_rank['hand_rank'] == 7: # full house. higher trips card then higher pair. If still tied. Tie.
            if isFullHouse(hand1)[1] > isFullHouse(hand1)[1]:
                return hand1
            elif isFullHouse(hand1)[1] < isFullHouse(hand1)[1]:
                return hand2
            else: # if the trip card is equal.
                if isFullHouse(hand1)[2] > isFullHouse(hand1)[2]:
                    return hand1
                elif isFullHouse(hand1)[2] < isFullHouse(hand1)[2]:
                    return hand2
                else:
                    return None
                
        elif hand1_rank['hand_rank'] == 6: # flush. high card wins.
            h1 = isFlush(hand1)
            h2 = isFlush(hand2)
            
            for card1, card2 in zip(h1[2], h2[2]):
                if card1 > card2:
                    return hand1
                elif card1 < card2:
                    return hand2
                
            return None # same flush ie. if the flush is all 5 board cards.
        
        elif hand1_rank['hand_rank'] == 5: # straight. high card wins. Else tie
            h1 = isStraight(hand1)
            h2 = isStraight(hand2)
            
            if h1[1] > h2[1]:
                return hand1
            elif h1[1] < h2[1]:
                return hand2
            else:
                return None
        
        elif hand1_rank['hand_rank'] == 4: # trips. high card wins.
            h1 = isTrips(hand1)
            h2 = isTrips(hand2)

            h1_cards = [h1[1]] + h1[2]
            h2_cards = [h2[1]] + h2[2]

            for card1, card2 in zip(h1_cards, h2_cards):
                if card1 > card2:
                    return hand1
                elif card1 < card2:
                    return hand2
                
            return None
        
        elif hand1_rank['hand_rank'] == 3: # two pair. highest pair then, highest second pair then kicker.
            h1 = isTwoPair(hand1)
            h2 = isTwoPair(hand2)

            h1_cards = [h1[1], h1[2], h1[3]]
            h2_cards = [h2[1], h2[2], h2[3]]

            for card1, card2 in zip(h1_cards, h2_cards):
                if card1 > card2:
                    return hand1
                elif card1 < card2:
                    return hand2
                
            return None
        
        elif hand1_rank['hand_rank'] == 2: # pair. highest pair then, then highest kicker.
            h1 = isPair(hand1)
            h2 = isPair(hand2)

            h1_cards = [h1[1]] + h1[2]
            h2_cards = [h2[1]] + h2[2]

            for card1, card2 in zip(h1_cards, h2_cards):
                if card1 > card2:
                    return hand1
                elif card1 < card2:
                    return hand2
                
            return None
        
        else: # highest card wins
            h1 = highCards(hand1)
            h2 = highCards(hand2)
            for card1, card2 in zip(h1, h2):
                if card1 > card2:
                    return hand1
                elif card1 < card2:
                    return hand2
            return None

    else:
        raise Exception("Error Comparing hands.")
            

        







if __name__ == '__main__':
    test_hand1 = [
        {'rank': 5, 'suit': 'diamonds', 'value': 5},
        {'rank': 6, 'suit': 'diamonds', 'value': 6},
        {'rank': 7, 'suit': 'diamonds', 'value': 7},
        {'rank': 8, 'suit': 'diamonds', 'value': 8},
        {'rank': "Q", 'suit': 'diamonds', 'value': 12},
        {'rank': 4, 'suit': 'diamonds', 'value': 4},
        {'rank': 4, 'suit': 'clubs', 'value': 4},
        {'rank': 4, 'suit': 'hearts', 'value': 4},
        {'rank': 4, 'suit': 'spades', 'value': 4},
    ]

    test_hand2 = [
        {'rank': 5, 'suit': 'diamonds', 'value': 5},
        {'rank': 6, 'suit': 'diamonds', 'value': 6},
        {'rank': 7, 'suit': 'diamonds', 'value': 7},
        {'rank': 8, 'suit': 'diamonds', 'value': 8},
        {'rank': "Q", 'suit': 'diamonds', 'value': 12},
        {'rank': 4, 'suit': 'diamonds', 'value': 4},
        {'rank': 4, 'suit': 'clubs', 'value': 4},
        {'rank': 4, 'suit': 'hearts', 'value': 4},
        {'rank': 9, 'suit': 'diamonds', 'value': 9},
    ]
    
    straight_hand = [
        {'rank': 5, 'suit': 'diamonds', 'value': 5},
        {'rank': 6, 'suit': 'diamonds', 'value': 6},
        {'rank': 7, 'suit': 'diamonds', 'value': 7},
        {'rank': 8, 'suit': 'spades', 'value': 8},
        {'rank': "Q", 'suit': 'clubs', 'value': 12},
        {'rank': 4, 'suit': 'diamonds', 'value': 4},
        {'rank': 4, 'suit': 'clubs', 'value': 4},
    ]

    flush_hand = [
        {'rank': 5, 'suit': 'diamonds', 'value': 5},
        {'rank': 6, 'suit': 'diamonds', 'value': 6},
        {'rank': 2, 'suit': 'diamonds', 'value': 2},
        {'rank': 8, 'suit': 'spades', 'value': 8},
        {'rank': "Q", 'suit': 'diamonds', 'value': 12},
        {'rank': 4, 'suit': 'diamonds', 'value': 4},
        {'rank': 4, 'suit': 'clubs', 'value': 4},
    ]

# winningHand = compareTwoHands(test_hand1, test_hand2)

# print("You have a", hand_strength['hand_type']+".", "Your Best 5 cards are: ")

# print("What is the high card?", highCards(test_hand))
# print("Is the hand a pair?", isPair(test_hand)[0], " ||  pair card:", isPair(test_hand)[1], "  ||  kickers:", isPair(test_hand)[2])
# print("Is the hand a two pair?", isTwoPair(test_hand)[0], " || hi pair card:", isTwoPair(test_hand)[1], " || hi pair card:", isTwoPair(test_hand)[2], "  ||  kickers:", isTwoPair(test_hand)[3])
# print("Is the hand trips?", isTrips(test_hand)[0], " ||  trips card:", isTrips(test_hand)[1], "  ||  kickers:", isTrips(test_hand)[2])
# print("Is the hand a straight?", isStraight(test_hand,  straightCards=True)[0], " ||  straight highcard:", isStraight(test_hand)[1])
# print("Is the hand a flush?", isFlush(test_hand)[0], " ||  flush highcard:", isFlush(test_hand)[1])
# print("Is the hand a full house?", isFullHouse(test_hand)[0], " ||  full house trip card:", isFullHouse(test_hand)[1], " ||  full house pair card:", isFullHouse(test_hand)[2])
# print("Is the hand a quads?", isQuads(test_hand)[0], " ||  quad card:", isQuads(test_hand)[1], "  ||  kicker:", isQuads(test_hand)[2])
# print("Is the hand a straight flush?", isStraightFlush(test_hand)[0],  " ||  straight flush highcard:", isStraightFlush(test_hand)[1])
