# FMF Code Challenge

This repository contains code for Noah Bogart's code challenge. All code is Python 3.5+.

## Calculator Prototype

calculator.py contains the MVP for a Java-styled singleton calculator that can handle the four basic operations:
addition, subtraction, multiplication, and division. It also include a small testing suite, handling the most common
edge-cases and setting up for expansion later.

I emulated the example code, as I don't have the time to fully refactor into more "Pythonic" code, but I feel the
internals are sound. Number has to be imported for multiplication, as Python will take `10 * '20'` and create a string
40 characters long.

## Bootstrap Page

My apologies, I have never worked with Bootstrap. This is the best I could come up with in the time I had left.

The page is located at bootstrap/index.html.

## Installation

    git clone https://github.com/NoahTheDuke/flock.git

Tests can by run by running `python3 calculator.py`.
