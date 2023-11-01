import sys
import os

from PyQt5.QtWidgets import (QApplication, QWidget, QDesktopWidget, QPushButton,
                QHBoxLayout, QVBoxLayout, QAction, QMainWindow, QToolBar,
                QMessageBox, QLineEdit, qApp, QLabel, QFileDialog)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

from task1 import create_annotation
from task2 import create_dataset2, create_annotation2
from task3 import create_dataset3, create_annotation3


class Window(QMainWindow):
    def __init__(self):

        super().__init__()

        self.initUI()

        if os.path.isdir('dataset2'):
            self.dataset2_is_created = True
        else:
            self.dataset2_is_created= False
        self.createActions()
        self.createMenuBar()
        self.createToolBar()


    def initUI(self):

        self.folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')

        self.resize(500, 450)
        self.center()
        self.setWindowTitle('Brown&Polar')
        self.setWindowIcon(QIcon('img/main_icon.png'))
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        brown_btn = QPushButton('Next Brown', self)
        polar_btn = QPushButton('Next Polar', self)

        pixmap = QPixmap('img/both.jpg')
        
        self.lbl = QLabel(self)
        #lbl.setPixmap(pixmap)
        self.lbl.setText(str(self.folderpath))

        hbox = QHBoxLayout()
        hbox.addSpacing(1)
        hbox.addWidget(brown_btn)
        hbox.addWidget(polar_btn)

        vbox = QVBoxLayout()
        vbox.addSpacing(1)
        vbox.addWidget(self.lbl)
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
    
    def createMenuBar(self):
        menuBar = self.menuBar()

        fileMenu = menuBar.addMenu('&File')

        fileMenu.addAction(self.exitAction)
        fileMenu.addAction(self.changeAction)

        annotMenu = menuBar.addMenu('&Annotation')
        annotMenu.addAction(self.createAnnotAction)
        '''
        annotMenu.addAction(self.createAnnotAction2)
        annotMenu.addAction(self.createAnnotAction3)
        '''
        dataMenu = menuBar.addMenu('&Dataset')
        dataMenu.addAction(self.createData2Action)
        if(self.dataset2_is_created is True):
            dataMenu.addAction(self.createData3Action)

      
    def createToolBar(self):
        fileToolBar = self.addToolBar('File')
        fileToolBar.addAction(self.exitAction)
    
    def createActions(self):

        self.exitAction = QAction(QIcon('img/exit.png'), '&Exit', self)
        self.exitAction.triggered.connect(qApp.quit)

        self.changeAction = QAction(QIcon('img/change.png'), '&Change directory', self)
        self.changeAction.triggered.connect(self.changeDir)

        self.createAnnotAction = QAction(QIcon('img/csv.png'), '&Create annotation for current dataset', self)
        self.createAnnotAction.triggered.connect(self.createAnnotation)
    
        self.createData2Action = QAction(QIcon('img/new_dataset.png'), '&Create dataset2', self)
        self.createData2Action.triggered.connect(self.createDataset2)

        self.createData3Action = QAction(QIcon('img/new_dataset.png'), '&Create dataset3', self)
        self.createData3Action.triggered.connect(self.createDataset3)
        
    def createAnnotation(self):
        if 'dataset2' in str(self.folderpath):
            create_annotation2()
        elif 'dataset3' in str(self.folderpath):
            create_annotation3()
        elif 'dataset' in str(self.folderpath):
            create_annotation()

    def createDataset2(self):
        self.dataset2_is_created = True
        create_dataset2()
        
    def createDataset3(self):
        create_dataset3()

    def changeDir(self):
        reply = QMessageBox.question(self, 'Warning', f'Are you sure to change current directory?\nCurrent dir: {str(self.folderpath)}',
            QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            self.folderpath = self.folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
            self.lbl.setText(str(self.folderpath))
        else:
            pass

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