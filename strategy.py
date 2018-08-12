"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from typing import Any
from random import choice
from copy import deepcopy

# TODO: Adjust the type annotation as needed.


def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def rough_outcome_strategy(game: Any) -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2  # Temporarily -- just so we can replace this easily later

    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move

# TODO: Implement a recursive version of the minimax strategy.


def recursive_minimax_strategy(game: Any) -> Any:
    """
    recursive minimax takes in a game,  and return the move that
    minimize the possibility to lose.
    """
    index = []
    moves = game.current_state.get_possible_moves()
    s = deepcopy(game)
    for i in range(len(moves)):
        new_state = game.current_state.make_move(moves[i])
        s.current_state = new_state
        state_value = state_score(s) * -1
        if state_value == 1:
            index.append(i)
    if index != []:
        return moves[choice(index)]
    return choice(moves)


# helper function for the recursive minimax
def state_score(game: Any) -> int:
    """
      This is the helper function for recursive_minimax_strategy, it takes in a
    game and evaluate the score of the state and return a value between
    If the state is over, return -1 because it means the current player loses
    obviously.
    If the game state is not over:
    If there's a move that result in immediate win, the score will be 1
    if for whatever move you make, you will always lose, return -1

    """
    state = game.current_state
    if game.is_over(state):
        if game.is_winner(state.get_current_player_name()):
            return state.WIN
        elif not game.is_winner(state.get_current_player_name()):
            return state.LOSE
        return state.DRAW
    else:
        y = []
        for move in state.get_possible_moves():
            s = deepcopy(game)
            s.current_state = state.make_move(move)
            y.append(s)
        return max([state_score(x) * -1 for x in y])

# TODO: Implement an iterative version of the minimax strategy.


def iterative_minimax_strategy(game: Any) -> any:
    """
      This is iterative minimax strategy, based on the game state, it will
    return the move that minimizes the possibility to lose.
    """
    tree = Tree()
    stack = Stack()
    tree.value = game
    stack.add(tree)
    while not stack.is_empty():
        s = stack.remove()
        state = s.value.current_state
        if s.value.is_over(state):
            if s.value.is_winner(state.get_current_player_name()):
                s.score = state.WIN
            elif not s.value.is_winner(state.get_current_player_name()):
                s.score = state.LOSE
            else:
                s.score = state.DRAW
        else:
            if s.children == []:
                create_children(s, stack, game)
            else:
                s.score = max([child.score * -1 for child in s.children])
    moves = []
    for i in range(len(tree.children)):
        if tree.children[i].score * -1 == tree.score:
            moves.append(i)
    return game.current_state.get_possible_moves()[choice(moves)]


def create_children(tree: "Tree", stack: "Stack", game: Any) -> None:
    """
       Helper function for iterative minimax strategy, create children of
       tree which is also a tree class and append parents back to stack,
        then children.
    """
    state = tree.value.current_state
    for move in state.get_possible_moves():
        new_tree = Tree()
        new_tree.value = deepcopy(game)
        new_state = state.make_move(move)
        new_tree.value.current_state = new_state
        tree.children.append(new_tree)
    stack.add(tree)
    for children in tree.children:
        stack.add(children)

# Here is the helper class and helper function for iterative
# strategy
# ==========================================================

# I copied it from lab6 to make things easier, and change value to score
# for reference.
# Oh I also create a new attribute for score


class Tree:
    """The tree class
    """

    def __init__(self, value=None, score=None, children=None) -> None:
        """
        Create Tree self with content value and 0 or more children
        """
        self.value = value
        self.score = score
        # copy children if not None
        self.children = children[:] if children is not None else []


# I copied and paste this from stack file given in lab4
# to make things easier.
# Oh I also change type annotation here so pycharm don't complain.


class Stack:
    """
    Last-in, first-out (LIFO) stack.
    """

    def __init__(self) -> None:
        """
        Create a new, empty Stack self.

        >>> s = Stack()
        """
        self._contents = []

    def add(self, obj: object) -> None:
        """
        Add object obj to top of Stack self.

        >>> s = Stack()
        >>> s.add(7)
        """
        self._contents.append(obj)

    def remove(self) -> Any:
        """
        Remove and return top element of Stack self.

        Assume Stack self is not empty.

        >>> s = Stack()
        >>> s.add(5)
        >>> s.add(7)
        >>> s.remove()
        7
        """
        return self._contents.pop()

    def is_empty(self) -> bool:
        """
        Return whether Stack self is empty.

        >>> s = Stack()
        >>> s.is_empty()
        True
        >>> s.add(7)
        >>> s.is_empty()
        False
        """
        return len(self._contents) == 0


if __name__ == "__main__":
    from python_ta import check_all

    check_all(config="a2_pyta.txt")

# added a line for testing
# ha second line right now
