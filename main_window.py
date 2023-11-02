import sys
sys.path.append(r'C:\Users\WWolk\Desktop\DataProcessing')

from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *

from task1 import create_annotation
from task2 import create_dataset2, create_annotation2
from task3 import create_dataset3, create_annotation3
from task5 import Iterator


class Window(QMainWindow):
    def __init__(self):

        super().__init__()

        self.initUI()
        self.initIterators()
        self.createActions()
        self.createMenuBar()
        self.createToolBar()

    def initUI(self):

        self.folderpath = QFileDialog.getExistingDirectory(
            self, 'Select Folder')

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
        self.lbl.setPixmap(pixmap)
        self.lbl.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addSpacing(1)
        hbox.addWidget(brown_btn)
        hbox.addWidget(polar_btn)

        vbox = QVBoxLayout()
        vbox.addSpacing(1)
        vbox.addWidget(self.lbl)
        vbox.addLayout(hbox)

        self.centralWidget.setLayout(vbox)

        brown_btn.clicked.connect(self.nextBrown)
        polar_btn.clicked.connect(self.nextPolar)

        self.showMaximized()

    def initIterators(self):

        self.brownbears = Iterator('brownbear', 'dataset')
        self.polarbears = Iterator('polarbear', 'dataset')

    def nextBrown(self):

        lbl_size = self.lbl.size()
        next_image = next(self.brownbears)
        if next_image != None:
            img = QPixmap(next_image).scaled(
                lbl_size, aspectRatioMode=Qt.KeepAspectRatio)
            self.lbl.setPixmap(img)
            self.lbl.setAlignment(Qt.AlignCenter)
        else:
            end_image = QPixmap(
                'img/no_photo.jpg').scaled(lbl_size, aspectRatioMode=Qt.KeepAspectRatio)
            self.lbl.setPixmap(end_image)
            self.lbl.setAlignment(Qt.AlignCenter)

    def nextPolar(self):

        lbl_size = self.lbl.size()
        next_image = next(self.polarbears)
        if next_image != None:
            img = QPixmap(next_image).scaled(
                lbl_size, aspectRatioMode=Qt.KeepAspectRatio)
            self.lbl.setPixmap(img)
            self.lbl.setAlignment(Qt.AlignCenter)
        else:
            end_image = QPixmap(
                'img/no_photo.jpg').scaled(lbl_size, aspectRatioMode=Qt.KeepAspectRatio)
            self.lbl.setPixmap(end_image)
            self.lbl.setAlignment(Qt.AlignCenter)

    def center(self):

        widget_rect = self.frameGeometry()
        pc_rect = QDesktopWidget().availableGeometry().center()
        widget_rect.moveCenter(pc_rect)
        self.move(widget_rect.center())

    def createMenuBar(self):

        menuBar = self.menuBar()

        self.fileMenu = menuBar.addMenu('&File')
        self.fileMenu.addAction(self.exitAction)
        self.fileMenu.addAction(self.changeAction)

        self.annotMenu = menuBar.addMenu('&Annotation')
        self.annotMenu.addAction(self.createAnnotAction)

        self.dataMenu = menuBar.addMenu('&Dataset')
        self.dataMenu.addAction(self.createData2Action)

    def createToolBar(self):

        fileToolBar = self.addToolBar('File')
        fileToolBar.addAction(self.exitAction)

        annotToolBar = self.addToolBar('Annotation')
        annotToolBar.addAction(self.createAnnotAction)

    def createActions(self):

        self.exitAction = QAction(QIcon('img/exit.png'), '&Exit')
        self.exitAction.triggered.connect(qApp.quit)

        self.changeAction = QAction(QIcon('img/change.png'), '&Change dataset')
        self.changeAction.triggered.connect(self.changeDataset)

        self.createAnnotAction = QAction(
            QIcon('img/csv.png'), '&Create annotation for current dataset')
        self.createAnnotAction.triggered.connect(self.createAnnotation)

        self.createData2Action = QAction(
            QIcon('img/new_dataset.png'), '&Create dataset2')
        self.createData2Action.triggered.connect(self.createDataset2)

        self.createData3Action = QAction(
            QIcon('img/new_dataset.png'), '&Create dataset3')
        self.createData3Action.triggered.connect(self.createDataset3)

    def createAnnotation(self):

        if 'dataset2' in str(self.folderpath):
            create_annotation2()
        elif 'dataset3' in str(self.folderpath):
            create_annotation3()
        elif 'dataset' in str(self.folderpath):
            create_annotation()

    def createDataset2(self):

        create_dataset2()
        self.dataMenu.addAction(self.createData3Action)

    def createDataset3(self):

        create_dataset3()

    def changeDataset(self):

        reply = QMessageBox.question(self, 'Warning', f'Are you sure you want to change current dataset?\nCurrent dataset: {str(self.folderpath)}',
                                     QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.folderpath = self.folderpath = QFileDialog.getExistingDirectory(
                self, 'Select Folder')
        else:
            pass

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Warning', 'Are you sure to quit?',
                                     QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main() -> None:
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
