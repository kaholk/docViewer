from PyQt6.QtWidgets import QApplication, QMainWindow, QSplitter, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QScrollArea, QSizePolicy
from PyQt6.QtCore import Qt
import sys

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

from PyQt6.QtWidgets import QFrame
class Popup(QFrame):  # Zmieniamy `QWidget` na `QFrame`
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setFixedSize(parent.size())

        # Stylizacja poprawiona dla `QFrame`
        self.setStyleSheet("background-color: red; border: 5px solid blue;")

        # Wymuszenie odświeżenia
        # self.update()
        # self.raise_()



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #ustawienie parametrów okna
        self.setWindowTitle("Monitory")
        self.setGeometry(100, 100, 800, 600)

        # Główny QSplitter (poziomy podział)
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        splitter.setContentsMargins(0, 0, 0, 0)
        
        # Dodanie sekcji do Splittera
        splitter.addWidget(SectionWidget())
        splitter.addWidget(SectionWidget())

        # Przyciski "Pobierz zlecenie" i "Pełny ekran"
        get_order_button = QPushButton("Pobierz zlecenie")
        get_order_button.setMinimumHeight(40)
        
        full_screen_button = QPushButton("Pełny ekran")
        full_screen_button.setMinimumHeight(40)

        #layout dla przycisków z kontenerem
        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(0, 0, 0, 0)
        button_container = QWidget()
        button_container.setLayout(button_layout)
        
        #dodanie przyciskow do layoutu
        button_layout.addWidget(get_order_button, 9)
        button_layout.addWidget(full_screen_button, 1)

        #główny layout z kontenerem
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        
        #dodanie elementów do główego widoku
        main_layout.addWidget(splitter, 1)
        main_layout.addWidget(button_container, 0)
        
        self.setCentralWidget(main_widget)
        
        
        self.popup = Popup(self)
        self.popup.show()
        

if __name__ == "__main__":
    #uruchomienie aplikacji
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
