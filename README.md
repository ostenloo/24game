# 24 Game 

Command Line Python Program that plays the 24 game with you. 

Shamelessly stole the code to generate solutions from [here](https://www.youtube.com/shorts/PNc_Ju3u-OE)

The other stuff was my own with help from ChatGPT lol 

I actually learned quite a bit about multithreading in Python.

Some of the implementations are pretty "hacky" and I should consider finding more elegant solutions. 

For example: 

(to be added later)

## Setting Up 

`git clone https://github.com/ostenloo/24game.git` 

`pip install -r requirements.txt` 

## Disclaimer 

I don't follow PEMDAS with the solutions. There are no parentheses and order of operations goes from left to right. `x` and `/` don't have precedence over `+` and `-`. I could implement these order of operation rules but it's a bit more complicated. This is why if you see a solution like `9+7*2-8`, the answer isn't `9+(7*2)-8 = 15`. It's `(9+7)*2-8 = 24`. 