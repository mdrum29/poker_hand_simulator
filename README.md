# poker_hand_simulator 🃏🃏

This program allows the user to simulate a variety of heads up (1v1) poker hand scenarios. The user must pass their starting hole cards and optionally may pass an opponent starting hand and/or the current table cards.
The program then simulates a real poker game (without betting for now). The cards are shuffled. The deck is cut, then the cards are dealt. The program also burns the proper cards. Once the hand runs out. The ranking function determines the winner. It accounts for tie breakers in all hand types. In poker, some hands can end in a tie. Then the simulator function runs this game as many times as the user passes. Higher numbers are more accurate but can run slowly on a local device.

*** NEW Addition - created an optimized simulation using numpy and binary search where applicable. The optimized version reduces the run time on 5000 simulations by ~14%. See 5.

## 1. main.py

Taking a look at main.py. This will call the simulator. You will need to pass in hole_cards and sims. Optional opponent hole cards and current board.

Cards are formatted cap first letter or number and lowercase first letter of suit. Examples "Tc" -> 10 of clubs  "9s" -> 9 of spades   "Ad" -> ace of diamonds

hole_cards = ["As", "2h"]
opponent_hole_cards = []

table_cards = ["9h", "9s", "7h"]    -> this means we are playing post flop
sims = 100

![main_func_start](https://github.com/mdrum29/poker_hand_simulator/assets/96875916/e6fab87f-4013-4352-86ef-fef4e0fc0e8c)



## 2. Run Example 1

Gif showing a set of simulations executing. Example is post flop with randomized opponent cards.


![Running_picture](https://github.com/mdrum29/poker_hand_simulator/assets/96875916/7799699d-7424-4218-9f73-3eed7afdab0e)



## 3. Run Example 2 

Gif showing a set of simulations executing. Example is post flop with given opponent cards.

## 4. Additional Examples

### a. only hole cards given.

![different_cards_no_flop](https://github.com/mdrum29/poker_hand_simulator/assets/96875916/aa79993b-dc8d-4659-8cf8-3d3dede30dae)

### b. no table cards give.

![image](https://github.com/mdrum29/poker_hand_simulator/assets/96875916/33f009cb-c94b-4fbe-ae0c-52813a3138a1)

## 5. Optimizied Example

Applied binary search algorithm to remove cards from deck faster. Used NumPy to generate random card_ids as integers and then translate those back into card string values.

![optimized_1](https://github.com/mdrum29/poker_hand_simulator/assets/96875916/d0ee9f6c-f333-4989-9cee-b3cdf2c0c248)


## Next Steps

1. Need to overhaul the ranking system. At the moment, the code looks at dictionaries with suits and values to determine straights, flushes, etc. Will need to think through an algorithm that can identify the hand from the card_ids.
2. I think there is opportunity for this because each card is assign a unique value 1-52 in a consistent pattern. An algorithm maybe able to identify hand strength by the number pattern of a hand.

