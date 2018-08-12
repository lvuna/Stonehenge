"""The file for stonehenge game and its state class
"""

from copy import deepcopy
from game import Game
from game_state import GameState


class StonehengeGame(Game):
    """the subclass of game for stonehenge game
        """

    def __init__(self, is_p1_play: bool) -> None:
        """initalize a new stonehenge game, and create
                    a game state for itself.
                """
        self.length = int(input('enter the side length of your board:'))
        self.is_p1_play = is_p1_play
        self.current_state = StonehengeState(is_p1_play, self.length)

    def get_instructions(self) -> str:
        """ return the instructions for the game
                """
        return """Game name: Stonehenge
                    Rule:
                        player takes turn to capture the cells by
                     calling its letter, once the player has
                     captured at least half of the cells 
                     on a layline,that layline will be captured.
                     The first player who has capture at
                     least half of the laylines will win the game
                    Note:
                        Layline is marked as '@' if uncaptured.
                     once player has captured the cells or
                     laylines, it will be shown by number 1
                     or 2 depends on who is the player
                     that captured it.
                     """

    def is_over(self, state: "StonhengeState") -> bool:
        """return whether if the game is over or not
                """
        p1 = 0
        p2 = 0
        for leyline in state.leyline:
            if leyline == '1':
                p1 += 1
            if leyline == '2':
                p2 += 1
        if p1 >= len(state.leyline) / 2:
            return True
        elif p2 >= len(state.leyline) / 2:
            return True
        return False

    def is_winner(self, player: str) -> bool:
        """return if the winner is the winner
                """
        return (self.current_state.get_current_player_name() != player
                and self.is_over(self.current_state))

    def str_to_move(self, string: str) -> str:
        """return the move format in correct type
                """
        return string.upper()


class StonehengeState(GameState):
    """subclass of GameState that keeps track of the information
             of stonehenge game.
        """

    def __init__(self, is_p1_turn: bool, side_length: int) -> None:
        """initalize a new gamestate for stonehenge game with sidelength
        between 1 - 5.
                """
        assert side_length in range(1, 6)
        super().__init__(is_p1_turn)
        self.side_length = side_length
        if self.side_length == 1:
            self.cell = [['A', 'B'], ['C'], ['A'], ['B', 'C'], ['A', 'C'],
                         ['B']]

        elif self.side_length == 2:
            self.cell = [['A', 'B'], ['C', 'D', 'E'], ['F', 'G'], ['A', 'C'],
                         ['B', 'D', 'F'], ['E', 'G'], ['C', 'F'],
                         ['A', 'D', 'G'], ['B', 'E']]

        elif self.side_length == 3:
            self.cell = [['A', 'B'], ['C', 'D', 'E'], ['F', 'G', 'H', 'I'],
                         ['J', 'K', 'L'], ['A', 'C', 'F'], ['B', 'D', 'G', 'J'],
                         ['E', 'H', 'K'], ['I', 'L'], ['F', 'J'],
                         ['C', 'G', 'K'], ['A', 'D', 'H', 'L'], ['B', 'E', 'I']]

        elif self.side_length == 4:
            self.cell = [['A', 'B'], ['C', 'D', 'E'], ['F', 'G', 'H', 'I'],
                         ['J', 'K', 'L', 'M', 'N'], ['O', 'P', 'Q', 'R'],
                         ['A', 'C', 'F', 'J'], ['B', 'D', 'G', 'K', 'O'],
                         ['E', 'H', 'L', 'P'], ['I', 'M', 'Q'], ['N', 'R'],
                         ['J', 'O'], ['F', 'K', 'P'], ['C', 'G', 'L', 'Q'],
                         ['A', 'D', 'H', 'M', 'R'], ['B', 'E', 'I', 'N']]

        else:
            self.cell = [['A', 'B'], ['C', 'D', 'E'], ['F', 'G', 'H', 'I'],
                         ['J', 'K', 'L', 'M', 'N'],
                         ['O', 'P', 'Q', 'R', 'S', 'T'],
                         ['U', 'V', 'W', 'X', 'Y'],
                         ['A', 'C', 'F', 'J', 'O'],
                         ['B', 'D', 'G', 'K', 'P', 'U'],
                         ['E', 'H', 'L', 'Q', 'V'], ['I', 'M', 'R', 'W'],
                         ['N', 'S', 'X'], ['T', 'Y'], ['O', 'U'],
                         ['J', 'P', 'V'], ['F', 'K', 'Q', 'W'],
                         ['C', 'G', 'L', 'R', 'X'],
                         ['A', 'D', 'H', 'M', 'S', 'Y'],
                         ['B', 'E', 'I', 'N', 'T']]

        self.leyline = ['@' for i in range((self.side_length + 1) * 3)]

    def __str__(self) -> str:
        """return the string representation of the class
                """
        if self.side_length == 1:
            return draw_graph1(self.cell, self.leyline)
        elif self.side_length == 2:
            return draw_graph2(self.cell, self.leyline)
        elif self.side_length == 3:
            return draw_graph3(self.cell, self.leyline)
        elif self.side_length == 4:
            return draw_graph4(self.cell, self.leyline)
        return draw_graph5(self.cell, self.leyline)

    def __repr__(self) -> str:
        """return the representation of the class
                """
        return (self.__str__() +
                '\n current player: {}'.format(self.get_current_player_name()))

    def get_possible_moves(self) -> list:
        """return  all the possible moves a player may choose in a list
        >>> s = StonehengeState(True, 1)
        >>> s.get_possible_moves()
        ['A', 'B', 'C']
                """
        s = []
        p1 = 0
        p2 = 0
        for leyline in self.leyline:
            if leyline == '1':
                p1 += 1
            if leyline == '2':
                p2 += 1
        if p1 >= len(self.leyline) / 2 or p2 >= len(self.leyline) / 2:
            return s
        for rows in self.cell:
            for cells in rows:
                if cells != '1' and cells != '2':
                    s.append(cells)
        s = set(s)
        s = list(s)
        s.sort()
        return s

    def make_move(self, move: str) -> "StonehengeState":
        """after making a move, rfeturn the new current state for the
        stonehenge game without making changes to the old one.
        >>> s = StonehengeState(True, 2)
        >>> y = s.make_move('A')
        >>> s.leyline != y.leyline
        True
                """
        new_cell = deepcopy(self.cell)
        for i in range(len(new_cell)):
            for x in range(len(new_cell[i])):
                if self.get_current_player_name() == 'p1' and\
                        move == new_cell[i][x]:
                    new_cell[i][x] = '1'
                if self.get_current_player_name() == 'p2' and\
                        move == new_cell[i][x]:
                    new_cell[i][x] = '2'
        temp_leyline = deepcopy(self.leyline)
        new_leyline = captured(new_cell, temp_leyline)
        new_state = StonehengeState(not self.p1_turn, self.side_length)
        new_state.cell = new_cell
        new_state.leyline = new_leyline
        return new_state

    def rough_outcome(self) -> float:
        """return the best estimated outcome the current player can get,
        1 represent win, 0 represent draw and -1 represent lost.
        the returned number can be between the interval[-1, 1].
        >>> s = StonehengeState(True, 1)
        >>> s.rough_outcome()
        1
                """
        if self.get_possible_moves() == []:
            return self.LOSE
        s = []
        for move in self.get_possible_moves():
            temp_new_state = self.make_move(move)
            if temp_new_state.get_possible_moves() == []:
                return self.WIN
            x = True
            for oppomove in temp_new_state.get_possible_moves():
                second_temp_state = temp_new_state.make_move(oppomove)
                if second_temp_state.get_possible_moves() == []:
                    x = False
            if x is True:
                s.append(True)
        if s == []:
            return self.LOSE
        return len(s) / len(self.get_possible_moves())


