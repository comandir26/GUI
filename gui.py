import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QDesktopWidget, QPushButton,
                QHBoxLayout, QVBoxLayout, QAction, QMenuBar, QMainWindow, QToolBar,
                QMessageBox, QTextEdit)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):

        super().__init__()

        self.initUI()


    def initUI(self):

        self.resize(500, 450)
        self.center()
        self.setWindowTitle('Brown&Polar')
        self.setWindowIcon(QIcon('img/main_icon.png'))
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        brown_btn = QPushButton('Next Brown', self)
        polar_btn = QPushButton('Next Polar', self)
        
        text = QTextEdit()

        hbox = QHBoxLayout()
        #hbox.addStretch(1)
        hbox.addSpacing(1)
        hbox.addWidget(brown_btn)
        hbox.addWidget(polar_btn)

        vbox = QVBoxLayout()
        vbox.addSpacing(1)
        vbox.addWidget(text)
        vbox.addLayout(hbox)
        
        self.centralWidget.setLayout(vbox)
        '''
        brown_btn.clicked.connect(self.nextBrown)

        polar_btn.clicked.connect(self.nextPolar)
        '''
        self.show()

    def center(self):

        widget_rect = self.frameGeometry()
        pc_rect = QDesktopWidget().availableGeometry().center()
        widget_rect.moveCenter(pc_rect)
        self.move(widget_rect.topLeft())
    '''
    def createMenuBar(self):
        menuBar = self.menuBar()

        fileMenu = menuBar.addMenu('&File')
        editMenu = menuBar.addMenu('&Edit')
        helpMenu = menuBar.addMenu('&Help')
      
    def createToolBar(self):
        fileToolBar = self.addToolBar('File')
        fileToolBar.addAction(self.exitAction)

        annotToolBar = self.addToolBar('Annotation')
        annotToolBar.addAction(self)

    def createActions(self):

        self.exitAction = QAction('Exit', self)
        self.exitAction.setStatusTip('Exit application')
        self.exitAction.triggered.connect(self.close)

        self.annotAction = QAction('Annotation', self)
        self.annotAction.setStatusTip('Make annotation of dataset')
         #self.annotAction.triggered.connect(self.makeAnnotation)
    '''

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Warning', 'Are you sure to quit?',
            QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())