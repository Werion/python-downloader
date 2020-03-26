import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QWidget, QShortcut, QLabel, QApplication, QHBoxLayout
import winsound

class Window(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

        self.label = QLabel("Try Ctrl+O", self)
        self.shortcut = QShortcut(QKeySequence("Ctrl+O"), self)
        self.shortcut.activated.connect(self.on_open)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)
        self.resize(150, 100)
        self.show()

    @pyqtSlot()
    def on_open(self):
        print("Opening!")
        winsound.PlaySound('play_output.wav', winsound.SND_FILENAME)

app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())