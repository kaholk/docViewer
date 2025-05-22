import sys
import fitz  # PyMuPDF
from PyQt6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem, QPushButton, QVBoxLayout, QWidget, QHBoxLayout
from PyQt6.QtGui import QPixmap, QImage, QWheelEvent
from PyQt6.QtCore import Qt


class PDFViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.pdf_document = None
        self.current_page = 0
        self.view_mode = "single"  # Domyślny tryb: pojedyncza strona

        # Graphics View
        self.scene = QGraphicsScene()
        self.view = PDFGraphicsView(self.scene)
        self.view.setRenderHint(self.view.renderHints().Antialiasing)

        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.view)
        self.setLayout(layout)

    def load_pdf(self, file_path, viev_mode="single"):
        self.pdf_document = fitz.open(file_path)
        self.current_page = 0
        self.view_mode = "all"
        self.display_page()
        self.view.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)  # Naprawienie interaktywnego przeciągania

    def clear_pdf(self):
        self.scene.clear()

    def display_page(self):
        if self.pdf_document:
            self.scene.clear()

            zoom_factor = max(2.0, self.view.scale_factor * 1.5)  # Dynamiczne skalowanie DPI
            rotation_angle = self.view.rotation_angle  # Pobieranie aktualnego kąta obrotu

            if self.view_mode == "single":
                page = self.pdf_document[self.current_page]
                pix = page.get_pixmap(matrix=fitz.Matrix(zoom_factor, zoom_factor).prerotate(rotation_angle))  # Obrót strony
                image = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format.Format_RGB888)
                pixmap = QPixmap.fromImage(image)

                self.pixmap_item = QGraphicsPixmapItem(pixmap)
                self.scene.addItem(self.pixmap_item)

                self.view.setSceneRect(0, 0, pix.width, pix.height)

            elif self.view_mode == "all":
                y_offset = 0
                for page in self.pdf_document:
                    pix = page.get_pixmap(matrix=fitz.Matrix(zoom_factor, zoom_factor).prerotate(rotation_angle))  # Obrót strony
                    image = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format.Format_RGB888)
                    pixmap = QPixmap.fromImage(image)

                    item = QGraphicsPixmapItem(pixmap)
                    item.setPos(0, y_offset)
                    self.scene.addItem(item)
                    y_offset += pix.height + 10  # Odstęp między stronami

                self.view.setSceneRect(0, 0, pix.width, y_offset)




    def prev_page(self):
        if self.pdf_document and self.current_page > 0 and self.view_mode == "single":
            self.current_page -= 1
            self.display_page()

    def next_page(self):
        if self.pdf_document and self.current_page < len(self.pdf_document) - 1 and self.view_mode == "single":
            self.current_page += 1
            self.display_page()
            
    def rotate_page(self, direction):
        """Obraca stronę o 90 stopni w lewo lub prawo"""
        if direction == "left":
            self.view.rotation_angle -= 90  # Obrót w lewo
        elif direction == "right":
            self.view.rotation_angle += 90  # Obrót w prawo
        self.display_page()  # Ponowne wyświetlenie strony po obrocie


    def zoom_in(self):
        self.view.zoom_in()

    def zoom_out(self):
        self.view.zoom_out()

    def set_view_mode(self, mode):
        """Zmiana trybu wyświetlania"""
        if mode in ["single", "all"]:
            self.view_mode = mode
            self.display_page()
            self.view.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)  # Naprawienie interaktywnego przeciągania



class PDFGraphicsView(QGraphicsView):
    def __init__(self, scene):
        super().__init__(scene)
        self.scale_factor = 1.0  # Początkowy zoom
        self.rotation_angle = 0  # Początkowy kąt obrotu
    
    def resetFactor(self):
        self.scale_factor = 1.0
        self.rotation_angle = 0

    def wheelEvent(self, event: QWheelEvent):
        if event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            # Ctrl + Scroll -> Zoomowanie
            delta = event.angleDelta().y()
            zoom_factor = 1.1 if delta > 0 else 0.9
            self.scale_factor *= zoom_factor
            self.setTransform(self.transform().scale(zoom_factor, zoom_factor))
        elif event.modifiers() == Qt.KeyboardModifier.ShiftModifier:
            # Shift + Scroll -> Przewijanie poziome
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - event.angleDelta().y())
        else:
            # Scroll bez modyfikatora -> Przewijanie pionowe
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() - event.angleDelta().y())


    def zoom_in(self):
        self.scale_factor *= 1.1
        self.setTransform(self.transform().scale(1.1, 1.1))

    def zoom_out(self):
        self.scale_factor *= 0.9
        self.setTransform(self.transform().scale(0.9, 0.9))