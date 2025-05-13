from PyQt6.QtWidgets import QApplication, QMainWindow, QFrame, QPushButton, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt

class PopupFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: rgba(192, 192, 192, 150); border: 2px solid black;")
        self.hide()  # Na początku ukrywamy popup

        # Tworzymy główny layout do wyśrodkowania zawartości
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # Usunięcie marginesów

        # Tworzymy kontener wewnątrz popupu
        self.container = QWidget()
        self.container.setFixedSize(400, 200)  # Rozmiar kontenera
        self.container.setStyleSheet("background-color: white; border-radius: 10px;")

        # Dodajemy kontener do layoutu, co automatycznie wyśrodkuje go
        layout.addWidget(self.container, alignment=Qt.AlignmentFlag.AlignCenter)

    def update_popup_size(self):
        """ Aktualizuje rozmiar popupu do pełnego rozmiaru okna głównego """
        self.setGeometry(0, 0, self.parent().width(), self.parent().height())

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Popup w tym samym oknie")
        self.setGeometry(200, 200, 500, 400)

        self.button = QPushButton("Otwórz popup", self)
        self.button.setGeometry(50, 50, 150, 40)
        self.button.clicked.connect(self.toggle_popup)

        self.popup = PopupFrame(self)
        self.popup.update_popup_size()  # Ustawienie początkowego rozmiaru popupu

    def resizeEvent(self, event):
        """ Dopasowanie popupu przy każdej zmianie rozmiaru okna głównego """
        self.popup.update_popup_size()

    def toggle_popup(self):
        """ Przełącza widoczność popupu """
        if self.popup.isVisible():
            self.popup.hide()
        else:
            self.popup.show()

app = QApplication([])
window = MyWindow()
window.show()
app.exec()
