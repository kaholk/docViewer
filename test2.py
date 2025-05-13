from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QSplitter, QScrollArea, QHBoxLayout, QSizePolicy, QGridLayout
from PyQt6.QtCore import Qt

class SectionWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        # Główny element zajmujący większość przestrzeni
        self.main_element = QPushButton("Główny element")
        self.main_element.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout.addWidget(self.main_element, 5)  # Większy priorytet rozmiaru

        # Obszar przewijania w poziomie z przyciskami (stała wysokość)
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll_area.setFixedHeight(60)  # Stała wysokość dopasowana do przycisków
        
        scroll_content = QWidget()
        scroll_layout = QHBoxLayout(scroll_content)
        for i in range(10):  # Przykładowe przyciski
            scroll_layout.addWidget(QPushButton(f"Przycisk {i+1}"))
        
        self.scroll_area.setWidget(scroll_content)
        layout.addWidget(self.scroll_area)

        # Dodatkowe przyciski pod obszarem przewijania
        button_container = QWidget()
        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(0, 0, 0, 0)
        
        # Sekcja nawigacji w dwóch wierszach
        nav_container = QWidget()
        nav_layout = QGridLayout()
        navigation_buttons = ["↑", "↓", "↻", "↺", "+", "-"]
        for i, text in enumerate(navigation_buttons):
            btn = QPushButton(text)
            btn.setFixedSize(50, 50)
            nav_layout.addWidget(btn, i // 3, i % 3)  # Rozmieszczenie w dwóch wierszach
        nav_container.setLayout(nav_layout)

        # Sekcja akcji w dwóch wierszach
        action_container = QWidget()
        action_layout = QGridLayout()
        action_buttons = ["LC", "RYS", "IP", "PIJ", "SP", "OTHER"]
        for i, text in enumerate(action_buttons):
            btn = QPushButton(text)
            btn.setFixedSize(50, 50)
            action_layout.addWidget(btn, i // 3, i % 3)  # Rozmieszczenie w dwóch wierszach
        action_container.setLayout(action_layout)

        button_layout.addWidget(nav_container)  # Sekcja nawigacji po lewej
        button_layout.addSpacing(10)  # Odstęp między sekcjami
        button_layout.addWidget(action_container)  # Sekcja akcji po prawej

        button_container.setLayout(button_layout)
        layout.addWidget(button_container)

        self.setLayout(layout)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)  # Eliminacja zbędnych marginesów
        main_layout.setSpacing(0)  # Usuń odstępy między elementami

        # Splitter z sekcjami
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.setContentsMargins(0, 0, 0, 0)
        splitter.setStyleSheet("border: 1px solid green; padding: 0px")
        left_section = SectionWidget()
        right_section = SectionWidget()
        splitter.addWidget(left_section)
        splitter.addWidget(right_section)
        splitter.setSizes([600, 600])  
        main_layout.addWidget(splitter, 1)

        # **Ustal, że splitter zajmuje całą przestrzeń**
        # main_layout.setStretchFactor(splitter, 1)

        # Przyciski pod splitterem
        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(0, 0, 0, 0)
        button_layout.setSpacing(5)  # Minimalny odstęp między przyciskami

        fetch_order_button = QPushButton("Pobierz zlecenie")
        fetch_order_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        fetch_order_button.setMinimumHeight(40)  

        full_screen_button = QPushButton("Pełny ekran")
        full_screen_button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        full_screen_button.setMinimumHeight(40)  

        button_layout.addWidget(fetch_order_button, 9)
        button_layout.addWidget(full_screen_button, 1)

        button_container = QWidget()
        button_container.setStyleSheet("border: 1px solid orange; padding: 0px")
        button_container.setLayout(button_layout)

        # **Usuń politykę Fixed, aby przyciski zajmowały pełną szerokość**
        button_container.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        # **Dodaj przyciski bez pozostawienia nadmiarowej przestrzeni**
        main_layout.addWidget(button_container, 0)

        self.setLayout(main_layout)





if __name__ == "__main__":
    app = QApplication([])
    window = MyApp()
    window.show()
    app.exec()
