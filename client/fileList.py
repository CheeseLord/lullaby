from PyQt5 import QtCore, QtWidgets


class FileList(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QGridLayout()

        label = QtWidgets.QLabel('Files')
        label.setAlignment(QtCore.Qt.AlignHCenter)

        self.layout.addWidget(label, 0, 0, 1, -1)

        self.setLayout(self.layout)