def captured(lst1: list, lst2: list) -> list:
    """check if the leyline has been captured or not, and return lst2
    lst1 is a list of lists that contains the elements in the
    leylines in the order with respect to lst2, which is the leyline.
    >>> lst1 = [['A', '1']]
    >>> lst2 = ['@']
    >>> captured(lst1, lst2)
    ['1']
        """
    for i in range(len(lst2)):
        if lst2[i] == '@':
            p1 = check_capture1(lst1[i])
            p2 = check_capture2(lst1[i])
            if p1 >= len(lst1[i]) / 2:
                lst2[i] = '1'
            elif p2 >= len(lst1[i]) / 2:
                lst2[i] = '2'
    return lst2


def check_capture1(lst: list) -> int:
    """
        Return p1  based on the number of occurences in lst1,
     this is a helper function for captured.
    """
    p1 = 0
    for element in lst:
        if element == '1':
            p1 += 1
    return p1


def check_capture2(lst: list) -> int:
    """
        Return p2  based on the number of occurences in lst1,
     this is a helper function for captured.
    """
    p2 = 0
    for element in lst:
        if element == '2':
            p2 += 1
    return p2


# template for each board(Helper function here)

def draw_graph1(lst1: list, lst2: list) -> str:
    """draw the graph for stonehenge of side length one, the lst1 is
    the list of leyline's cell, and lsst2 contains the leyline situation,
     it should return a graph like string.
    """
    assert len(lst1) == len(lst2) == 6
    return \
        """\
              {}   {}
             /   /
        {} - {} - {}
             \\ / \\
          {} - {}   {}
               \\
                {}""".format(lst2[2], lst2[3], lst2[0], lst1[0][0],
                             lst1[0][1], lst2[1], lst1[1][0], lst2[5],
                             lst2[4])


def draw_graph2(lst1: list, lst2: list) -> str:
    """draw the graph for stonehenge of side length two, the lst1 is
    the list of leyline's cell, and lsst2 contains the leyline situation,
     it should return a graph like string.
    """
    assert len(lst1) == len(lst2) == 9
    return \
        """\
                {}   {}
               /   /
          {} - {} - {}   {}
             / \\ / \\ /
        {} - {} - {} - {}
             \\ / \\ / \\
          {} - {} - {}   {}
               \\   \\
                {}   {}""".format(lst2[3], lst2[4], lst2[0], lst1[0][0],
                                  lst1[0][1], lst2[5], lst2[1], lst1[1][0],
                                  lst1[1][1], lst1[1][2], lst2[2], lst1[2][0],
                                  lst1[2][1], lst2[8], lst2[6], lst2[7])


