#!/usr/bin/env python

from die import * 
import sys
import crapsResources_rc
from time import sleep
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import  QMainWindow, QApplication

class Craps(QMainWindow) :
    """A game of Craps."""
    die1 = die2 = None

    def __init__( self, parent=None ):
        """Build a g+ame with two dice."""

        super().__init__(parent)
        uic.loadUi("Craps.ui", self)

        self.bidSpinBox.setRange ( 1, 1000 )
        self.bidSpinBox.setSingleStep ( 5 )
        self.wins = 0
        self.losses = 0
        self.bank = 1000
        self.die1 = Die()
        self.die2 = Die()
        self.buttonText = "Roll"
        self.resultsText = "Welcome to the game of craps."
        self.firstTime = True
        self.rollingText= "No roll yet."
             #          0  1  2  3  4    5    6    7    8    9    10   11   12
        self.payouts = [0, 0, 0, 0, 2.0, 1.5, 1.2, 1.0, 1.2, 1.5, 2.0, 1.0, 0]

        self.rollButton.clicked.connect(self.rollButtonClickedHandler)

    def __str__( self ):
        """String representation for Dice.
        """

        return "Die1: %s\nDie2: %s" % ( str(self.die1),  str(self.die2) )

    def updateUI ( self ):
        self.die1View.setPixmap(QtGui.QPixmap( ":/" + str( self.die1.getValue() ) ) )
        self.die2View.setPixmap(QtGui.QPixmap( ":/" + str( self.die2.getValue() ) ) )
        self.bankValue.setText("$" + str(self.bank))
        self.winsLabel.setText(str(self.wins))
        self.lossesLabel.setText(str(self.losses))
        self.resultsLabel.setText(self.resultsText)
        self.rollingForLabel.setText(self.rollingText)
        # Add your code here to update the GUI view so it matches the game state.

		# Player asked for another roll of the dice.
    def rollButtonClickedHandler ( self ):
        self.currentBet = self.bidSpinBox.value()
        if self.currentBet > self.bank:
            self.resultsText = "You do not have that money to bet, lower your bet."
            self.updateUI()
            return
        self.totalRoll = self.die1.roll() + self.die2.roll()
        self.rollingText = "Roll: " + str(self.totalRoll)
        if self.firstTime:
            if self.totalRoll in (7, 11):
                self.wins += 1
                self.bank += self.currentBet
                self.resultsText = "You won this round!"
            elif self.totalRoll in (2, 3, 12):
                self.losses += 1
                self.bank -= self.currentBet
                self.resultsText = "You lost this round!"
            else:
                self.resultsText = "Roll again!"
                self.firstTime = False
                self.previousRoll = self.totalRoll
        else:
            if self.totalRoll == self.previousRoll:
                self.wins += 1
                self.resultsText = "You won this round!"
                self.bank += self.payouts[self.totalRoll] * self.currentBet
            else:
                self.losses += 1
                self.resultsText = "You lost this round!"
                self.bank -= self.currentBet
            self.firstTime = True

        if self.bank <= 0:
            self.resultsText = "You have lost the game, your money, and your house."
            self.rollingText = "Go get a job, hobo."
            self.rollButton.setEnabled(False)

        # Play the first roll
        self.updateUI()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    diceApp = Craps()
    diceApp.updateUI()
    diceApp.show()
    sys.exit(app.exec_())


