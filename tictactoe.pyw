#!/usr/bin/env python

import sys
# import tictactoeResources_rc
from time import sleep
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import  QMainWindow, QApplication

class TicTacToe(QMainWindow) :
    """A game of Craps."""

    def __init__( self, parent=None ):
        """Build a g+ame with two dice."""

        super().__init__(parent)
        uic.loadUi("tictactoe.ui", self)

        self.wins = 0
        self.losses = 0

        # self.rollButton.clicked.connect(self.rollButtonClickedHandler)

    def __str__( self ):
        """String representation for Dice.
        """

        return ""

    def updateUI ( self ):
        pass
        # Add your code here to update the GUI view so it matches the game state.

		# Player asked for another roll of the dice.

        # Play the first roll

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tictactoeApp = TicTacToe()
    tictactoeApp.updateUI()
    tictactoeApp.show()
    sys.exit(app.exec_())



