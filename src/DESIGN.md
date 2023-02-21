# Design 

I want this site to be simple at first. I want to try to avoid feature bloat if possible. I'm taking inspiration for many of the features from setwithfriends.com and it's GitHub https://github.com/ekzhang/setwithfriends 

The features that are specific to the game of 24 are as follows: 

2 game modes: 

- Traditional 
- Set 

Traditional will randomly deal 4 cards (1-9) and the players try to be the first to input the correct solution. Once a solution is found, a new group of cards will be dealt. 

Set is a twist on the game Set. A 4 by 4 grid of cards will be dealt and players can choose any combination of 4 cards to try and create 24. Once a solution is submitted, those 4 cards will disappear from the board and be replaced by newer cards. This is similar to the game of Set except the rules are 4 cards must form 24. 

Games will take place in a room where there can be 1-6 players. 

Dealing with no possible solutions: 

This is a real possibility so I have thought about 2 solutions: 

-Make sure that 