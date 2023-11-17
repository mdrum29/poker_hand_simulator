# poker_hand_simulator
This program allows the user to simulates a variety of heads up (1v1) poker hand scenarios. The user must pass their starting hole cards and optionally may pass an opponent starting hand and/or the current table cards.
The program then simulates a real poker game (without betting for now). The cards are shuffled. The deck is cut, then the cards are dealt. The program also burns the proper cards. Once the hand runs out. The ranking function determines the winner. It accounts for tie breakers in all hand types. In poker, some hands can end in a tie. Then the simulator function runs this game as many times as the user passes. Higher numbers are more accurate but can run slowly on a local device.

## 1. main.py
Taking a look at main.py. This will call the simulator. You will need to pass in hole_cards and sims. Optional opponent hole cards and current board.

Cards are formatted cap first letter or number and lowercase first letter of suit. Examples "Tc" -> 10 of clubs  "9s" -> 9 of spades   "Ad" -> ace of diamonds

hole_cards = ["As", "2h"]
opponent_hole_cards = []

table_cards = ["9h", "9s", "7h"]    -> this means we are playing post flop
sims = 100

![main_func_start](https://github.com/mdrum29/poker_hand_simulator/assets/96875916/e6fab87f-4013-4352-86ef-fef4e0fc0e8c)



## 2. Run an example
Gif showing a set of simulations executing. Example is post flop with randomize opponent cards.


![Running_picture](https://github.com/mdrum29/poker_hand_simulator/assets/96875916/7799699d-7424-4218-9f73-3eed7afdab0e)



## 3. Run example 2 
Gif showing a set of simulations executing. Example is post flop with given opponent cards.



![Running_picture_2](https://github.com/mdrum29/poker_hand_simulator/assets/96875916/d5939b8c-a327-47a6-8346-997f61837782)
