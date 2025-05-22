from PyQt6.QtWidgets import QApplication, QMainWindow, QSplitter, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QScrollArea, QSizePolicy, QFrame, QLineEdit, QProgressBar, QMessageBox
from PyQt6.QtCore import Qt, QThread, pyqtSignal

import os
import shutil
import sys

# import qpageview.qpageview as qpageview
from pdfViewer import PDFViewer

from config_menager import appConfig

from databaseEngine import DbConnector
from databaseModels import ProductionOrderLine, RecordLink
from sqlalchemy import select

class SectionWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        
        self.autoSelectCategoryPanel = "None"
        
        self.documentationFilenames = {
            "LC": [],
            "RYS": [],
            "IP": [],
            "PIJ": [],
            "SP": [],
            "OTHER": []
        }
        
        # główny layout sekcji
        self.section_layout = QVBoxLayout()
        self.section_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.section_layout)

        # element wyswetlająÍcy pdf
        self.fileView = PDFViewer()
        # self.fileView.kineticScrollingEnabled = False
        # self.fileView.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # ScrollArea z poziomo przewijanymi przyciskami (stała wysokość)
        self.scroll_widget = QWidget()
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setFixedHeight(50)
        self.scroll_area.setStyleSheet("""
            QScrollBar:horizontal {
                height: 20px;  /* Ustalona wysokość paska przewijania */
            }

        """)
        self.scroll_layout = QHBoxLayout(self.scroll_widget)
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.scroll_layout.setSpacing(0)

        # layout z konteneram na przyciski navigacji i akcji
        self.extra_buttons_layout = QHBoxLayout()
        self.extra_buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.extra_buttons_layout.setSpacing(0)
        self.extra_buttons_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.extra_buttons_container = QWidget()
        self.extra_buttons_container.setLayout(self.extra_buttons_layout)

        self.nav_buttons_text = ["↑", "↻", "+", "↓", "↺", "-"]
        self.nav_buttons: list[QPushButton] = []
        self.action_buttons_text = ["LC", "IP", "SP", "RYS", "PIJ", "OTHER"]
        self.action_buttons: list[QPushButton] = []

        #layout dla przycisków navigacji
        nav_layout = QVBoxLayout()
        nav_layout.setContentsMargins(0, 0, 0, 0)
        nav_layout.setSpacing(0)
        
        # Tworzenie przycisków nawigacyjnych (lewa strona, dwa wiersze)
        for i in range(0, len(self.nav_buttons_text), 3):  # Po trzy w wierszu
            row_layout = QHBoxLayout()
            row_layout.setContentsMargins(0, 0, 0, 0)
            row_layout.setSpacing(0)
            for label in self.nav_buttons_text[i:i+3]:
                button = QPushButton(label)
                button.setFixedSize(50, 50)
                button.setToolTip(f"Nawigacja: {label}")
                button.clicked.connect(lambda _, l=label: self.handle_nav_action(l))
                self.nav_buttons.append(button)
                row_layout.addWidget(button)
            nav_layout.addLayout(row_layout)
        
        #layout dla przycisków akcji
        action_layout = QVBoxLayout()
        action_layout.setContentsMargins(0, 0, 0, 0)
        action_layout.setSpacing(0)

        # Tworzenie przycisków akcji (prawa strona, dwa wiersze)
        for i in range(0, len(self.action_buttons_text), 3):  # Po trzy w wierszu
            row_layout = QHBoxLayout()
            row_layout.setContentsMargins(0, 0, 0, 0)
            row_layout.setSpacing(0)
            for label in self.action_buttons_text[i:i+3]:
                button = QPushButton(label)
                button.setFixedSize(50, 50)
                button.setToolTip(f"Akcja: {label}")
                button.clicked.connect(lambda _, l=label: self.handle_action(l))
                self.action_buttons.append(button)
                row_layout.addWidget(button)
            action_layout.addLayout(row_layout)

        #dodanie przycisków nawigacji oraz akcji do layoutu z przyciskami
        self.extra_buttons_layout.addLayout(nav_layout)  # Przyciski nawigacji po lewej
        self.extra_buttons_layout.addLayout(action_layout)  # Przyciski akcji po prawej

        #dodanie elementów do głównego widoku
        self.section_layout.addWidget(self.fileView, 1)
        self.section_layout.addWidget(self.scroll_area, 0)
        self.section_layout.addWidget(self.extra_buttons_container, 0)
    
    def set_documentation_file_names(self, documentationFilenames):
        self.documentationFilenames = documentationFilenames
        
        for actionn_button_idx, actionn_button_txt in enumerate(self.action_buttons_text):
            if len(self.documentationFilenames[actionn_button_txt]) == 0:
                self.action_buttons[actionn_button_idx].setDisabled(True)
            else:
                self.action_buttons[actionn_button_idx].setEnabled(True)
                if actionn_button_txt == self.autoSelectCategoryPanel:
                    self.action_buttons[actionn_button_idx].click()
                    

    def handle_nav_action(self, action):
        # "↑", "↻", "+", "↓", "↺", "-"
        if action == "↑":
            self.fileView.prev_page()
        elif action == "↓":
            self.fileView.next_page()
        elif action == "↻":
            self.fileView.rotate_page("right")
        elif action == "↺":
            self.fileView.rotate_page("left")
        elif action == "+":
            self.fileView.zoom_in()
        elif action == "-":
            self.fileView.zoom_out()

    def handle_action(self, action):
        for actionn_button_idx, actionn_button_txt in enumerate(self.action_buttons_text):
            if action == actionn_button_txt:
                self.action_buttons[actionn_button_idx].setStyleSheet("background-color: #258B4E;")
            else:
                self.action_buttons[actionn_button_idx].setStyleSheet("")
        
        # usuniecie wyszystkich przycisków w scrool_layout
        while self.scroll_layout.count():
            item = self.scroll_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
                
        scroolLayoutButtons: list[QPushButton] = []
        for documentationFile in self.documentationFilenames[action]:
            button = QPushButton(f"{documentationFile['description']}")
            button.setStyleSheet("padding: 5px 10px")
            button.clicked.connect(lambda _, fileName=documentationFile['fileName'], button=button: self.loadFile(f"tempDocumentation/{fileName}", button))
            scroolLayoutButtons.append(button)
            self.scroll_layout.addWidget(button)
        
        # autoamtyczny wybór dokumentu
        if appConfig.get("App", "AutoSelectFirstDocumentation") == 'true':
            scroolLayoutButtons[0].click()
        
    
    def loadFile(self, filePath: str, cliclkedButton: QPushButton):

        # set style to clicked button
        for buttonIdx in range(self.scroll_layout.count()):
            widget = self.scroll_layout.itemAt(buttonIdx).widget()
            if widget == cliclkedButton:
                widget.setStyleSheet("background-color: #258B4E;")
            else:
                widget.setStyleSheet("")
                
        # Wczytanie pliku PDF lub obrazu
        self.fileView.clear_pdf()
        try:
            if filePath.endswith(".pdf"):
                self.fileView.load_pdf(filePath, appConfig.get("App", "PdfViewMode"))
            # elif filePath.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
            #     self.fileView.loadImages([filePath])
            else:
                raise ValueError(f"Unsupported file format: {filePath}")
        except Exception as e:
            print(f"Error loading file {filePath}: {e}")


