from fileList import FileList

from PyQt5 import QtWidgets


class Lullaby(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Lullaby')

        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        settingsLayout = QtWidgets.QHBoxLayout()

        self.preview = QtWidgets.QLabel('Viewer')
        self.startButton = QtWidgets.QPushButton('START')
        self.zoomLabel = QtWidgets.QLabel('Zoom')
        self.zoomEntry = QtWidgets.QDoubleSpinBox()
        self.fileList = FileList()

        layout.addWidget(self.preview)
        layout.addWidget(self.startButton)
        settingsLayout.addWidget(self.zoomLabel)
        settingsLayout.addWidget(self.zoomEntry)
        layout.addLayout(settingsLayout)
        layout.addWidget(self.fileList)

        widget.setLayout(layout)
        self.setCentralWidget(widget)

