from board import Board, check_valid
from typing import Callable
from board import *
from copy import deepcopy
from queue import PriorityQueue
from board import check_valid, is_solved
from math import sqrt
from pygame_draw import  draw_intermediate, draw_final
import time

node_count = 0

"""

Classes
----------
BoardState


Functions
----------
bfs
dfs
ids
ucs
greedy
a_star

"""


class BoardState:
    """
    A class to represent a state of the board.

    ...

    Attributes
    ----------
    goal_x : int
        x coordinate of the goal spot
    goal_y : int
        y coordinate of the goal spot
    x : int
        x coordinate of the current spot
    y : int
        y coordinate of the current spot
    board : Board
        current content of the board
    previous_node : BoardState
        the previous state in the path
    next_node : BoardState
        the next state in the path

    Methods
    -------
    """

    def __init__(self, pos, board: Board, previous_node=None, next_node=None) -> None:
        """
        Constructs all the necessary attributes for the BoardState object.

        ...

        Parameters
        ----------
        goal_x : int
            x coordinate of the goal spot
        goal_y : int
            y coordinate of the goal spot
        x : int
            x coordinate of the current spot
        y : int
            y coordinate of the current spot
        board : Board
            current content of the board
        previous_node : BoardState
            the previous state in the path
        next_node : BoardState
            the next state in the path

        """
        self.goal_y, self.goal_x = board.goal
        self.y, self.x = pos
        self.board = board
        self.previous_node = previous_node
        self.next_node = next_node

    def __eq__(self, __o: object) -> bool:
        """
        Checks if two BoardStates are the same

        """
        return isinstance(__o, BoardState) and self.board == __o.board

    def __lt__(self, __o: object) -> bool:
        """
        Compares two BoardStates

        """
        return isinstance(__o, BoardState) and self.x == __o.x

    def __repr__(self):
        """
        Represents a board state by the current position's coordinates

        """
        return f"(x: {self.x}, y: {self.y})"


# Operators


def move_up(state: BoardState) -> BoardState | None:
    """
    Generate a next state where the player has gone up by one spot

        Parameters:
            state (BoardState): the current state

        Returns:
            new_state (BoardState): the state after moving up
    """
    new_pos = (state.y - 1, state.x)
    if not check_valid(state.board, new_pos):
        return
    new_board = deepcopy(state.board)
    new_board.visit(new_pos)
    newstate = BoardState(new_pos, new_board)
    newstate.previous_node = state
    return newstate


def move_down(state: BoardState) -> BoardState | None:
    """
    Generate a next state where the player has gone down by one spot

        Parameters:
            state (BoardState): the current state

        Returns:
            new_state (BoardState): the state after moving down
    """
    new_pos = (state.y + 1, state.x)
    if not check_valid(state.board, new_pos):
        return
    new_board = deepcopy(state.board)
    new_board.visit(new_pos)
    newstate = BoardState(new_pos, new_board)
    newstate.previous_node = state
    return newstate


def move_left(state: BoardState) -> BoardState | None:
    """
    Generate a next state where the player has gone left by one spot

        Parameters:
            state (BoardState): the current state

        Returns:
            new_state (BoardState): the state after moving left
    """
    new_pos = (state.y, state.x - 1)
    if not check_valid(state.board, new_pos):
        return
    new_board = deepcopy(state.board)
    new_board.visit(new_pos)
    newstate = BoardState(new_pos, new_board)
    newstate.previous_node = state
    return newstate


def move_right(state: BoardState) -> BoardState | None:
    """
    Generate a next state where the player has gone right by one spot

        Parameters:
            state (BoardState): the current state

        Returns:
            new_state (BoardState): the state after moving right
    """
    new_pos = (state.y, state.x + 1)
    if not check_valid(state.board, new_pos):
        return
    new_board = deepcopy(state.board)
    new_board.visit(new_pos)
    newstate = BoardState(new_pos, new_board)
    newstate.previous_node = state
    return newstate


def move_back(state: BoardState) -> BoardState:
    """
    Generate the state that originated the current state

        Parameters:
            state (BoardState): the current state

        Returns:
            previous (BoardState): the previous state
    """
    if state.previous_node is None:
        return state
    else:
        return state.previous_node


OPERATORS = {move_up: 1, move_down: 1, move_left: 1, move_right: 1}

# Search algorithms


