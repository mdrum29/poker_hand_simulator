from src.simulate_game import sim_game
import time

def print_results(wp, hand_made_count, hand_percent):
    print("Win Probability:", wp)
    print("")
    for t in hand_made_count.keys():
        print(t, "probability:", hand_percent[t])
    print("")

def run_simulations(sims: int, startingHand: [str], opponentStartHand: [str] = [], cards_on_table: [str] = []):
    start_time = time.time()

    game_results = []
    hands_made = []
    for sim in range(0,sims):
        result = sim_game(startingHand = startingHand, opponentStartHand=opponentStartHand, cards_on_table=cards_on_table)
        game_results.append(result[0])
        hands_made.append(result[1]['player_hand_made'])
    # tie_probablity = sum([1 for result in game_results if result is None])/sims
    win_probability = game_results.count(True)/sims
    hand_made_count = {unique_hand: hands_made.count(unique_hand) for unique_hand in list(set(hands_made))}
    hand_percent = {k: round(hand_made_count[k]/sims,4) for k in hand_made_count.keys()}
    end_time = time.time()
    execution_time = end_time - start_time

    print(sims, "sims completed in", round(execution_time,4),"seconds.")
    print("")
    return win_probability, hand_made_count, hand_percent

if __name__ == "__main__":
    win_probabilty2, hand_made_count, hand_percent = run_simulations(sims=250, startingHand = ["Qh","Th"], opponentStartHand = ['9c','7c'])