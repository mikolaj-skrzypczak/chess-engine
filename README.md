# Python Chess Engine

## Table of contents
* [General info](#general-info)
* [Image processing project](#image-processing)
* [Technologies](#technologies)
* [TODO](#todo)
* [Instructions](#instructions)
* [Further development ideas](#further-development-ideas)

## General info
I have been playing chess since primary school and one day I had an idea to implement chess in Python. Then, I came across a tutorial by Eddie Sharick, who made a whole 16 episodes series covering the topic.
This repository is a result of following his videos,  sometimes coming up with some improvements on my own. Hereby, I highly
encourage you to visit his YouTube channel and check the whole series by yourself.

[Eddie's YouTube channel](https://www.youtube.com/channel/UCaEohRz5bPHywGBwmR18Qww)

[First episode of "Chess engine in Python"](https://www.youtube.com/watch?v=EnYui0e73Rs&ab_channel=EddieSharick)

Edit (November 2021):
In order to complete my Human-Computer Communication classes I had to choose any image processing related topic and 
prepare a project of my choice. I have decided to go with chess again. Our (project done in pairs, my co-worker's GitHub profile: [Piotr45](https://github.com/Piotr45))
goal is to create a neural network able to recognize pieces from a 2D chess board :smile:

Files related to this project can be found in [image_processing](image_processing) folder.
## Technologies
* Python 3.7.8
* pygame 2.0.1
* numpy 1.21.4


## TODO
feel free to contribute :grinning:
- [ ] Cleaning up the code - right now it is really messy.
- [ ] Using numpy arrays instead of 2d lists.
- [ ] Stalemate on 3 repeated moves or 50 moves without capture/pawn advancement.
- [ ] Menu to select player vs player/computer.
- [ ] Allow dragging pieces.
- [ ] Resolve ambiguating moves (notation).

## Instructions
1. Clone this repository.
2. Select whether you want to play versus computer, against another player locally, or watch the game of engine playing against itself by setting appropriate flags in lines 52 and 53 of `ChessMain.py`.
3. Run `ChessMain.py`.
4. Enjoy the game!

#### Sic:
* Press `z` to undo a move.
* Press `r` to reset the game.

## Further development ideas
1. Ordering the moves (ex. looking at checks and/or captures) should make the engine much quicker (because of the alpha-beta pruning).
2. Keeping track of all the possible moves in a given position, so that after a move is made the engine doesn't have to recalculate all the moves.
3. Evaluating kings placement on the board (separate in middle game and in the late game).
4. Book of openings.