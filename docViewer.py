import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout,  QPushButton, QHBoxLayout, QSplitter
from PyQt6.QtCore import Qt
import qpageview.qpageview as qpageview


class FileWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # Tworzenie układu pionowego
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # Tworzenie widoku plików
        self.fileView = qpageview.View()
        self.fileView.kineticScrollingEnabled = False
        self.layout.addWidget(self.fileView)


        # Tworzenie układu siatki z 2 wierszami
        self.buttonsGridLayout = QGridLayout()
        self.buttonsGridLayout.setContentsMargins(0, 0, 0, 0)
        # self.buttonsGridLayout.setSpacing(0)
        self.buttonsGridLayout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        # self.buttonsGridLayout.setSpacing(5)

        # Tworzenie przycisków powiększania i pomniejszania
        # self.buttonsLayout = QVBoxLayout()
        # self.buttonsLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        #page up button
        self.pageUpButton = QPushButton("↑")
        self.pageUpButton.setFixedSize(50, 50)
        self.pageUpButton.setToolTip("Poprzednai strona")
        self.pageUpButton.clicked.connect(self.pageUp)
        self.buttonsGridLayout.addWidget(self.pageUpButton, 0, 0)

        #page down button
        self.pageDownButton = QPushButton("↓")
        self.pageDownButton.setFixedSize(50, 50)
        self.pageDownButton.setToolTip("Następna strona")
        self.pageDownButton.clicked.connect(self.pageDown)
        self.buttonsGridLayout.addWidget(self.pageDownButton, 1, 0)

        # rotate right button
        self.rotateRightButton = QPushButton("↻")
        self.rotateRightButton.setFixedSize(50, 50)
        self.rotateRightButton.setToolTip("Obróć w prawo")
        self.rotateRightButton.clicked.connect(self.rotateRight)
        self.buttonsGridLayout.addWidget(self.rotateRightButton, 0, 1)


        # rotate left button
        self.rotateLeftButton = QPushButton("↺")
        self.rotateLeftButton.setFixedSize(50, 50)
        self.rotateLeftButton.setToolTip("Obróć w lewo")
        self.rotateLeftButton.clicked.connect(self.rotateLeft)
        self.buttonsGridLayout.addWidget(self.rotateLeftButton, 1, 1)
        

        # zoom in button
        self.zoomInButton = QPushButton("+")
        self.zoomInButton.setFixedSize(50, 50)
        self.zoomInButton.setToolTip("Powiększ")
        self.zoomInButton.clicked.connect(self.zoomIn)
        self.buttonsGridLayout.addWidget(self.zoomInButton, 0, 2)

        # zoom out button
        self.zoomOutButton = QPushButton("-")
        self.zoomOutButton.setFixedSize(50, 50)
        self.zoomOutButton.setToolTip("Pomniejsz")
        self.zoomOutButton.clicked.connect(self.zoomOut)
        self.buttonsGridLayout.addWidget(self.zoomOutButton, 1, 2)

        # cutting list button
        self.cuttingListButton = QPushButton("LC")
        self.cuttingListButton.setFixedSize(50, 50)
        self.cuttingListButton.setToolTip("Lista cięcia")
        self.cuttingListButton.clicked.connect(lambda: print("Cutting List"))
        self.buttonsGridLayout.addWidget(self.cuttingListButton, 0, 3)

        # drawing list button
        self.drawingListButton = QPushButton("RYS")
        self.drawingListButton.setFixedSize(50, 50)
        self.drawingListButton.setToolTip("Lista rysunków")
        self.drawingListButton.clicked.connect(lambda: print("Drawing List"))
        self.buttonsGridLayout.addWidget(self.drawingListButton, 1, 3)

        # work instruction button
        self.workInstructionButton = QPushButton("IP")
        self.workInstructionButton.setFixedSize(50, 50)
        self.workInstructionButton.setToolTip("Instrukcja pracy")
        self.workInstructionButton.clicked.connect(lambda: print("Work Instruction"))
        self.buttonsGridLayout.addWidget(self.workInstructionButton, 0, 4)

        # PIJ button
        self.pijButton = QPushButton("PIJ")
        self.pijButton.setFixedSize(50, 50)
        self.pijButton.setToolTip("PIJ")
        self.pijButton.clicked.connect(lambda: print("PIJ"))
        self.buttonsGridLayout.addWidget(self.pijButton, 1, 4)

        # packing specification list button
        self.packingSpecificationButton = QPushButton("SP")
        self.packingSpecificationButton.setFixedSize(50, 50)
        self.packingSpecificationButton.setToolTip("Specyfikacja pakowania")
        self.packingSpecificationButton.clicked.connect(lambda: print("Packing Specification"))
        self.buttonsGridLayout.addWidget(self.packingSpecificationButton, 0, 5)

        # Dodanie układu siatki do głównego układu
        self.layout.addLayout(self.buttonsGridLayout)

    def zoomIn(self):
        self.fileView.zoomIn()

    def zoomOut(self):
        self.fileView.zoomOut()

    def pageUp(self):
        self.fileView.gotoNextPage()
    
    def pageDown(self):
        self.fileView.gotoPreviousPage()
    
    def rotateLeft(self):
        self.fileView.rotateLeft()

    def rotateRight(self):
        self.fileView.rotateRight()

    def loadFile(self, filePath: str):
        # Wczytanie pliku PDF lub obrazu
        try:
            if filePath.endswith(".pdf"):
                self.fileView.loadPdf(filePath)
            elif filePath.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
                self.fileView.loadImages([filePath])
            else:
                raise ValueError(f"Unsupported file format: {filePath}")
        except Exception as e:
            print(f"Error loading file {filePath}: {e}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DocViewer")
        self.setGeometry(100, 100, 800, 600)

        # Tworzenie głównego widżetu i układu
        self.mainWidget = QWidget()
        self.setCentralWidget(self.mainWidget)
        self.layout = QVBoxLayout(self.mainWidget)

        # Tworzenie widoków plików
        self.fileViews = [FileWidget(self.mainWidget), FileWidget(self.mainWidget)]

        # Tworzenie podzielonego widoku
        self.splitterWidget = QSplitter(Qt.Orientation.Horizontal, self.mainWidget)
        self.splitterWidget.setContentsMargins(0, 0, 0, 0)
        self.splitterWidget.setHandleWidth(10)
        self.splitterWidget.setChildrenCollapsible(False)

        # Dodanie widoków plików do podzielonego widoku
        for fileView in self.fileViews:
            self.splitterWidget.addWidget(fileView)

        # Dodanie podzielonego widoku do głównego układu
        self.layout.addWidget(self.splitterWidget)

        self.downloadOrderButton = QPushButton("Pobierz zlecenie")
        self.downloadOrderButton.setStyleSheet("padding: 10px;")
        self.layout.addWidget(self.downloadOrderButton)

        self.fullScreenButton = QPushButton("Pełny ekran")
        self.fullScreenButton.setStyleSheet("padding: 10px;")
        self.fullScreenButton.clicked.connect(self.changeFullscreen)
        self.layout.addWidget(self.fullScreenButton)

        # Wczytanie plików do widoków
        self.fileViews[0].loadFile("assets/wniosek.pdf")
        self.fileViews[1].loadFile("assets/wniosek.pdf")

        # Obsługa klawisza ESC do wyjścia z trybu pełnoekranowego
        self.keyPressEvent = self.handleKeyPress

    def changeFullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

    def handleKeyPress(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.showNormal()
        elif event.key() == Qt.Key.Key_F11:
           self.changeFullscreen()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())




#pyinstaller docViewer.py --noconsole --add-data "assets;assets" --icon="assets/editor.png" --name editor --noconfirm
#pyinstaller docViewer.py --noconsole --name docViewer --noconfirm