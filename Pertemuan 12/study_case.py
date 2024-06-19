import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton, QColorDialog, QSpinBox, QLineEdit
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor
from PyQt6.QtCore import Qt, QPoint

class DrawWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.shape = None
        self.color = Qt.GlobalColor.black
        self.thickness = 1
        self.fill_color = Qt.GlobalColor.white
        self.start_point = QPoint()
        self.end_point = QPoint()
        self.points = []

    def set_shape(self, shape):
        self.shape = shape
        self.update()

    def set_color(self, color):
        self.color = color
        self.update()

    def set_fill_color(self, fill_color):
        self.fill_color = fill_color
        self.update()

    def set_thickness(self, thickness):
        self.thickness = thickness
        self.update()

    def set_points(self, points):
        self.points = points
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(self.color, self.thickness)
        painter.setPen(pen)
        painter.setBrush(QBrush(self.fill_color))

        if self.shape == "Garis":
            if len(self.points) == 2:
                painter.drawLine(self.points[0], self.points[1])
        elif self.shape == "Persegi Panjang":
            if len(self.points) == 4:
                painter.drawPolygon(*self.points)
        elif self.shape == "Lingkaran":
            if len(self.points) == 2:
                radius = int((self.points[0].x() - self.points[1].x()) ** 2 + (self.points[0].y() - self.points[1].y()) ** 2) ** 0.5
                painter.drawEllipse(self.points[0], radius, radius)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplikasi Visual Edukasi Matematika")
        self.setGeometry(100, 100, 800, 600)

        self.canvas = DrawWidget()

        self.shape_selector = QComboBox()
        self.shape_selector.addItems(["Garis", "Persegi Panjang", "Lingkaran"])
        self.shape_selector.currentTextChanged.connect(self.shape_changed)

        self.color_button = QPushButton("Pilih Warna Garis")
        self.color_button.clicked.connect(self.choose_color)

        self.fill_color_button = QPushButton("Pilih Warna Isi")
        self.fill_color_button.clicked.connect(self.choose_fill_color)

        self.thickness_selector = QSpinBox()
        self.thickness_selector.setRange(1, 10)
        self.thickness_selector.setValue(1)

        self.start_x_input = QLineEdit()
        self.start_y_input = QLineEdit()
        self.end_x_input = QLineEdit()
        self.end_y_input = QLineEdit()

        self.draw_button = QPushButton("Gambar")
        self.draw_button.clicked.connect(self.draw_shape)

        layout = QVBoxLayout()
        controls_layout = QVBoxLayout()

        controls_layout.addWidget(QLabel("Pilih Bentuk:"))
        controls_layout.addWidget(self.shape_selector)
        controls_layout.addWidget(self.color_button)
        controls_layout.addWidget(self.fill_color_button)
        controls_layout.addWidget(QLabel("Tebal Garis:"))
        controls_layout.addWidget(self.thickness_selector)
        controls_layout.addWidget(QLabel("Koordinat (x1, y1, x2, y2):"))
        controls_layout.addWidget(self.start_x_input)
        controls_layout.addWidget(self.start_y_input)
        controls_layout.addWidget(self.end_x_input)
        controls_layout.addWidget(self.end_y_input)
        controls_layout.addWidget(self.draw_button)

        main_layout = QHBoxLayout()
        main_layout.addLayout(controls_layout)
        main_layout.addWidget(self.canvas)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def shape_changed(self, shape):
        if shape == "Garis":
            self.start_x_input.setPlaceholderText("x1")
            self.start_y_input.setPlaceholderText("y1")
            self.end_x_input.setPlaceholderText("x2")
            self.end_y_input.setPlaceholderText("y2")
        elif shape == "Persegi Panjang":
            self.start_x_input.setPlaceholderText("x1")
            self.start_y_input.setPlaceholderText("y1")
            self.end_x_input.setPlaceholderText("x2 (width)")
            self.end_y_input.setPlaceholderText("y2 (height)")
        elif shape == "Lingkaran":
            self.start_x_input.setPlaceholderText("x (center)")
            self.start_y_input.setPlaceholderText("y (center)")
            self.end_x_input.setPlaceholderText("radius")
            self.end_y_input.clear()
            self.end_y_input.setDisabled(True)

    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.canvas.set_color(color)

    def choose_fill_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.canvas.set_fill_color(color)

    def draw_shape(self):
        shape = self.shape_selector.currentText()
        thickness = self.thickness_selector.value()
        x1 = int(self.start_x_input.text())
        y1 = int(self.start_y_input.text())
        x2 = int(self.end_x_input.text())

        points = []

        if shape == "Garis":
            y2 = int(self.end_y_input.text())
            points = [QPoint(x1, y1), QPoint(x2, y2)]
        elif shape == "Persegi Panjang":
            width = x2
            height = int(self.end_y_input.text())
            points = [
                QPoint(x1, y1),
                QPoint(x1 + width, y1),
                QPoint(x1 + width, y1 + height),
                QPoint(x1, y1 + height)
            ]
        elif shape == "Lingkaran":
            y_center = y1
            radius = x2
            points = [QPoint(x1, y_center), QPoint(x1 + radius, y_center)]

        self.canvas.set_shape(shape)
        self.canvas.set_thickness(thickness)
        self.canvas.set_points(points)
        self.canvas.update()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
