__author__ = ['Til Blechschmidt', 'Noah Peeters', 'Merlin Brandt']

import math

import numpy as np
from numba import jit

from config import BOARD_WIDTH, FIELD_EMPTY, FIELD_P1, FIELD_P2, FIELD_SWAMP
from setup import bcolors


@jit(nopython=True)
def rotate_board(b):
    return b.reshape((BOARD_WIDTH, BOARD_WIDTH)).T


@jit
def rotate_board_clockwise(board):
    return np.fliplr(rotate_board(board)).flatten()


@jit
def rotate_board_anti_clockwise(board):
    return np.flipud(rotate_board(board)).flatten()


def print_board(board):
    board_width = int(math.sqrt(len(board)))
    location = 0
    for row in range(board_width):
        print "|",
        for field in range(board_width):
            cur_loc = board[location]
            if (field == 0 or field == 23 or row == 0 or row == 23) and cur_loc == FIELD_EMPTY:
                if row == 0 or row == 23:
                    print bcolors.BASE_BLUE + '0' + bcolors.ENDC,
                else:
                    print bcolors.BASE_RED + '0' + bcolors.ENDC,
            elif cur_loc == FIELD_P1:
                print bcolors.RED + '1' + bcolors.ENDC,
            elif cur_loc == FIELD_P2:
                print bcolors.BLUE + '2' + bcolors.ENDC,
            elif cur_loc == FIELD_SWAMP:
                print bcolors.SWAMP + '3' + bcolors.ENDC,
            else:
                print "-",
            location += 1
        print "|"