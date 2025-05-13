from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QSplitter, QPushButton, QTextEdit,
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QSizePolicy
)
from PyQt6.QtCore import Qt


class Section(QWidget):
    """Klasa reprezentująca pojedynczą sekcję w QSplitter."""
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # Kontener główny (rozszerzający się)
        self.container = QLabel("Kontener")
        self.container.setStyleSheet("background-color: lightgray; padding: 20px;")
        self.container.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout.addWidget(self.container)

        # Scroll area z przykładowymi przyciskami
        self.scroll_area = QScrollArea()
        self.scroll_area.setFixedHeight(50)
        scroll_widget = QWidget()
        scroll_layout = QHBoxLayout()

        for i in range(10):  # Przykładowe przyciski w scroll area
            button = QPushButton(f"Przycisk {i+1}")
            # button.setFixedSize(50, 50)
            scroll_layout.addWidget(button)

        scroll_widget.setLayout(scroll_layout)
        self.scroll_area.setWidget(scroll_widget)
        self.scroll_area.setWidgetResizable(True)
        layout.addWidget(self.scroll_area)

        # Sekcja przycisków nawigacyjnych i akcji
        button_area = QVBoxLayout()

        # Przycisk nawigacji - 2 wiersze
        nav_buttons_layout = QVBoxLayout()
        nav_row_1 = QHBoxLayout()
        nav_row_2 = QHBoxLayout()

        for text in ["↑", "↻", "+"]:
            button = QPushButton(text)
            button.setFixedSize(50, 50)
            nav_row_1.addWidget(button)

        for text in ["↓", "↺", "-"]:
            button = QPushButton(text)
            button.setFixedSize(50, 50)
            nav_row_2.addWidget(button)

        nav_buttons_layout.addLayout(nav_row_1)
        nav_buttons_layout.addLayout(nav_row_2)

        # Przycisk akcji - 2 wiersze
        action_buttons_layout = QVBoxLayout()
        action_row_1 = QHBoxLayout()
        action_row_2 = QHBoxLayout()

        for text in ["LC", "IP", "SP"]:
            button = QPushButton(text)
            button.setFixedSize(50, 50)
            action_row_1.addWidget(button)

        for text in ["RYS", "PIJ", "OTHER"]:
            button = QPushButton(text)
            button.setFixedSize(50, 50)
            action_row_2.addWidget(button)

        action_buttons_layout.addLayout(action_row_1)
        action_buttons_layout.addLayout(action_row_2)

        button_area.addLayout(nav_buttons_layout)
        button_area.addLayout(action_buttons_layout)
        layout.addLayout(button_area)

        self.setLayout(layout)


from PyQt6.QtWidgets import QFrame


from PyQt6.QtGui import QPalette, QColor

from PyQt6.QtCore import QRect

from PyQt6.QtWidgets import QGridLayout


from PyQt6.QtWidgets import QSpacerItem, QSizePolicy

class Popup(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 120);")
        self.setFixedSize(parent.size())  # Pobiera rozmiar rodzica

        # Kontener Popup
        self.popup_container = QWidget(self)
        self.popup_container.setFixedSize(300, 200)
        self.popup_container.setStyleSheet("""
            background-color: white;
            border-radius: 10px;
            padding: 15px;
            border: 2px solid black;
        """)

        layout = QVBoxLayout(self.popup_container)
        layout.addWidget(QLabel("Wpisz tekst:"))

        self.text_input = QTextEdit()
        self.text_input.setFixedSize(250, 50)
        layout.addWidget(self.text_input)

        button_layout = QHBoxLayout()
        self.confirm_button = QPushButton("Potwierdź")
        self.cancel_button = QPushButton("Anuluj")
        self.confirm_button.setFixedSize(100, 40)
        self.cancel_button.setFixedSize(100, 40)
        button_layout.addWidget(self.confirm_button)
        button_layout.addWidget(self.cancel_button)

        layout.addLayout(button_layout)
        self.cancel_button.clicked.connect(self.hide)

        self.center_popup_container()

    def resizeEvent(self, event):
        """Popup dynamicznie dostosowuje swój rozmiar do `MainWindow` i wyśrodkowuje `popup_container`."""
        if self.parent():
            self.setFixedSize(self.parent().size())  # Pobiera rozmiar `MainWindow`
        self.center_popup_container()  # Wyśrodkowanie
        self.update()  # Wymuszenie ponownego renderowania
        super().resizeEvent(event)

    def center_popup_container(self):
        """Wyśrodkowanie `popup_container` względem `Popup`."""
        self.popup_container.adjustSize()  # Upewnij się, że kontener zachowuje swój rozmiar
        self.popup_container.move(
            (self.width() - self.popup_container.width()) // 2,
            (self.height() - self.popup_container.height()) // 2
        )





class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplikacja PyQt6")
        self.setGeometry(100, 100, 800, 600)

        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        splitter.addWidget(Section())  # Lewa sekcja
        splitter.addWidget(Section())  # Prawa sekcja

        # Przyciski pod QSplitterem
        bottom_widget = QWidget()
        bottom_layout = QHBoxLayout()
        self.fetch_button = QPushButton("Pobierz zlecenie")
        self.fullscreen_button = QPushButton("Pełny ekran")

        bottom_layout.addWidget(self.fetch_button, 9)
        bottom_layout.addWidget(self.fullscreen_button, 1)
        bottom_widget.setLayout(bottom_layout)

        self.fetch_button.clicked.connect(self.show_popup)

        # Główny layout
        central_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.addWidget(splitter, 9)
        main_layout.addWidget(bottom_widget, 1)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Popup jako nakładka w tym samym oknie
        self.popup = Popup(self)
        self.popup.hide()

    # def resizeEvent(self, event):
    #     """Automatyczne dostosowanie `Popup` do nowego rozmiaru okna."""
    #     if not self.popup.isHidden():  # Tylko jeśli Popup jest widoczny
    #         self.popup.setFixedSize(self.size())  # Dostosowanie do nowego rozmiaru MainWindow
    #         self.popup.center_popup_container()  # Wyśrodkowanie
    #     super().resizeEvent(event)

    def show_popup(self):
        self.popup.setFixedSize(self.size())  # Dopasowanie Popup do rozmiaru okna
        self.popup.center_popup_container()  # Dynamiczne wyśrodkowanie
        self.popup.show()



app = QApplication([])
window = MainWindow()
window.show()
app.exec()
