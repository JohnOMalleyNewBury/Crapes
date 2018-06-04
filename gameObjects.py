#! /usr/bin/env python
__author__ = 'John Omalley'

class Square(object):
    def __init__(self):
        self.content = -1

    def setMark(self, newMark):
        if newMark == "X":
            self.content = 1
        elif newMark == 'O':
            self.content = 2

    def getMark(self):
        if self.content == 1:
            return  'X'
        elif self.content == 2:
            return 'O'
        return None

    def isEmpty(self):
        return self.content == -1

class Board(object):
    def __init__(self):
        self.gameBoard = []
        for squareNumber in range(0, 9):
            self.gameBoard.append(Square())

    def isEmpty(self, squareNumber):
        return self.gameBoard[squareNumber].isEmpty()
