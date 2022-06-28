from lullaby import Lullaby

from PyQt5 import QtWidgets


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = Lullaby()
    win.show()
    app.instance().exec_()

