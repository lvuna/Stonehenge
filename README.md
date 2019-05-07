# Intro
This was one of my first shcool assignment, it is mainly an AI vs. human game, our goal is to implements decision strategy made by computer so it always chooses the "absolute" winning step, if there is one, of course.

## Stonehenge
The game is simple, within a grid, player take turns repeatly, each time they are allowed to capture one spot. If more than half the spots were captured by the same player on an horizontal/vertical/diagonal line, the player gets a point. Whoever gets the most points wins after all spots have been captured.

## Idea of AI design
The idea of Ai design is to recursively explore every possible states, determine if it leads to win state, and randomly pick one that will lead to the winstate.

## Setup
* It's a console app game, just run it inside terminal after cloning the project.
