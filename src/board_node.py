from .board import Board


class BoardNode:
    def __init__(self, board: Board, previousNode=None) -> None:
        self.board = board
        self.previousNode = previousNode
        self.children = self.calculateChildren()

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BoardNode) and self.board == __o.board

    def calculateChildren(self):
        pass
