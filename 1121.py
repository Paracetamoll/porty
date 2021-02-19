from PyQt5.QtWidgets import QGraphicsView, QPushButton
from PyQt5 import Qt
import random


class MainWindow(Qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 200, 700, 670)
        self.setWindowTitle('Cлучайные окружности')

        self.gr = QGraphicsView(self)
        self.gr.setGeometry(10, 10, 680, 550)

        self.btn = QPushButton('Случайный круг.', self)
        self.btn.setGeometry(275, 570, 150, 80)

        self.scene = Qt.QGraphicsScene()
        self.gr.setScene(self.scene)
        self.btn.clicked.connect(self.run)

    def run(self):
        b = random.randrange(0, 250)
        c = (Qt.Qt.red, Qt.Qt.blue, Qt.Qt.yellow, Qt.Qt.green, Qt.Qt.black, Qt.Qt.darkYellow,
             Qt.Qt.gray, Qt.Qt.cyan, Qt.Qt.darkBlue, Qt.Qt.darkCyan, Qt.Qt.darkGray,
             Qt.Qt.darkGreen, Qt.Qt.magenta, Qt.Qt.darkMagenta, Qt.Qt.transparent,
             Qt.Qt.lightGray, Qt.Qt.darkRed)
        rect = Qt.QRectF(random.randrange(0, 450) - b, random.randrange(0, 250) - b, b, b)
        cc = random.randrange(0, 14)
        color = c[cc]
        self.scene.addEllipse(rect, Qt.QPen(color), Qt.QBrush(color))


if __name__ == '__main__':
    app = Qt.QApplication([])
    mw = MainWindow()
    mw.show()
    app.exec()