class DataDownloader(QThread):
    data_signal = pyqtSignal(dict)  # Sygnał do wysyłania pobranych danych
    data_error = pyqtSignal(str)  # Sygnał do wysyłania błędów

    def __init__(self, orderNumber: str):
        super().__init__()
        self.orderNumber = orderNumber.upper()
        self.filenames = []
        self.fileLinks = {
            "LC": [],
            "RYS": [],
            "IP": [],
            "PIJ": [],
            "SP": [],
            "OTHER": []
        }

    def createComponentBytesId(self, component: str, tableId: int = 27, fieldType: int = 2) -> bytearray:
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
    
    def dowloadDataFromDataBase(self):
        with DbConnector() as session:
            productionOrder = session.scalar(select(ProductionOrderLine).where(ProductionOrderLine.prodOrderNo == self.orderNumber))
            if productionOrder is None:
                raise Exception("Nie odnaleziono zlecenia")
            itemId = self.createComponentBytesId(productionOrder.itemNo)
            
            recordLinks = session.scalars(select(RecordLink).where( (RecordLink.recordId == itemId) & (RecordLink.type == 0) & (RecordLink.company == appConfig.get('BC', 'CompanyName')))).all()
            if len(recordLinks) == 0:
                raise Exception('Nie odanleziono powiązanej dokumentacji')
            
            for recordLink in recordLinks:
                fileName = recordLink.url1.split('/')[-1]
                description = recordLink.description
                
                self.filenames.append(fileName)
                fileLink = {
                    "fileName": fileName,
                    'description': description
                }

                if description.startswith("LC"):
                    self.fileLinks["LC"].append(fileLink)
                elif description.startswith("Rysunek"):
                    self.fileLinks["RYS"].append(fileLink)
                elif description.startswith("IP"):
                    self.fileLinks["IP"].append(fileLink)
                elif description.startswith("SP"):
                    self.fileLinks["SP"].append(fileLink)
                elif description.startswith("QIP"):
                    self.fileLinks["PIJ"].append(fileLink)
                else:
                    self.fileLinks["OTHER"].append(fileLink)
    
    def copy_files_by_name(self, source_dir, destination_dir, file_names):
        # Tworzenie folderu docelowego, jeśli nie istnieje
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        # Usunięcie tylko plików, które można usunąć
        for file_name in os.listdir(destination_dir):
            file_path = os.path.join(destination_dir, file_name)
            if os.path.isfile(file_path):  # Sprawdzenie, czy to plik
                try:
                    os.remove(file_path)  # Próba usunięcia pliku
                except PermissionError:
                    # print(f"Nie można usunąć pliku: {file_path} (może być otwarty)")
                    continue

        # Kopiowanie plików z listy
        for file_name in file_names:
            source_path = os.path.join(source_dir, file_name)
            destination_path = os.path.join(destination_dir, file_name)

            if os.path.exists(source_path):
                shutil.copy2(source_path, destination_path)

    def copyDocumentationToTempFolder(self):
        self.copy_files_by_name(appConfig.get('Documentation', 'Path'), 'tempDocumentation', self.filenames)
    
    def run(self):
        """ Uruchamia symulację pobierania danych """
        downloadError = False
        
        # pobierz informacje o dokumentacji z bazy
        try:
            self.dowloadDataFromDataBase()
        except Exception as e:
            downloadError = True
            self.data_error.emit(f"Bład z Bazą: {e}")
            
        # skopiuj dokumentacje do folderu tymczasowego
        try:
            self.copyDocumentationToTempFolder()
        except Exception as e:
            downloadError = True
            self.data_error.emit(f'Bład podczas pobierania dokumentacji')
        
        # jeśli wszystko przebieglo pomyslnie zwwróć dane
        if not downloadError:
            self.data_signal.emit(self.fileLinks)

