from src.hand_rankings import get_hand_strength, compareTwoHands
from src.game_setup import Deck

def getFormatHand(id_list: list):
    hand = []
    for id in id_list:
        hand.append(Deck().card_lookup_by_id(id))

    return hand

def sim_game(startingHand: [str], opponentStartHand: [str] = [], cards_on_table: [str] = []):
    
    # error checking.
    if len(startingHand) != 2:
        raise Exception("invalid player starting hand")
    
    if len(opponentStartHand) != 2 and len(opponentStartHand) != 0:
        raise Exception("invalid opponent starting hand")
    
    # if len(cards_on_table) not in [0,3,4]:
    #     raise Exception("invalid starting table cards")
    


    # initiating deck.
    game_deck = Deck()
    game_deck.shuffle_deck()

    # removing starting table cards from deck
    starting_table_ids = []
    if len(cards_on_table) != 0:
        for c in cards_on_table:
            card_id = game_deck.lookup_ID_by_shorthand(c)
            game_deck.remove_card_from_deck(card_id)
            starting_table_ids.append(card_id)

    # setting starting hands
    startingHand_ids = []
    for card in startingHand:
        card_id = game_deck.lookup_ID_by_shorthand(card)
        startingHand_ids.append(card_id)
        game_deck.remove_card_from_deck(card_id)


    if not opponentStartHand:            
        opponent_ids, opponent_hand = game_deck.deal_hand()
    
    else:
        opponent_ids = []
        opponent_hand = opponentStartHand

        for card in opponent_hand:
            card_id = game_deck.lookup_ID_by_shorthand(card)
            opponent_ids.append(card_id)
            game_deck.remove_card_from_deck(card_id)

    # end hand set up ---------------------------------
    # -------------------------------------------------
    
    # dealing table cards.

    table_cards_ids = []
    table_cards = []

    if len(starting_table_ids) == 3:
        table_cards = table_cards + cards_on_table
        table_cards_ids = table_cards_ids + starting_table_ids

    elif len(starting_table_ids) < 3:
        # burn first card.
        game_deck.burn_card()

        # deal the flop
        flop_ids, flop_cards = game_deck.flop()
        
        for i in range(len(flop_cards)):
            table_cards_ids.append(flop_ids[i])
            table_cards.append(flop_cards[i])

    if len(starting_table_ids) == 4:
        table_cards = table_cards + cards_on_table
        table_cards_ids = table_cards_ids + starting_table_ids

    
    elif len(starting_table_ids) < 4:
        # burn second card.
        game_deck.burn_card()
        
        # deal turn
        turn_id, turn_card = game_deck.turn()
        table_cards_ids = table_cards_ids + turn_id
        table_cards = table_cards + turn_card

    if len(starting_table_ids) == 5:
        table_cards = table_cards + cards_on_table
        table_cards_ids = table_cards_ids + starting_table_ids

    elif len(starting_table_ids) < 5:
        # burn third card.
        game_deck.burn_card()

        # deal river
        river_id, river_card = game_deck.turn()
        table_cards_ids = table_cards_ids + river_id
        table_cards = table_cards + river_card

    allplayer_cards = startingHand + table_cards 
    allplayer_ids = startingHand_ids + table_cards_ids
    player_hand = getFormatHand(allplayer_ids)
    player_details = get_hand_strength(player_hand)
    # print("Player has", player_details['hand_type'])

    allopponent_cards = opponent_hand + table_cards 
    allopponent_ids = opponent_ids + table_cards_ids
    oppo_hand = getFormatHand(allopponent_ids)
    oppo_details = get_hand_strength(oppo_hand)
    # print("Opponent has", oppo_details['hand_type'])

    winningHand = compareTwoHands(player_hand, oppo_hand)

    game_details = {"winning_hand": winningHand, "player_hand": player_hand, "opponent_hand":oppo_hand, "player_hole_cards": startingHand, "opponent_hole_cards": opponent_hand, "table_cards": table_cards, 'player_hand_made': player_details['hand_type']}
    if winningHand == player_hand:
        game_details['winner'] = 'player'
        # print("player wins")
        return True, game_details
    
    elif winningHand == oppo_hand:
        game_details['winner'] = 'opponent'
        # print("opponent wins")
        return False, game_details
    
    else: # if tie
        game_details['winner'] = 'tie'
        # print('hands tied.')
        return None, game_details

    print("")
    return None


if __name__ == "__main__":
    isWin, game_details = sim_game(startingHand=['Ac','2c'], opponentStartHand=['2d','6c'], cards_on_table=['3d', '4h', '5h', 'Td', '5s'])

    print("player_cards:",game_details['player_hole_cards']," || ", game_details['opponent_hole_cards']," || ", game_details['table_cards'])
    print("")
    # print(game_details['player_hand'], game_details['opponent_hand'])

    print("pause.")
