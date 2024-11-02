from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QApplication, QPushButton, QLabel, QVBoxLayout, QWidget

class MyWidget(QWidget):
    # 시그널 정의
    button_clicked = Signal()

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.button = QPushButton("Click Me")
        self.label = QLabel("")

        layout.addWidget(self.button)
        layout.addWidget(self.label)
        self.setLayout(layout)

        # 시그널과 슬롯 연결
        self.button.clicked.connect(self.button_clicked)
        self.button_clicked.connect(self.on_button_click)

    # 슬롯 정의
    @Slot()
    def on_button_click(self):
        self.label.setText("Button Clicked!")

app = QApplication([])
widget = MyWidget()
widget.show()
app.exec()