def draw_graph3(lst1: list, lst2: list) -> str:
    """draw the graph for stonehenge of side length three, the lst1 is
        the list of leyline's cell, and lsst2 contains the leyline situation,
         it should return a graph like string.
        """
    assert len(lst1) == len(lst2) == 12
    return \
        """\
                 {}   {}
                /   / 
            {} - {} - {}   {}
               / \\ / \\ /
          {} - {} - {} - {}   {}
             / \\ / \\ / \\ /
        {} - {} - {} - {} - {}
             \\ / \\ / \\ / \\
          {} - {} - {} - {}   {}
               \\   \\   \\
                {}   {}   {}""".format(lst2[4], lst2[5], lst2[0],
                                       lst1[0][0], lst1[0][1], lst2[6],
                                       lst2[1], lst1[1][0], lst1[1][1],
                                       lst1[1][2], lst2[7], lst2[2],
                                       lst1[2][0], lst1[2][1], lst1[2][2],
                                       lst1[2][3], lst2[3], lst1[3][0],
                                       lst1[3][1], lst1[3][2], lst2[11],
                                       lst2[8], lst2[9], lst2[10])


def draw_graph4(lst1: list, lst2: list) -> str:
    """draw the graph for stonehenge of side length four, the lst1 is
        the list of leyline's cell, and lsst2 contains the leyline situation,
         it should return a graph like string.
        """

    assert len(lst1) == len(lst2) == 15
    return \
        """\
                    {}   {}
                   /   / 
              {} - {} - {}   {}
                 / \\ / \\ /
            {} - {} - {} - {}   {}
               / \\ / \\ / \\ /
          {} - {} - {} - {} - {}   {}
             / \\ / \\ / \\ / \\ /
        {} - {} - {} - {} - {} - {}
             \\ / \\ / \\ / \\ / \\
          {} - {} - {} - {} - {}   {}
               \\   \\   \\   \\
                {}   {}   {}   {}""".format(lst2[5], lst2[6], lst2[0],
                                            lst1[0][0], lst1[0][1], lst2[7],
                                            lst2[1], lst1[1][0], lst1[1][1],
                                            lst1[1][2],
                                            lst2[8], lst2[2], lst1[2][0],
                                            lst1[2][1],
                                            lst1[2][2], lst1[2][3], lst2[9],
                                            lst2[3],
                                            lst1[3][0], lst1[3][1], lst1[3][2],
                                            lst1[3][3], lst1[3][4], lst2[4],
                                            lst1[4][0], lst1[4][1], lst1[4][2],
                                            lst1[4][3], lst2[14], lst2[10],
                                            lst2[11], lst2[12], lst2[13])


def draw_graph5(lst1: list, lst2: list) -> str:
    """draw the graph for stonehenge of side length five, the lst1 is
        the list of leyline's cell, and lsst2 contains the leyline situation,
         it should return a graph like string.
        """

    assert len(lst1) == len(lst2) == 18
    return \
        """\
                      {}   {}
                     /   / 
                {} - {} - {}   {}
                   / \\ / \\ /
              {} - {} - {} - {}   {}
                 / \\ / \\ / \\ /
            {} - {} - {} - {} - {}   {}
               / \\ / \\ / \\ / \\ /
          {} - {} - {} - {} - {} - {}   {}
             / \\ / \\ / \\ / \\ / \\ /
        {} - {} - {} - {} - {} - {} - {}
             \\ / \\ / \\ / \\ / \\ / \\
          {} - {} - {} - {} - {} - {}   {}
               \\   \\   \\   \\   \\
                {}   {}   {}   {}   {}""".format(lst2[6], lst2[7], lst2[0],
                                                 lst1[0][0], lst1[0][1],
                                                 lst2[8],
                                                 lst2[1], lst1[1][0],
                                                 lst1[1][1],
                                                 lst1[1][2], lst2[9], lst2[2],
                                                 lst1[2][0], lst1[2][1],
                                                 lst1[2][2],
                                                 lst1[2][3], lst2[10], lst2[3],
                                                 lst1[3][0], lst1[3][1],
                                                 lst1[3][2],
                                                 lst1[3][3], lst1[3][4],
                                                 lst2[11],
                                                 lst2[4], lst1[4][0],
                                                 lst1[4][1],
                                                 lst1[4][2], lst1[4][3],
                                                 lst1[4][4],
                                                 lst1[4][5], lst2[5],
                                                 lst1[5][0],
                                                 lst1[5][1], lst1[5][2],
                                                 lst1[5][3],
                                                 lst1[5][4], lst2[17], lst2[12],
                                                 lst2[13],
                                                 lst2[14], lst2[15], lst2[16])

if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
