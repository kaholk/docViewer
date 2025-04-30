import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QStackedLayout, QGridLayout,  QPushButton, QHBoxLayout, QSplitter
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QInputDialog
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
        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        self.buttonsLayoutGroup1 = QVBoxLayout()
        self.buttonsLayoutGroup2 = QVBoxLayout()
        self.buttonsLayoutGroup3 = QVBoxLayout()
        self.buttonsLayoutGroup4 = QVBoxLayout()
        self.buttonsLayoutGroup5 = QVBoxLayout()
        self.buttonsLayoutGroup6 = QVBoxLayout()
        
        self.buttonsLayout.addLayout(self.buttonsLayoutGroup1)
        self.buttonsLayout.addLayout(self.buttonsLayoutGroup2)
        self.buttonsLayout.addLayout(self.buttonsLayoutGroup3)
        self.buttonsLayout.addLayout(self.buttonsLayoutGroup4)
        self.buttonsLayout.addLayout(self.buttonsLayoutGroup5)
        self.buttonsLayout.addLayout(self.buttonsLayoutGroup6)
        
        #page up button
        self.pageUpButton = QPushButton("↑")
        self.pageUpButton.setFixedSize(50, 50)
        self.pageUpButton.setToolTip("Poprzednai strona")
        self.pageUpButton.clicked.connect(self.pageUp)
        self.buttonsLayoutGroup1.addWidget(self.pageUpButton)

        #page down button
        self.pageDownButton = QPushButton("↓")
        self.pageDownButton.setFixedSize(50, 50)
        self.pageDownButton.setToolTip("Następna strona")
        self.pageDownButton.clicked.connect(self.pageDown)
        self.buttonsLayoutGroup1.addWidget(self.pageDownButton)

        # rotate right button
        self.rotateRightButton = QPushButton("↻")
        self.rotateRightButton.setFixedSize(50, 50)
        self.rotateRightButton.setToolTip("Obróć w prawo")
        self.rotateRightButton.clicked.connect(self.rotateRight)
        self.buttonsLayoutGroup2.addWidget(self.rotateRightButton)

        # rotate left button
        self.rotateLeftButton = QPushButton("↺")
        self.rotateLeftButton.setFixedSize(50, 50)
        self.rotateLeftButton.setToolTip("Obróć w lewo")
        self.rotateLeftButton.clicked.connect(self.rotateLeft)
        self.buttonsLayoutGroup2.addWidget(self.rotateLeftButton)
        
        # zoom in button
        self.zoomInButton = QPushButton("+")
        self.zoomInButton.setFixedSize(50, 50)
        self.zoomInButton.setToolTip("Powiększ")
        self.zoomInButton.clicked.connect(self.zoomIn)
        self.buttonsLayoutGroup3.addWidget(self.zoomInButton)

        # zoom out button
        self.zoomOutButton = QPushButton("-")
        self.zoomOutButton.setFixedSize(50, 50)
        self.zoomOutButton.setToolTip("Pomniejsz")
        self.zoomOutButton.clicked.connect(self.zoomOut)
        self.buttonsLayoutGroup3.addWidget(self.zoomOutButton)

        # cutting list button
        self.cuttingListButton = QPushButton("LC")
        self.cuttingListButton.setFixedSize(50, 50)
        self.cuttingListButton.setToolTip("Lista cięcia")
        self.cuttingListButton.clicked.connect(lambda: print("Cutting List"))
        self.buttonsLayoutGroup4.addWidget(self.cuttingListButton)

        # drawing list button
        self.drawingListButton = QPushButton("RYS")
        self.drawingListButton.setFixedSize(50, 50)
        self.drawingListButton.setToolTip("Lista rysunków")
        self.drawingListButton.clicked.connect(lambda: print("Drawing List"))
        self.buttonsLayoutGroup4.addWidget(self.drawingListButton)

        # work instruction button
        self.workInstructionButton = QPushButton("IP")
        self.workInstructionButton.setFixedSize(50, 50)
        self.workInstructionButton.setToolTip("Instrukcja pracy")
        self.workInstructionButton.clicked.connect(lambda: print("Work Instruction"))
        self.buttonsLayoutGroup5.addWidget(self.workInstructionButton)

        # inspection instruction button
        self.inspectionInstructionButton = QPushButton("PIJ")
        self.inspectionInstructionButton.setFixedSize(50, 50)
        self.inspectionInstructionButton.setToolTip("PIJ")
        self.inspectionInstructionButton.clicked.connect(lambda: print("PIJ"))
        self.buttonsLayoutGroup5.addWidget(self.inspectionInstructionButton)

        # packing specification list button
        self.packingSpecificationButton = QPushButton("SP")
        self.packingSpecificationButton.setFixedSize(50, 50)
        self.packingSpecificationButton.setToolTip("Specyfikacja pakowania")
        self.packingSpecificationButton.clicked.connect(lambda: print("Packing Specification"))
        self.buttonsLayoutGroup6.addWidget(self.packingSpecificationButton)

        # Dodanie układu siatki do głównego układu
        self.layout.addLayout(self.buttonsLayout)

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
        self.mainWidgetLayout:QVBoxLayout = QVBoxLayout()
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainWidgetLayout)
        self.setCentralWidget(self.mainWidget)

        self.z1 = QVBoxLayout()
        self.z2 = QVBoxLayout()
        
        # Tworzenie podzielonego widoku
        self.splitterWidget = QSplitter(Qt.Orientation.Horizontal)
        self.splitterWidget.setContentsMargins(0, 0, 0, 0)
        self.splitterWidget.setHandleWidth(10)
        self.splitterWidget.setChildrenCollapsible(False)
        
        # Tworzenie widoków plików
        self.fileWidgets = [FileWidget(), FileWidget()]
        
        # Dodanie widoków plików do podzielonego widoku
        for fileView in self.fileWidgets:
            self.splitterWidget.addWidget(fileView)
            
        self.z1.addWidget(self.splitterWidget)

        # Dodanie podzielonego widoku do głównego układu
        # self.mainWidgetLayout.addWidget(self.splitterWidget)
        
        self.stackedLayout:QStackedLayout = QStackedLayout()
        self.stackedLayout.addItem(self.z1)
        # self.stackedLayout.addItem(self.z2)
        # self.stackedLayout.addWidget(self.splitterWidget)
        self.mainWidgetLayout.addLayout(self.stackedLayout)
        
        #layout for download order and fullscreen button
        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.mainWidgetLayout.addLayout(self.buttonsLayout)
        
        # download order buttin
        self.downloadOrderButton = QPushButton("Pobierz zlecenie")
        self.downloadOrderButton.setStyleSheet("padding: 10px;"),
        self.downloadOrderButton.clicked.connect(self.showInputDialog)
        self.buttonsLayout.addWidget(self.downloadOrderButton, 1)

        #fullscreen button
        self.fullScreenButton = QPushButton("Pełny ekran")
        self.fullScreenButton.setStyleSheet("padding: 10px;")
        self.fullScreenButton.setFixedWidth(100)
        self.fullScreenButton.clicked.connect(self.changeFullscreen)
        self.buttonsLayout.addWidget(self.fullScreenButton)

        # Wczytanie plików do widoków
        self.fileWidgets[0].loadFile("assets/wniosek.pdf")
        self.fileWidgets[1].loadFile("assets/wniosek.pdf")
        
        # Obsługa klawisza ESC do wyjścia z trybu pełnoekranowego
        self.keyPressEvent = self.handleKeyPress

    def showInputDialog(self):
        text, ok = QInputDialog.getText(self, "Wprowadź tekst", "Podaj dane:")
        if ok and text:
            print(f"Wprowadzono: {text}")

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