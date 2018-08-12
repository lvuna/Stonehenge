BOARD_LENGTH_3 = \
"""\
         @   @
        /   / 
    @ - {} - B   {}
       / \\ / \\ /
  @ - C - D - E   @
     / \\ / \\ / \\ /
@ - F - G - H - I
     \\ / \\ / \\ / \\
  @ - J - K - L   @
       \\   \\   \\
        @   @   @""".format('A', 1)

s = "      @   @\n     /   /\n@ - A - B\n     \\ / \\\n" +\
                        "  @ - C   @\n       \\\n        @"

v = "      @   @\n     /   /\n@ - A - B\n     \\ / \\\n" +\
                        "  @ - C   @\n       \\\n        @"

class testing:

    test1 = 5
    test2 = [4, 5, 6]

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.z = v

    def __str__(self):

        return self.z


    index = []
    current_state = game.current_state
    moves = current_state.get_possible_moves()
    for i in range(len(moves)):
        new_state = current_state.make_move(moves[i])
        state_value = state_score(new_state) * -1
        if state_value == 1:
            index.append(i)
    if index != []:
        return moves[choice(index)]
    else:
        return choice(moves)


temp_game = deepcopy(game)
    temp_game.current_state = state
    if temp_game.is_over(state):
        if temp_game.is_winner(state.get_current_player_name()):
            return 1
        else:
            return -1
    else:
        return max([state_score(temp_game,
                                temp_game.current_state.make_move(move)) * -1
                    for move in state.get_possible_moves()])


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
        state_value = state_score(s)
        if state_value == 1:
            index.append(i)
    if index != []:
        return moves[choice(index)]
    else:
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
    if game.is_winner(state.get_current_player_name()):
        return 1
    elif not game.is_winner(state.get_current_player_name()):
        return -1
    else:
        y = []
        s = deepcopy(game)
        for move in state.get_possible_moves():
            s.current_state = state.make_move(move)
            y.append(s)
        return max([(state_score(x) * -1) for x in y])







def recursive_minimax_strategy(game: Any) -> Any:
    """
    recursive minimax takes in a game,  and return the move that
    minimize the possibility to lose.
    """
    index = []
    current_state = game.current_state
    moves = current_state.get_possible_moves()
    for i in range(len(moves)):
        new_state = current_state.make_move(moves[i])
        state_value = state_score(new_state) * -1
        if state_value == 1:
            index.append(i)
    if index != []:
        return moves[choice(index)]
    else:
        return choice(moves)


# helper function for the recursive minimax
def state_score(state: Any) -> int:
    """
      This is the helper function for recursive_minimax_strategy, it takes in a
    game and evaluate the score of the state and return a value between
    If the state is over, return -1 because it means the current player loses
    obviously.
    If the game state is not over:
    If there's a move that result in immediate win, the score will be 1
    if for whatever move you make, you will always lose, return -1

    """
    if state.get_possible_moves() == []:
        return -1
    else:
        return max([state_score(state.make_move(move)) * -1 for move in
                    state.get_possible_moves()])


