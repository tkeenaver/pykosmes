from PySide6.QtWidgets import (QApplication,
    QMainWindow, QLabel)

app = QApplication([])
window = QMainWindow()
window.setWindowTitle("Hello PySide6")
label = QLabel("Hello, PySide6!", parent=window)
window.setCentralWidget(label)
window.resize(400, 300)
window.show()
app.exec()
