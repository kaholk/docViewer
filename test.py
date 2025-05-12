from PyQt6.QtWidgets import QApplication, QMainWindow, QSplitter, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QScrollArea, QSizePolicy
from PyQt6.QtCore import Qt
import sys

class SectionWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        section_layout = QVBoxLayout()

        # Element zajmujący większość przestrzeni (dynamicznie rozszerzający się)
        main_element = QWidget()
        main_element.setStyleSheet("background-color: lightgray; min-height: 200px;")
        main_element.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # ScrollArea z poziomo przewijanymi przyciskami (stała wysokość)
        scroll_area = QScrollArea()
        scroll_widget = QWidget()
        scroll_layout = QHBoxLayout(scroll_widget)

        for i in range(10):
            button = QPushButton(f"Przycisk {i+1}")
            scroll_layout.addWidget(button)

        scroll_area.setWidget(scroll_widget)
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        scroll_area.setFixedHeight(50)

        # Pozostałe przyciski - podzielone na dwie sekcje (na lewo i na prawo)
        extra_buttons_container = QWidget()
        extra_buttons_container.setContentsMargins(0, 0, 0, 0)
        extra_buttons_layout = QHBoxLayout()
        extra_buttons_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        nav_buttons = ["↑", "↓", "↻", "↺", "+", "-"]
        action_buttons = ["LC", "RYS", "IP", "PIJ", "SP", "OTHER"]

        nav_layout = QVBoxLayout()
        action_layout = QVBoxLayout()

        # Tworzenie przycisków nawigacyjnych (lewa strona, dwa wiersze)
        for i in range(0, len(nav_buttons), 3):  # Po trzy w wierszu
            row_layout = QHBoxLayout()
            for label in nav_buttons[i:i+3]:
                button = QPushButton(label)
                button.setFixedSize(50, 50)
                button.setToolTip(f"Nawigacja: {label}")
                button.clicked.connect(lambda _, l=label: self.handle_nav_action(l))
                row_layout.addWidget(button)
            nav_layout.addLayout(row_layout)

        # Tworzenie przycisków akcji (prawa strona, dwa wiersze)
        for i in range(0, len(action_buttons), 3):  # Po trzy w wierszu
            row_layout = QHBoxLayout()
            for label in action_buttons[i:i+3]:
                button = QPushButton(label)
                button.setFixedSize(50, 50)
                button.setToolTip(f"Akcja: {label}")
                button.clicked.connect(lambda _, l=label: self.handle_action(l))
                row_layout.addWidget(button)
            action_layout.addLayout(row_layout)

        extra_buttons_layout.addLayout(nav_layout)  # Przyciski nawigacji po lewej
        extra_buttons_layout.addLayout(action_layout)  # Przyciski akcji po prawej
        extra_buttons_container.setLayout(extra_buttons_layout)

        section_layout.addWidget(main_element, 1)
        section_layout.addWidget(scroll_area, 0)
        section_layout.addWidget(extra_buttons_container, 0)

        self.setLayout(section_layout)

    def handle_nav_action(self, action):
        print(f"Wykonano nawigację: {action}")

    def handle_action(self, action):
        print(f"Wykonano akcję: {action}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Schemat aplikacji PyQt6")
        self.setGeometry(100, 100, 800, 600)

        # Główny QSplitter (poziomy podział)
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # Dodanie sekcji do Splittera
        splitter.addWidget(SectionWidget())
        splitter.addWidget(SectionWidget())

        # Przyciski "Pobierz zlecenie" i "Pełny ekran"
        button_layout = QHBoxLayout()
        get_order_button = QPushButton("Pobierz zlecenie")
        full_screen_button = QPushButton("Pełny ekran")


        button_layout.addWidget(get_order_button, 9)
        button_layout.addWidget(full_screen_button, 1)

        button_container = QWidget()
        button_container.setContentsMargins(0, 0, 0, 0)
        button_container.setLayout(button_layout)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(splitter, 1)
        main_layout.addWidget(button_container, 0)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