if s.children == []:
    for move in state.get_possible_moves():
        new_tree = Tree()
        new_tree.value = deepcopy(game)
        new_state = state.make_move(move)
        new_tree.value.current_state = new_state
        s.children.append(new_tree)
    stack.add(s)
    for children in s.children:
        stack.add(children)




 y = ('@ 1 / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - 1 - L - M - N @ / \ / \ / \ / \ / \ / @ - O - P - Q - R - S - T \ / \ / \ / \ / \ / \ @ - U - V - W - X - Y @ \ \ \ \ \ @ @ 1 @ @ @ 1 / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - K - L - M - N @ / \ / \ / \ / \ / \ / @ - O - 1 - Q - R - S - T \ / \ / \ / \ / \ / \ @ - U - V - W - X - Y @ \ \ \ \ \ @ @ @ @ @ @ 1 / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - K - L - M - N @ / \ / \ / \ / \ / \ / @ - O - P - Q - R - S - T \ / \ / \ / \ / \ / \ @ - 1 - V - W - X - Y @ \ \ \ \ \ 1 @ @ @ @ @ @ / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - 1 - K - L - M - N @ / \ / \ / \ / \ / \ / @ - O - P - Q - R - S - T \ / \ / \ / \ / \ / \ @ - U - V - W - X - Y @ \ \ \ \ \ @ @ @ @ @ @ @ / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - K - 1 - M - N @ / \ / \ / \ / \ / \ / @ - O - P - Q - R - S - T \ / \ / \ / \ / \ / \ @ - U - V - W - X - Y @ \ \ \ \ \ @ @ @ @ @ @ @ / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - K - L - 1 - N @ / \ / \ / \ / \ / \ / @ - O - P - Q - R - S - T \ / \ / \ / \ / \ / \ @ - U - V - W - X - Y @ \ \ \ \ \ @ @ @ @ 1 @ @ / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - K - L - M - 1 @ / \ / \ / \ / \ / \ / @ - O - P - Q - R - S - T \ / \ / \ / \ / \ / \ @ - U - V - W - X - Y @ \ \ \ \ \ @ @ @ @ @ @ @ / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - K - L - M - N 1 / \ / \ / \ / \ / \ / @ - O - P - Q - R - S - 1 \ / \ / \ / \ / \ / \ @ - U - V - W - X - Y @ \ \ \ \ \ @ @ @ @ @ @ @ / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - K - L - M - N 1 / \ / \ / \ / \ / \ / @ - O - P - Q - R - S - T \ / \ / \ / \ / \ / \ @ - U - V - W - X - 1 @ \ \ \ \ \ @ @ @ @ 1 @ @ / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - K - L - M - N @ / \ / \ / \ / \ / \ / @ - 1 - P - Q - R - S - T \ / \ / \ / \ / \ / \ @ - U - V - W - X - Y @ \ \ \ \ \ 1 @ @ @ @ @ @ / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - K - L - M - N @ / \ / \ / \ / \ / \ / @ - O - P - 1 - R - S - T \ / \ / \ / \ / \ / \ @ - U - V - W - X - Y @ \ \ \ \ \ @ @ 1 @ @ @ @ / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - K - L - M - N @ / \ / \ / \ / \ / \ / @ - O - P - Q - 1 - S - T \ / \ / \ / \ / \ / \ @ - U - V - W - X - Y @ \ \ \ \ \ @ @ @ @ @ @ @ / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - K - L - M - N @ / \ / \ / \ / \ / \ / @ - O - P - Q - R - 1 - T \ / \ / \ / \ / \ / \ @ - U - V - W - X - Y @ \ \ \ \ \ @ @ @ @ 1 @ @ / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - K - L - M - N @ / \ / \ / \ / \ / \ / @ - O - P - Q - R - S - T \ / \ / \ / \ / \ / \ @ - U - 1 - W - X - Y @ \ \ \ \ \ @ @ @ @ @ @ @ / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - K - L - M - N @ / \ / \ / \ / \ / \ / @ - O - P - Q - R - S - T \ / \ / \ / \ / \ / \ @ - U - V - 1 - X - Y @ \ \ \ \ \ @ @ 1 @ @ @ @ / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - K - L - M - N @ / \ / \ / \ / \ / \ / @ - O - P - Q - R - S - T \ / \ / \ / \ / \ / \ @ - U - V - W - 1 - Y @ \ \ \ \ \ @ @ @ @ @')

 x = ('@ 1 / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - 1 - L - M - N @ / \ / \ / \ / \ / \ / @ - O - P - Q - R - S - T \ / \ / \ / \ / \ / \ @ - U - V - W - X - Y @ \ \ \ \ \ @ @ 1 @ @ @ 1 / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - K - L - M - N @ / \ / \ / \ / \ / \ / @ - O - 1 - Q - R - S - T \ / \ / \ / \ / \ / \ @ - U - V - W - X - Y @ \ \ \ \ \ @ @ @ @ @ @ 1 / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - K - L - M - N @ / \ / \ / \ / \ / \ / @ - O - P - Q - R - S - T \ / \ / \ / \ / \ / \ @ - 1 - V - W - X - Y @ \ \ \ \ \ 1 @ @ @ @ @ @ / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - 1 - K - L - M - N @ / \ / \ / \ / \ / \ / @ - O - P - Q - R - S - T \ / \ / \ / \ / \ / \ @ - U - V - W - X - Y @ \ \ \ \ \ @ @ @ @ @ @ @ / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - K - 1 - M - N @ / \ / \ / \ / \ / \ / @ - O - P - Q - R - S - T \ / \ / \ / \ / \ / \ @ - U - V - W - X - Y @ \ \ \ \ \ @ @ @ @ @ @ @ / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - K - L - 1 - N @ / \ / \ / \ / \ / \ / @ - O - P - Q - R - S - T \ / \ / \ / \ / \ / \ @ - U - V - W - X - Y @ \ \ \ \ \ @ @ @ @ @ @ @ / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - K - L - M - 1 @ / \ / \ / \ / \ / \ / @ - O - P - Q - R - S - T \ / \ / \ / \ / \ / \ @ - U - V - W - X - Y @ \ \ \ \ \ @ @ @ @ @ @ @ / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - K - L - M - N 1 / \ / \ / \ / \ / \ / @ - O - P - Q - R - S - 1 \ / \ / \ / \ / \ / \ @ - U - V - W - X - Y @ \ \ \ \ \ @ @ @ @ @ @ @ / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - K - L - M - N 1 / \ / \ / \ / \ / \ / @ - O - P - Q - R - S - T \ / \ / \ / \ / \ / \ @ - U - V - W - X - 1 @ \ \ \ \ \ @ @ @ @ @ @ @ / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - K - L - M - N @ / \ / \ / \ / \ / \ / @ - 1 - P - Q - R - S - T \ / \ / \ / \ / \ / \ @ - U - V - W - X - Y @ \ \ \ \ \ 1 @ @ @ @ @ @ / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - K - L - M - N @ / \ / \ / \ / \ / \ / @ - O - P - 1 - R - S - T \ / \ / \ / \ / \ / \ @ - U - V - W - X - Y @ \ \ \ \ \ @ @ 1 @ @ @ @ / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - K - L - M - N @ / \ / \ / \ / \ / \ / @ - O - P - Q - 1 - S - T \ / \ / \ / \ / \ / \ @ - U - V - W - X - Y @ \ \ \ \ \ @ @ @ @ @ @ @ / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - K - L - M - N @ / \ / \ / \ / \ / \ / @ - O - P - Q - R - 1 - T \ / \ / \ / \ / \ / \ @ - U - V - W - X - Y @ \ \ \ \ \ @ @ @ @ @ @ @ / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - K - L - M - N @ / \ / \ / \ / \ / \ / @ - O - P - Q - R - S - T \ / \ / \ / \ / \ / \ @ - U - 1 - W - X - Y @ \ \ \ \ \ @ @ @ @ @ @ @ / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - K - L - M - N @ / \ / \ / \ / \ / \ / @ - O - P - Q - R - S - T \ / \ / \ / \ / \ / \ @ - U - V - 1 - X - Y @ \ \ \ \ \ @ @ 1 @ @ @ @ / / 2 - 2 - 1 @ / \ / \ / 2 - 2 - 1 - 2 @ / \ / \ / \ / 1 - 1 - 2 - 1 - 2 @ / \ / \ / \ / \ / @ - J - K - L - M - N @ / \ / \ / \ / \ / \ / @ - O - P - Q - R - S - T \ / \ / \ / \ / \ / \ @ - U - V - W - 1 - Y @ \ \ \ \ \ @ @ @ @ @')

print(y == x)
