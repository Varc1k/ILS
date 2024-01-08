import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


class Suprematism(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('UI.ui', self)
        self.setWindowTitle('Suprematism')
        self.pushButton.clicked.connect(self.draw_circle)
        self.show()

    def draw_circle(self):
        painter = QPainter(self)
        diameter = random.randint(20, 100)
        color = QColor(Qt.yellow)
        painter.setPen(QPen(color))
        painter.drawEllipse(random.randint(0, 500), random.randint(0, 500), diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Suprematism()
    sys.exit(app.exec_())



