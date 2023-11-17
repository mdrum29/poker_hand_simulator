from src.calculate_win_probability import run_simulations, print_results

hole_cards = ["As", "2h"]
opponent_hole_cards = ["Kh", "Ks"]

table_cards = ["2s", "7h", "Th", "9c"]
sims = 100

if __name__ == "__main__":
    wp, hands_made, hand_percent = run_simulations(sims, startingHand=hole_cards, 
                            opponentStartHand=opponent_hole_cards, cards_on_table=table_cards)
    print_results(wp, hands_made, hand_percent)
