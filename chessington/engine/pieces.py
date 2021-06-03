"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod

from chessington.engine.constants import BOARD_SIZE
from chessington.engine.data import Player, Square

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.move_count = 0
        self.player = player

    @abstractmethod
    def get_available_moves(self, board):
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)
        self.move_count += 1


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """

    def _get_direction(self):
        if self.player == Player.WHITE:
            return 1
        else:
            return -1

    def get_available_moves(self, board):
        current_square = board.find_piece(self)
        square_in_front = Square.at(
                current_square.row + self._get_direction(),
                current_square.col
            )

        available_moves = [square_in_front]
        if self.move_count == 0:
            available_moves.append(
                Square.at(
                    current_square.row + (self._get_direction() * 2),
                    current_square.col
                )
            )
        
        return [
            square for square in available_moves if
                square.col >= 0 and
                square.col < BOARD_SIZE and
                square.row >= 0 and
                square.row < BOARD_SIZE and
                not board.get_piece(square_in_front) and
                not board.get_piece(square)
        ]


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        available_moves = []
        return [square for square in available_moves if not board.get_piece(square)]


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []