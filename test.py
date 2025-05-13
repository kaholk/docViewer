from PyQt6.QtWidgets import QApplication, QMainWindow, QSplitter, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QScrollArea, QSizePolicy, QFrame, QTextEdit, QStyle, QStyleFactory, QProgressBar
from PyQt6.QtCore import Qt, QTimer, QThread, pyqtSignal

from config_menager import appConfig

class SectionWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        # główny layout sekcji
        section_layout = QVBoxLayout()
        section_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(section_layout)

        # Element zajmujący większość przestrzeni (dynamicznie rozszerzający się)
        main_element = QWidget()
        main_element.setStyleSheet("background-color: lightgray; min-height: 200px;")
        main_element.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # ScrollArea z poziomo przewijanymi przyciskami (stała wysokość)
        scroll_widget = QWidget()
        scroll_area = QScrollArea()
        scroll_area.setWidget(scroll_widget)
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll_area.setFixedHeight(50)
        scroll_area.setStyleSheet("""
            QScrollBar:horizontal {
                height: 20px;  /* Ustalona wysokość paska przewijania */
            }

        """)
        scroll_layout = QHBoxLayout(scroll_widget)
        scroll_layout.setContentsMargins(0, 0, 0, 0)
        scroll_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        scroll_layout.setSpacing(0)

        #dodanie przycisków do scrollArea
        for i in range(10):
            button = QPushButton(f"Przycisk {i+1}")
            scroll_layout.addWidget(button)

        # layout z konteneram na przyciski navigacji i akcji
        extra_buttons_layout = QHBoxLayout()
        extra_buttons_layout.setContentsMargins(0, 0, 0, 0)
        extra_buttons_layout.setSpacing(0)
        extra_buttons_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        extra_buttons_container = QWidget()
        extra_buttons_container.setLayout(extra_buttons_layout)

        nav_buttons = ["↑", "↻", "+", "↓", "↺", "-"]
        action_buttons = ["LC", "IP", "SP", "RYS", "PIJ", "OTHER"]

        #layout dla przycisków navigacji
        nav_layout = QVBoxLayout()
        nav_layout.setContentsMargins(0, 0, 0, 0)
        nav_layout.setSpacing(0)
        
        # Tworzenie przycisków nawigacyjnych (lewa strona, dwa wiersze)
        for i in range(0, len(nav_buttons), 3):  # Po trzy w wierszu
            row_layout = QHBoxLayout()
            row_layout.setContentsMargins(0, 0, 0, 0)
            row_layout.setSpacing(0)
            for label in nav_buttons[i:i+3]:
                button = QPushButton(label)
                button.setFixedSize(50, 50)
                button.setToolTip(f"Nawigacja: {label}")
                button.clicked.connect(lambda _, l=label: self.handle_nav_action(l))
                row_layout.addWidget(button)
            nav_layout.addLayout(row_layout)
        
        #layout dla przycisków akcji
        action_layout = QVBoxLayout()
        action_layout.setContentsMargins(0, 0, 0, 0)
        action_layout.setSpacing(0)

        # Tworzenie przycisków akcji (prawa strona, dwa wiersze)
        for i in range(0, len(action_buttons), 3):  # Po trzy w wierszu
            row_layout = QHBoxLayout()
            row_layout.setContentsMargins(0, 0, 0, 0)
            row_layout.setSpacing(0)
            for label in action_buttons[i:i+3]:
                button = QPushButton(label)
                button.setFixedSize(50, 50)
                button.setToolTip(f"Akcja: {label}")
                button.clicked.connect(lambda _, l=label: self.handle_action(l))
                row_layout.addWidget(button)
            action_layout.addLayout(row_layout)

        #dodanie przycisków nawigacji oraz akcji do layoutu z przyciskami
        extra_buttons_layout.addLayout(nav_layout)  # Przyciski nawigacji po lewej
        extra_buttons_layout.addLayout(action_layout)  # Przyciski akcji po prawej

        #dodanie elementów do głównego widoku
        section_layout.addWidget(main_element, 1)
        section_layout.addWidget(scroll_area, 0)
        section_layout.addWidget(extra_buttons_container, 0)
        

    def handle_nav_action(self, action):
        print(f"Wykonano nawigację: {action}")

    def handle_action(self, action):
        print(f"Wykonano akcję: {action}")


class DataDownloader(QThread):
    data_signal = pyqtSignal(str)  # Sygnał do wysyłania pobranych danych

    def __init__(self):
        super().__init__()

    def run(self):
        """ Uruchamia symulację pobierania danych """
        self.data_signal.emit(f'Pobrano dane')

class Popup(QFrame):
    def __init__(self, parent:QMainWindow=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: rgba(192, 192, 192, 150);")
        self.hide()  # Na początku ukrywamy popup

        # Tworzymy główny layout do wyśrodkowania zawartości
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # Usunięcie marginesów

        # Tworzymy kontener wewnątrz popupu
        self.container = QWidget()
        self.container.setStyleSheet("background-color: rgba(192, 192, 192, 255); border-radius: 10px; border: 1px solid gray;")
        self.container_layout = QVBoxLayout(self.container)

        self.text_input = QTextEdit()
        self.text_input.setFixedHeight(40)
        self.text_input.setPlaceholderText("Wprowadź numer zlecenia")
        self.text_input.setStyleSheet("""
            background-color: #f0f0f0;
            border: 1px solid gray;
            color: black;
            border-radius: 5px;
            font-size: 14px;
            padding: 5px;
        """)


        # Pole na błąd
        self.error_label = QLabel("testowy bład")
        self.error_label.setStyleSheet("color: red; font-size: 14px; border-radius: 0px")
        # self.error_label.setVisible(False)  # Ukrywamy na start

        # Pasek ładowania
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

        self.buttons_layout = QHBoxLayout()
        self.confirm_button = QPushButton("Potwierdź")
        self.confirm_button.clicked.connect(self.dowload_prder)
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

        self.buttons_layout.addWidget(self.confirm_button)
        self.buttons_layout.addWidget(self.cancel_button)

        self.container_layout.addWidget(self.text_input)
        self.container_layout.addWidget(self.error_label)
        self.container_layout.addWidget(self.progress_bar)
        self.container_layout.addLayout(self.buttons_layout)

        # Dodajemy kontener do layoutu, co automatycznie wyśrodkuje go
        layout.addWidget(self.container, alignment=Qt.AlignmentFlag.AlignCenter)

    def dowload_prder(self):
        self.progress_bar.show()
        self.dataDownloader = DataDownloader()
        self.dataDownloader.data_signal.connect(self.download_order_resoult)
        self.dataDownloader.start()
    
    def download_order_resoult(self, data):
        self.progress_bar.hide()
        print(data)
    
    def close_popup(self):
        self.hide()
        

    def update_popup_size(self):
        """ Aktualizuje rozmiar popupu do pełnego rozmiaru okna głównego """
        self.setGeometry(0, 0, self.parent().width(), self.parent().height())



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #ustawienie parametrów okna
        self.setWindowTitle("Monitory")
        self.setGeometry(appConfig.get('App', 'PositionX', int), appConfig.get('App', 'PositionY', int), appConfig.get('App', 'Width', int), appConfig.get('App', 'Height', int))
        self.setGeometry(100, 100, 800, 600)

        #główny kontener z layoutem
        main_widget = QWidget(self)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.setCentralWidget(main_widget)

        # QSplitter podział na lewą i prawą sekcje
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        splitter.setContentsMargins(0, 0, 0, 0)
        
        # Dodanie sekcji do Splittera
        splitter.addWidget(SectionWidget())
        splitter.addWidget(SectionWidget())

        #kontener z layoutem dla przycisków "Pobierz zlecenie" i "Pełny ekran"
        buttons_container = QWidget()
        buttons_layout = QHBoxLayout(buttons_container)
        buttons_layout.setContentsMargins(0, 0, 0, 0)

        # Przyciski "Pobierz zlecenie"
        get_order_button = QPushButton("Pobierz zlecenie")
        get_order_button.setMinimumHeight(40)
        get_order_button.clicked.connect(self.tooglePopup)
        buttons_layout.addWidget(get_order_button, 9)
        
        #Przycisk "Pełny ekran"
        full_screen_button = QPushButton("Pełny ekran")
        full_screen_button.setMinimumHeight(40)
        full_screen_button.clicked.connect(self.toogleFullscreen)
        buttons_layout.addWidget(full_screen_button, 1)

        #dodanie elementów do główego układu
        main_layout.addWidget(splitter, 1)
        main_layout.addWidget(buttons_container, 0)
        
        # popup do pobierania zlecenia
        self.popup = Popup(self)
        self.popup.show()

        # uruchom w trybie pełnoekranowym jezeli wskazuje na to konfiguracja
        if appConfig.get("App", "Fullscreen") == 'true':
            self.showFullScreen()

        # ukrycie prawego panelu jeeżeli wskazuje na to konfiguracja
        if appConfig.get("App", "SplitterSections") == '1':
            splitter.setSizes([1, 0])


    # metoda zmieniajaca tryb aplikacji pomiędzy tyrbami: pełnoekranowym a normalnym
    def toogleFullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else: self.showFullScreen()
        
    # metoda wyśetlająca i ukrywająca popup
    def tooglePopup(self):
        if self.popup.isVisible():
            self.popup.hide()
        else: self.popup.show()

    # metoda aktualizujaca rozmiar popup przy prozszerzaniu okna mainwindow
    def resizeEvent(self, a0):
        self.popup.update_popup_size()
        
# uruchomienie aplikacji
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
