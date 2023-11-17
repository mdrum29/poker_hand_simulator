import numpy as np
import random
from src.game_setup import Deck
from src.hand_rankings import compareTwoHands
from src.simulate_game import getFormatHand, get_hand_strength
import time

np.set_printoptions(suppress=True)

def binary_search(Lst, delete_card):
    # Binary search
    low, high = 0, len(Lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if Lst[mid] == delete_card:
            Lst.pop(mid)
        elif Lst[mid] < delete_card:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found

def vectorized_poker(sims: int, startingHand: [str], opponentStartHand: [str] = [], cards_on_table: [str] = []):
    start_time = time.time()
    # how many more cards to simulate.
                    # public card               # opponent hole cards
    total_cards = 9
    cards_to_sim = (5 - len(cards_on_table)) + (2 - len(opponentStartHand))
    sims_array = np.empty((sims, total_cards))

    all_card_ids = [x for x in range(1,53)]

    # set hands
    ref_deck = Deck()
    player_hole_card_ids = [ref_deck.lookup_ID_by_shorthand(i) for i in startingHand]
    
    # removing cards from deck.
    for card in player_hole_card_ids:
        binary_search(all_card_ids, card)

    oppo_hole_card_ids = []
    if opponentStartHand:
        oppo_hole_card_ids = oppo_hole_card_ids + [ref_deck.lookup_ID_by_shorthand(i) for i in opponentStartHand]
        for card in oppo_hole_card_ids:
            binary_search(all_card_ids, card)

    table_card_ids = []
    if cards_on_table:
        table_card_ids = table_card_ids + [ref_deck.lookup_ID_by_shorthand(i) for i in cards_on_table]
        for card in table_card_ids:
            binary_search(all_card_ids, card)

    
    
    for i in range(sims_array.shape[0]):
        sim_card_ids = player_hole_card_ids + table_card_ids + [all_card_ids[c] for c in  random.sample(range(1, len(all_card_ids)), cards_to_sim)] + oppo_hole_card_ids
        sims_array[i, :] = sim_card_ids

    win_tracker = np.empty(sims)
    hand_tracker = np.empty(sims)
    for idx in range(sims_array.shape[0]):
        player_hand = getFormatHand(sims_array[idx,:-2])
        opp_hand = getFormatHand(sims_array[idx,2:])
        winning_hand = compareTwoHands(player_hand, opp_hand)
        player_made_hand = get_hand_strength(player_hand)['hand_rank']
        hand_tracker[idx] = player_made_hand
        if winning_hand == player_hand:
            win_tracker[idx] = 1
        elif winning_hand == opp_hand:
            win_tracker[idx] = -1
        else:
            win_tracker[idx] = 0

    win_count = np.sum(np.isin(win_tracker, 1))
    loss_count = np.sum(np.isin(win_tracker, -1))
    tie_count = sims - win_count - loss_count

    hm={}
    for i in set(hand_tracker.tolist()):
        if i == 9:
            hand = 'straight_flush'
        elif i == 8:
            hand = 'quads'
        elif i == 7:
            hand = 'full_house'
        elif i == 6:
            hand = 'flush'
        elif i == 5:
            hand = 'straight'
        elif i == 4:
            hand = 'trips'
        elif i == 3:
            hand = 'two_pair'
        elif i == 2:
            hand = 'pair'
        else:
            hand = 'highcard'
        hm[hand] = np.count_nonzero(np.isin(hand_tracker, i))/sims

    

    end_time = time.time()
    execution_time = end_time - start_time
    print(execution_time)
    return {"win_probability": win_count/sims,"loss_probability": loss_count/sims,"tie_probability": tie_count/sims, 'hands_made':hm}



probabilities = vectorized_poker(1000, startingHand=["Ac","Ah"], opponentStartHand=["2s","7h"])

print("")