def manhattan_distance(node: BoardState) -> int:
    """
    Calculate the manhattan distance between the current position and the goal

        Parameters:
            node (BoardState): the current board state
        
        Returns:
            distance (int): the manhattan distance between the current position and the goal
    """
    return abs(node.x - node.goal_x) + abs(node.y - node.goal_y)


def visited_l(node: BoardState) -> int:
    """
    Calculate the number of L shapes that have not been visited

        Parameters:
            node (BoardState): the current board state

        Returns:
            not_visited (int): the number of Ls that have not been visited
    """
    return len(node.board.all_shapes.difference(node.board.visited_shapes))


def euclidian_distance(node: BoardState) -> float:
    """
    Calculate the euclidian distance between the current position and the goal

        Parameters:
            node (BoardState): the current board state

        Returns:
            distance (float): the resulting distance
    """
    return int(sqrt(((node.goal_x - node.x) ** 2) + ((node.goal_y - node.y) ** 2)))



def bfs(start: BoardState, intermediate=True, pygame_game=False, window=None) -> list:
    """
    Run breadth-first search to find a solution to the game.

        Parameters:
            start (BoardState): the starting state
            intermediate (bool): whether or not to print intermediate boards
            pygame_game (bool): whether or not the game is being run using pygame
            window (pygame surface): the pygame surface to draw on

        Returns:
            path (list): the path from the starting state to the final state
    """
    start_time = time.time()
    global node_count
    node_count = 0
    queue = [start]
    solution = None

    while queue:
        current = queue.pop(0)
        node_count += 1
        if intermediate:
            time.sleep(0.1)
            if pygame_game:
                 draw_intermediate(window, current.board, "Breadth-First Search")
            else:
                print(current.board)
        if is_solved(
            (current.y, current.x), (current.goal_y, current.goal_x), current.board
        ):
            solution = current
            break
        for op in OPERATORS:
            next = op(current)
            if not next:
                continue
            next.previous_node = current
            queue.append(next)

    end_time = time.time()
    duration = end_time - start_time


    return get_solution_from_previous(solution, pygame_game=pygame_game, window=window, algo="Breadth-First Search", duration=duration, node_count=node_count)


def dfs(state: BoardState, max_depth: int, show_perf=True, intermediate=True, dfs=True, pygame_game=False, window=None) -> list:
    """
    Run depth-first search to find a solution to the game.

        Parameters:
            state (BoardState): the starting state
            max_depth (int): the limit of the depth to explore
            show_perf (bool): whether or not to show performance metrics
            intermediate (bool): whether or not to print intermediate boards
            dfs (bool): whether dfs was called in order to calculate using dfs. false if ids
            pygame_game (bool): whether or not the game is being run using pygame
            window (pygame surface): the pygame surface to draw on

        Returns:
            path (list): the path from the starting state to the final state
    """

    algo = "Depth-First Search"
    if not dfs:
        algo = "Iterative Deepening Search"

    global node_count
    node_count = 0
    start = time.time()
    found = dfs_rec(state, 0, max_depth, intermediate, algo=algo, pygame_game=pygame_game, window=window)
    if found:
        end = time.time()
        duration = end - start
        if show_perf:
            print("Took", duration, "seconds and visited", node_count, "nodes")
        return get_solution_from_next(state, pygame_game=pygame_game, window=window, algo=algo, duration=duration, node_count=node_count)


def dfs_rec(state: BoardState, current_depth: int, max_depth: int, intermediate=True, algo="Depth-First Search", pygame_game=False, window=None) -> bool:
    """
    Auxiliary function to run depth-first search to find a solution to the game.

        Parameters:
            state (BoardState): the state that is being currently explored
            current_depth (int): the depth of the current state
            max_depth (int): the limit of the depth to explore
            intermediate (bool): wheter or not to print intermediate boards
            algo (string): name of the algorithm that called dfs_rec
            pygame_game (bool): whether or not the game is being run using pygame
            window (pygame surface): the pygame surface to draw on

        Returns:
            found (bool): whether a solution has been found
    """
    global node_count
    node_count += 1
    if intermediate:
        time.sleep(0.1)
        if pygame_game:
            draw_intermediate(window, state.board, algo)
        else:
            print(state.board)
    if current_depth == max_depth:
        return False

    if is_solved((state.y, state.x), (state.goal_y, state.goal_x), state.board):
        return True

    for op in OPERATORS:
        next = op(state)
        if not next:
            continue
        state.next_node = next
        if dfs_rec(next, current_depth + 1, max_depth, intermediate, algo=algo, pygame_game=pygame_game, window=window):
            return True

    return False


