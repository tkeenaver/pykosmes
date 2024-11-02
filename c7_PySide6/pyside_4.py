from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.label = QLabel("Press a key")
        layout.addWidget(self.label)
        self.setLayout(layout)

    def keyPressEvent(self, event):
        self.label.setText(f"Key Pressed: {event.key()}")

app = QApplication([])
widget = MyWidget()
widget.show()
app.exec()
