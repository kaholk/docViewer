import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QSpacerItem, QLayout, QVBoxLayout, QStackedLayout, QGridLayout, QScrollArea,  QPushButton, QHBoxLayout, QSplitter, QSizePolicy
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QInputDialog, QLineEdit
import qpageview.qpageview as qpageview


from sqlalchemy import select
from databaseEngine import SessionMaker
from database.models import ProductionOrderLine, RecordLink


def createComponentBytes(component: str, tableId: int, fieldType: int) -> bytearray:
    component_bytes = bytearray()
    component_bytes += tableId.to_bytes(length=4, byteorder='little')
    component_bytes += fieldType.to_bytes(length=1, byteorder='little')
    component_bytes += "{".encode(encoding='utf-8', errors='strict')

    for idx, char in enumerate(component):
        prefix = (255).to_bytes(length=1, byteorder='little') if idx == 0 else (0).to_bytes(length=1, byteorder='little')
        component_bytes += prefix + char.encode(encoding='utf-8', errors='strict')

    # Dodanie pięciu bajtów zerowych na końcu
    component_bytes += (0).to_bytes(length=5, byteorder='little')

    return component_bytes

class FileWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.fileLinks = {
            "LC": [],
            "RYS": [],
            "IP": [],
            "PIJ": [],
            "SP": [],
            "OTHER": []
        }
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

        self.selectDocumentLayout = QHBoxLayout()
        self.selectDocumentLayout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

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
        self.cuttingListButton.clicked.connect(lambda: self.loadDocument(documentType="LC"))
        self.buttonsLayoutGroup4.addWidget(self.cuttingListButton)

        # drawing list button
        self.drawingListButton = QPushButton("RYS")
        self.drawingListButton.setFixedSize(50, 50)
        self.drawingListButton.setToolTip("Lista rysunków")
        self.drawingListButton.clicked.connect(lambda: self.loadDocument(documentType="RYS"))
        self.buttonsLayoutGroup4.addWidget(self.drawingListButton)

        # work instruction button
        self.workInstructionButton = QPushButton("IP")
        self.workInstructionButton.setFixedSize(50, 50)
        self.workInstructionButton.setToolTip("Instrukcja pracy")
        self.workInstructionButton.clicked.connect(lambda: self.loadDocument(documentType="IP"))
        self.buttonsLayoutGroup5.addWidget(self.workInstructionButton)

        # inspection instruction button
        self.inspectionInstructionButton = QPushButton("PIJ")
        self.inspectionInstructionButton.setFixedSize(50, 50)
        self.inspectionInstructionButton.setToolTip("PIJ")
        self.inspectionInstructionButton.clicked.connect(lambda: self.loadDocument(documentType="PIJ"))
        self.buttonsLayoutGroup5.addWidget(self.inspectionInstructionButton)

        # packing specification list button
        self.packingSpecificationButton = QPushButton("SP")
        self.packingSpecificationButton.setFixedSize(50, 50)
        self.packingSpecificationButton.setToolTip("Specyfikacja pakowania")
        self.packingSpecificationButton.clicked.connect(lambda: self.loadDocument(documentType="SP"))
        self.buttonsLayoutGroup6.addWidget(self.packingSpecificationButton)

        # other documents button
        self.otherDocumentsButton = QPushButton("Other")
        self.otherDocumentsButton.setFixedSize(50, 50)
        self.otherDocumentsButton.setToolTip("Pozostałe dokumenty")
        self.otherDocumentsButton.clicked.connect(lambda: self.loadDocument(documentType="OTHER"))
        self.buttonsLayoutGroup6.addWidget(self.otherDocumentsButton)

        # Dodanie układu siatki do głównego układu
        self.layout.addLayout(self.selectDocumentLayout)
        self.layout.addLayout(self.buttonsLayout)

    def setButtonsActivation(self):
        self.cuttingListButton.setEnabled(True)
        self.drawingListButton.setEnabled(True)
        self.workInstructionButton.setEnabled(True)
        self.inspectionInstructionButton.setEnabled(True)
        self.packingSpecificationButton.setEnabled(True)
        self.otherDocumentsButton.setEnabled(True)


        if len(self.fileLinks["LC"]) == 0:
            self.cuttingListButton.setDisabled(True)

        if len(self.fileLinks["RYS"]) == 0:
            self.drawingListButton.setDisabled(True)
            
        if len(self.fileLinks["IP"]) == 0:
            self.workInstructionButton.setDisabled(True)

        if len(self.fileLinks["PIJ"]) == 0:
            self.inspectionInstructionButton.setDisabled(True)

        if len(self.fileLinks["SP"]) == 0:
            self.packingSpecificationButton.setDisabled(True)

        if len(self.fileLinks["OTHER"]) == 0:
            self.otherDocumentsButton.setDisabled(True)


    def loadDocument(self, documentType="LC"):
        for i in reversed(range(self.selectDocumentLayout.count())): 
            self.selectDocumentLayout.itemAt(i).widget().setParent(None)

        for fileLink in self.fileLinks[documentType]:
            selectDocumentButton = QPushButton(fileLink["description"])
            selectDocumentButton.setToolTip(fileLink["description"])
            selectDocumentButton.setFixedHeight(50)
            # selectDocumentButton.setFixedSize(50, 50)
            selectDocumentButton.clicked.connect(lambda: self.loadFile(filePath=fileLink["fileName"]))
            self.selectDocumentLayout.addWidget(selectDocumentButton)

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
        self.mainLayout = QVBoxLayout(self.mainWidget)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)
        self.setCentralWidget(self.mainWidget)


        self.z1 = QWidget(self.mainWidget)

        self.z1Layout = QGridLayout(self.z1)
        
        self.fileWidgets = [
            FileWidget(), FileWidget()
        ]

        self.splitterWidget = QSplitter(Qt.Orientation.Horizontal)
        self.splitterWidget.setHandleWidth(5)
        
        for fileWidget in self.fileWidgets:
            self.splitterWidget.addWidget(fileWidget)

        self.z1Layout.addWidget(self.splitterWidget, 0, 0, 1, 2)

        self.downloadButton = QPushButton("Pobierz Zlecenie")
        self.downloadButton.setFixedHeight(50)
        self.downloadButton.clicked.connect(self.hangeInpputOrder)
        self.z1Layout.addWidget(self.downloadButton, 1, 0, 1, 1)

        self.fullscreenButton = QPushButton("Pełny ekran")
        self.fullscreenButton.setFixedSize(100, 50)
        self.fullscreenButton.clicked.connect(self.hangeFullscreen)
        self.z1Layout.addWidget(self.fullscreenButton, 1, 1, 1, 1)


        self.z2 = QWidget(self.mainWidget)
        self.z2Layout = QHBoxLayout(self.z2)
        self.z2Layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.sp1acer = QSpacerItem(200, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.z2Widget = QWidget()
        self.z2Widget.setMinimumWidth(200)
        self.z2Widget.setMaximumWidth(800)
        # Dodanie spacerów i z2Widget do układu
        self.z2Layout.addItem(self.sp1acer)  # Spacer
        self.z2Layout.addWidget(self.z2Widget)  # z2Widget
        self.z2Layout.addItem(self.sp1acer)  # Spacer
        
        palette = self.z2Widget.palette()
        palette.setColor(QPalette.ColorRole.Window, self.palette().color(QPalette.ColorRole.Window).darker(100))
        self.z2Widget.setAutoFillBackground(True)
        self.z2Widget.setPalette(palette)
        self.z2WidgetLayout = QVBoxLayout(self.z2Widget)
    

        self.orderInput = QLineEdit()
        self.orderInput.setStyleSheet("padding: 10px 20px;")
        self.orderInput.setFixedHeight(50)
        self.orderInput.setPlaceholderText("Wprowadź numer zamówienia")
        self.orderInput.returnPressed.connect(self.handleDownloadOrder)
        self.z2WidgetLayout.addWidget(self.orderInput)

        self.z2WidgetButtonsLayout = QHBoxLayout()

        self.btnCancel = QPushButton("Anuluj")
        self.btnCancel.setStyleSheet("padding: 10px 20px;")
        self.btnCancel.clicked.connect(self.hangeInpputOrder)
        self.z2WidgetButtonsLayout.addWidget(self.btnCancel)

        self.btnProcced = QPushButton("Zatwierdź")
        self.btnProcced.setStyleSheet("padding: 10px 20px;")
        self.btnProcced.clicked.connect(self.handleDownloadOrder)
        self.z2WidgetButtonsLayout.addWidget(self.btnProcced)
        self.z2WidgetLayout.addLayout(self.z2WidgetButtonsLayout)



        self.keyPressEvent = self.handleKeyPress
        self.resizeEvent = self.handleResize
        self.handleResize(None)

    def hangeInpputOrder(self):
        self.orderInput.clear()

        if self.z2.isVisible():
            self.z2.hide()
        else:
            self.z2.show()
            self.orderInput.setFocus()

    def handleDownloadOrder(self):
        orderNumber = self.orderInput.text()

        # fileLinks = {
        #     "LC": [
        #         {
        #             "fileName": "file1.pdf",
        #             'description': "Rysunek etykietowy  REV1(RED2024-04-04)(17-02-2025)"
        #         },
        #         {
        #             "fileName": "file2.pdf",
        #             'description': "LC 2Rysunek etykietowy  REV1(RED2024-04-04)(17-02-2025)"
        #         },
        #         {
        #             "fileName": "file3.pdf",
        #             'description': "Rysunek etykietowy  REV1(RED2024-04-04)(17-02-2025)"
        #         }
        #     ],
        #     "RYS": [],
        #     "IP": [],
        #     "PIJ": [],
        #     "SP": [],
        #     "OTHER": []
        # }
        fileLinks = {
            "LC": [],
            "RYS": [],
            "IP": [],
            "PIJ": [],
            "SP": [],
            "OTHER": []
        }
        with SessionMaker() as session:
            order = session.scalar(select(ProductionOrderLine).where(ProductionOrderLine.prodOrderNo == orderNumber))
            itemBytesId = createComponentBytes(component=order.itemNo, tableId=27, fieldType=2)
            recordLinks = session.scalars(select(RecordLink).where(RecordLink.recordId == itemBytesId)).all()

            for recordLink in recordLinks:
                fileName = recordLink.url1.split('/')[-1]
                description = recordLink.description
                fileLink = {
                    "fileName": fileName,
                    'description': description
                }

                if description.startswith("LC"):
                    fileLinks["LC"].append(fileLink)
                elif description.startswith("Rysunek"):
                    fileLinks["RYS"].append(fileLink)
                elif description.startswith("IP"):
                    fileLinks["IP"].append(fileLink)
                elif description.startswith("SP"):
                    fileLinks["SP"].append(fileLink)
                elif description.startswith("QIP"):
                    fileLinks["PIJ"].append(fileLink)
                else:
                    fileLinks["OTHER"].append(fileLink)

        for fileWidget in self.fileWidgets:
            fileWidget.fileLinks = fileLinks
            fileWidget.setButtonsActivation()

        self.hangeInpputOrder()
        # print(orderNumber)

    def hangeFullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

    def handleResize(self, event):
        self.z1.setGeometry(self.rect())
        self.z2.setGeometry(self.rect())

        super().resizeEvent(event)

    def handleKeyPress(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.showNormal()
        elif event.key() == Qt.Key.Key_F11:
           self.hangeFullscreen()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())




#pyinstaller docViewer.py --noconsole --add-data "assets;assets" --icon="assets/editor.png" --name editor --noconfirm
#pyinstaller docViewer.py --noconsole --name docViewer --noconfirm