def ids(state: BoardState, intermediate=True, pygame_game=False, window=None) -> list:
    """
    Run iterative deepening search to find a solution to the game.

        Parameters:
            state (BoardState): the starting state
            intermediate (bool): whether or not to print intermediate boards
            pygame_game (bool): whether or not the game is being run using pygame
            window (pygame surface): the pygame surface to draw on

        Returns:
            path (list): the path from the starting state to the final state
    """
    global node_count
    node_count = 0
    start = time.time()
    depth = 0
    while True:
        if intermediate:
            time.sleep(0.1)
            if pygame_game:
                draw_intermediate(window, state.board, "Iterative Deepening Search")
            else:
                print(state.board)
        if not dfs(state, depth, False, intermediate, dfs=False, pygame_game=pygame_game, window=window):
            depth += 1
        else:
            end = time.time()
            duration = end - start

            return get_solution_from_next(state, False, pygame_game=pygame_game, window=window, algo="Iterative Deepening Search", duration=duration, node_count=node_count)


def ucs(start: BoardState, intermediate=True, pygame_game=False, window=None) -> list:
    """
    Run uniform cost search to find a solution to the game.

        Parameters:
            state (BoardState): the starting state
            intermediate (bool): whether or not to print intermediate boards
            pygame_game (bool): whether or not the game is being run using pygame
            window (pygame surface): the pygame surface to draw on

        Returns:
            path (list): the path from the starting state to the final state
    """
    start_time = time.time()
    global node_count
    node_count = 0
    queue = PriorityQueue()
    queue.put((0, [start]))

    while queue:
        pair = queue.get()
        current = pair[1][-1]
        node_count += 1
        if intermediate:
            time.sleep(0.1)
            if pygame_game:
                draw_intermediate(window, current.board, "Uniform Cost Search")
            else:
                print(current.board)
        if is_solved(
            (current.y, current.x), (current.goal_y, current.goal_x), current.board
        ):
            solution = current
            break
        for op in OPERATORS:
            nextstate = op(current)
            if not nextstate:
                continue
            nextstate.previous_node = current
            queue.put((pair[0] + OPERATORS[op], [nextstate]))

    end_time = time.time()
    duration = end_time - start_time

    return get_solution_from_previous(solution, True, pygame_game=pygame_game, window=window, algo="Uniform Cost Search", duration=duration, node_count=node_count)


def greedy(start: BoardState, heuristic: Callable[[BoardState], int | float], intermediate=True, pygame_game=False, window=None) -> list:
    """
    Run greedy search to find a solution to the game.

        Parameters:
            state (BoardState): the starting state
            heuristic (function): the heuristic function
            intermediate (bool): whether or not to print intermediate boards
            pygame_game (bool): whether or not the game is being run using pygame
            window (pygame surface): the pygame surface to draw on

        Returns:
            path (list): the path from the starting state to the final state
    """

    start_time = time.time()
    global node_count
    node_count = 0
    queue = PriorityQueue()
    queue.put((100, [start]))

    while queue:
        pair = queue.get()
        current = pair[1][-1]
        node_count += 1
        if intermediate:
            time.sleep(0.1)
            if pygame_game:
                draw_intermediate(window, current.board, "Greedy Search", heuristic)
            else:
                print(current.board)
        if is_solved(
            (current.y, current.x), (current.goal_y, current.goal_x), current.board
        ):
            solution = current
            break
        for op in OPERATORS:
            nextstate = op(current)
            if not nextstate:
                continue
            nextstate.previous_node = current
            queue.put((heuristic(nextstate), [nextstate]))

    end_time = time.time()
    duration = end_time - start_time

    return get_solution_from_previous(solution, pygame_game=pygame_game, window=window, algo="Greedy Search", heuristic=heuristic, duration=duration, node_count=node_count)