class Popup(QFrame):
    data_signal = pyqtSignal(dict)
    
    def __init__(self, parent:QMainWindow=None):
        super().__init__(parent)
        
        # półprzezroczyste tło popupu
        self.setStyleSheet("background-color: rgba(192, 192, 192, 150);")
        
        # popup domyślnie ukryty
        self.hide()

        # layout dla głównego kontenera Qframe
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        #konenener z layoutem z główna zawartościa wewnątrz popup
        self.container = QWidget()
        self.container.setMinimumWidth(300)
        self.container.setStyleSheet("background-color: rgba(192, 192, 192, 255); border-radius: 10px; border: 1px solid gray;")
        self.container_layout = QVBoxLayout(self.container)
        layout.addWidget(self.container, alignment=Qt.AlignmentFlag.AlignCenter)

        # pole tekstowe gdzie można wprowadzić numer zlecenia
        self.text_input = QLineEdit()
        self.text_input.setFixedHeight(40)
        self.text_input.setPlaceholderText("Wprowadź numer zlecenia")
        self.text_input.returnPressed.connect(self.dowload_order)
        self.text_input.setStyleSheet("""
            background-color: #f0f0f0;
            border: 1px solid gray;
            color: black;
            border-radius: 5px;
            font-size: 14px;
            padding: 5px;
        """)

        # Pole na wyśwetlenie błędu, początkowo ukryte
        self.error_label = QLabel("testowy bład")
        self.error_label.setStyleSheet("color: red; font-size: 14px; border-radius: 0px")
        self.error_label.setVisible(False) 

        # Pasek ładowania, początkowo ukryte
        self.progress_bar = QProgressBar()
        self.progress_bar.setFixedHeight(20)
        self.progress_bar.setRange(0, 0)
        self.progress_bar.hide()
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 1px solid gray;
                border-radius: 5px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #4CAF50;
                width: 10px;
            }
        """)

        # layout dla przycisków "Anuluj" i "Potwierdź"
        self.buttons_layout = QHBoxLayout()
        
        # przycisk "Anuluj"
        self.cancel_button = QPushButton("Anuluj")
        self.cancel_button.clicked.connect(self.close_popup)
        self.cancel_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                font-size: 14px;
                border-radius: 5px;
                border: none;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #d32f2f;
            }
            QPushButton:pressed {
                background-color: #b71c1c;
            }
        """)
        self.buttons_layout.addWidget(self.cancel_button)
        
        
        # przycisk "Potwierdź"
        self.confirm_button = QPushButton("Potwierdź")
        self.confirm_button.clicked.connect(self.dowload_order)
        self.confirm_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 14px;
                border-radius: 5px;
                border: none;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #388E3C;
            }
        """)
        self.buttons_layout.addWidget(self.confirm_button)

        # dodanie elementów do container_layout
        self.container_layout.addWidget(self.text_input)
        self.container_layout.addWidget(self.error_label)
        self.container_layout.addWidget(self.progress_bar)
        self.container_layout.addLayout(self.buttons_layout)

    def dowload_order(self):
        self.error_label.setText("")
        self.error_label.setVisible(False)
        self.progress_bar.show()
        self.dataDownloader = DataDownloader(self.text_input.text())
        self.dataDownloader.data_signal.connect(self.download_order_resoult)
        self.dataDownloader.data_error.connect(self.download_order_error)
        self.dataDownloader.start()
    
    def download_order_resoult(self, data):
        self.progress_bar.hide()
        self.data_signal.emit(data)
    
    def download_order_error(self, error):
        self.progress_bar.hide()
        self.error_label.setText(error)
        self.error_label.setVisible(True)
    
    def show_popup(self):
        self.error_label.setText("")
        self.text_input.setText("")
        self.text_input.setFocus()
        self.show()
    
    def close_popup(self):
        self.error_label.setText("")
        self.text_input.setText("")
        self.hide()
        
    # aktualizacja popup do rozmiaru rodzica nalezy uruchomić po kazdej zmianie rozmiaru okna aby wysrodkować popup
    def update_popup_size(self):
        """ Aktualizuje rozmiar popupu do pełnego rozmiaru okna głównego """
        self.setGeometry(0, 0, self.parent().width(), self.parent().height())



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DocViewer")
        
        # utwórz plik konfiguracyjny jeśli nie istnieje
        if not os.path.exists("config.ini"):
            self.configMessageBox = QMessageBox()
            self.configMessageBox.setWindowTitle("Plik konfiguracyjny")
            self.configMessageBox.setText('Plik konfiguracyjny "config.ini" został utworzony\nAplikacja zostanie zamknięta\nSkonfiguruj ustawienia a następnie ponownie uruchom aplikacje')
            self.configMessageBox.exec()
            appConfig.apply_default_values()
            appConfig.save_config()
            sys.exit(0)
        
        self.documentationFilenames = {
            "LC": [],
            "RYS": [],
            "IP": [],
            "PIJ": [],
            "SP": [],
            "OTHER": []
        }
        
        #ustawienie parametrów okna
        self.setGeometry(appConfig.get('App', 'PositionX', int), appConfig.get('App', 'PositionY', int), appConfig.get('App', 'Width', int), appConfig.get('App', 'Height', int))

        #główny kontener z layoutem
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout(self.main_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.setCentralWidget(self.main_widget)

        # QSplitter podział na lewą i prawą sekcje
        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        self.splitter.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.splitter.setContentsMargins(0, 0, 0, 0)
        
        # Dodanie sekcji do Splittera
        self.sectionWidgets = [SectionWidget(), SectionWidget()]
        for sectionWidget in self.sectionWidgets:
            self.splitter.addWidget(sectionWidget)

        #kontener z layoutem dla przycisków "Pobierz zlecenie" i "Pełny ekran"
        self.buttons_container = QWidget()
        self.buttons_layout = QHBoxLayout(self.buttons_container)
        self.buttons_layout.setContentsMargins(0, 0, 0, 0)

        # Przyciski "Pobierz zlecenie"
        self.get_order_button = QPushButton("Pobierz zlecenie")
        self.get_order_button.setMinimumHeight(40)
        self.get_order_button.clicked.connect(self.tooglePopup)
        self.buttons_layout.addWidget(self.get_order_button, 9)
        
        #Przycisk "Pełny ekran"
        self.full_screen_button = QPushButton("Pełny ekran")
        self.full_screen_button.setMinimumHeight(40)
        self.full_screen_button.clicked.connect(self.toogleFullscreen)
        self.buttons_layout.addWidget(self.full_screen_button, 1)

        #dodanie elementów do główego układu
        self.main_layout.addWidget(self.splitter, 1)
        self.main_layout.addWidget(self.buttons_container, 0)
        
        # popup do pobierania zlecenia
        self.popup = Popup(self)
        self.popup.data_signal.connect(self.documentationReady)
        
        # uruchom w trybie pełnoekranowym jezeli wskazuje na to konfiguracja
        if appConfig.get("App", "Fullscreen") == 'true':
            self.showFullScreen()

        # ukrycie prawego panelu jeeżeli wskazuje na to konfiguracja
        if appConfig.get("App", "SplitterSections") == '1':
            self.splitter.setSizes([1, 0])
        
        # pokazanie popup po uruchomieniu do pobierania zlecenia jeżeli wskazuje na to konfiguracja
        if appConfig.get("App", "ShowPopUpOnStart") == 'true':
            self.popup.show_popup()
            
        if appConfig.get("App", "AutoSelectCategoryPanel1") != 'None':
            self.sectionWidgets[0].autoSelectCategoryPanel = appConfig.get("App", "AutoSelectCategoryPanel1")
            
        if appConfig.get("App", "AutoSelectCategoryPanel2") != 'None':
            self.sectionWidgets[1].autoSelectCategoryPanel = appConfig.get("App", "AutoSelectCategoryPanel2")
            
        

    def documentationReady(self, documentation:dict):
        self.documentationFilenames = documentation
        self.popup.close_popup()
        for sectionWidget in self.sectionWidgets:
            sectionWidget.set_documentation_file_names(documentation)
        

    # metoda zmieniajaca tryb aplikacji pomiędzy tyrbami: pełnoekranowym a normalnym
    def toogleFullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else: self.showFullScreen()
        
    # metoda wyśetlająca i ukrywająca popup
    def tooglePopup(self):
        if self.popup.isVisible():
            self.popup.close_popup()
        else: 
            self.popup.show_popup()

    # metoda aktualizujaca rozmiar popup przy prozszerzaniu okna mainwindow
    def resizeEvent(self, a0):
        self.popup.update_popup_size()
        
# uruchomienie aplikacji
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()




#kompilacja kodu źródłowego
#pyinstaller --noconfirm --noconsole --name docViewer docViewer.py