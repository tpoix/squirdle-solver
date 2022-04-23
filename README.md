# Squirdle Solver

## What is it?

Squirdle Solver is a tiny program developped in Python 3 to simulate someone solving a [Squirdle](https://squirdle.fireblend.com/daily.html) by Fireblend.<br>
It picks a random Pokémon and then reduce the list of possibilities, then picks another random Pokémon in this new list and again and again... until it finds the Pokémon of the day.

## How to launch it?

Before launching it, be sure to have all 3 batches of data in the same directory as `squirdle_solver.py`. The 3 batches are available in this repo, but you can fetch them with `fetch_data.py`. Data is provided by [PokéAPI](https://pokeapi.co/), so be sure you have an Internet connection before fetching data. A lot of thanks to them for making this possible.

To launch the solver, just launch `squirdle_solver.py` with a Python 3 environnement. You will have to type the name of the Pokémon of the day.<br>
By default, the data is in French, so you have to enter names in French. Other languages may be supported in the future (if I have the time).

## Why is it for?

Well, I wanted to make a little program to simulate this kind of situation. It's very basic, the solver isn't very smart, I didn't want to implement strategical guesses (like picking middle sized Pokémon to eliminate half the population from the start) because I wanted to be able to beat it haha. Also I really like random guesses.<br>
You can try to beat it each day, it may be hard if they make a very good guess from the start! 