def a_star(start: BoardState, heuristic: Callable[[BoardState], int | float], intermediate=True, pygame_game=False, window=None) -> list:
    """
    Run a* search to find a solution to the game.

        Parameters:
            state (BoardState): the starting state
            heuristic (function): the heuristic function
            intermediate (bool): whether or not to print intermediate boards
            pygame_game (bool): whether or not the game is being run using pygame
            window (pygame surface): the pygame surface to draw on

        Returns:
            path (list): the path from the starting state to the final state
    """
    start_time = time.time()
    global node_count
    node_count = 0
    queue = PriorityQueue()
    queue.put((100, [start]))

    while queue:
        pair = queue.get()
        node_count += 1
        current = pair[1][-1]
        if intermediate:
            time.sleep(0.1)
            if pygame_game:
                draw_intermediate(window, current.board, "A* Search", heuristic)
            else:
                print(current.board)
        if is_solved(
            (current.y, current.x), (current.goal_y, current.goal_x), current.board
        ):
            solution = current
            break
        for op in OPERATORS:
            nextstate = op(current)
            if not nextstate:
                continue
            nextstate.previous_node = current
            queue.put((OPERATORS[op] + pair[0] + heuristic(nextstate), [nextstate]))

    end_time = time.time()
    duration = end_time - start_time

    return get_solution_from_previous(solution, pygame_game=pygame_game, window=window, algo="A* Search", heuristic=heuristic, duration=duration, node_count=node_count)


def get_solution_from_next(state: BoardState, show: bool = True, pygame_game=False, window=None, algo=None, heuristic=None, duration=0, node_count=0) -> list:
    """
    Calculate the path saved in a state's next attribute

        Parameters:
            state (BoardState): starting state
            show (bool, default: True): whether or not to print the final board
            pygame_game (bool): whether or not the game is being run using pygame
            window (pygame surface): the pygame surface to draw on
            algo (string): name of the algorithm that called dfs_rec
            heuristic (function): the heuristic function
            duration (int): the time it took to find the solution
            node_count (int): number of nodes visited

        Returns:
            path (list): the path from the starting state to the final state
    """
    
    path = []
    while state:
        path.append(state)
        state = state.next_node
    if show:
        print("Took", duration, "seconds and visited", node_count, "nodes")
        if pygame_game:
            draw_final(window, path[-1].board, duration, node_count, algo)
        else:
            print(path[-1].board)
    return path


def get_solution_from_previous(state: BoardState, show=True, pygame_game=False, window=None, algo=None, heuristic=None, duration=0, node_count=0) -> list:
    """
    Calculate the path saved in a state's previous attribute

        Parameters:
            state (BoardState): final state
            show (bool, default: True): whether or not to print the final board
            pygame_game (bool): whether or not the game is being run using pygame
            window (pygame surface): the pygame surface to draw on
            algo (string): name of the algorithm that called dfs_rec
            heuristic (function): the heuristic function
            duration (int): the time it took to find the solution
            node_count (int): number of nodes visited

        Returns:
            path (list): the path from the starting state to the final state
    """
    path = []
    if state:
        if show:
            print("Took", duration, "seconds and visited", node_count, "nodes")
            if pygame_game:
                draw_final(window, state.board, duration, node_count, algo)
            else:
                print(state.board)
        while state:
            path.append(state)
            state = state.previous_node

    return list(reversed(path))

def run_perf_test(pygame_game=False, window=None):
    """
    Run set of tests for each algorithm on a set board to compare them

        Parameters:
            pygame_game (bool): whether or not the game is being run using pygame
            window (pygame surface): the pygame surface to draw on
    """
    board = generate_board(1)
    board_state = BoardState(board.start, board)
    algs = {bfs, dfs, ids, ucs, greedy, a_star}
    print("BFS")
    bfs(board_state, False, pygame_game=pygame_game, window=window)
    board.reset()
    print("DFS")
    dfs(board_state, 20, True, False, pygame_game=pygame_game, window=window)
    board.reset()
    print("IDS")
    ids(board_state, False, pygame_game=pygame_game, window=window)
    board.reset()
    print("UCS")
    ucs(board_state, False, pygame_game=pygame_game, window=window)
    board.reset()
    print("GREEDY - MANHATTAN")
    greedy(board_state, manhattan_distance, False, pygame_game=pygame_game, window=window)
    board.reset()
    print("GREEDY - EUCLIDEAN")
    greedy(board_state, euclidian_distance, False, pygame_game=pygame_game, window=window)
    board.reset()
    print("GREEDY - VISITED LS")
    greedy(board_state, visited_l, False, pygame_game=pygame_game, window=window)
    board.reset()
    print("A* - MANHATTAN")
    a_star(board_state, manhattan_distance, False, pygame_game=pygame_game, window=window)
    board.reset()
    print("A* - EUCLIDEAN")
    a_star(board_state, euclidian_distance, False, pygame_game=pygame_game, window=window)
    board.reset()
    print("A* - VISITED LS")
    a_star(board_state, visited_l, False, pygame_game=pygame_game, window=window)