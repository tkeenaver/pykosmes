import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QLabel, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 Widgets Example")
        self.setGeometry(100, 100, 400, 300)

        # 레이아웃 설정
        layout = QVBoxLayout()

        # QLabel 생성 및 추가
        label = QLabel("This is a QLabel")
        layout.addWidget(label)

        # QPushButton 생성 및 추가
        button = QPushButton("Click Me")
        layout.addWidget(button)

        # QLineEdit 생성 및 추가
        line_edit = QLineEdit("Type here")
        layout.addWidget(line_edit)

        # QTextEdit 생성 및 추가
        text_edit = QTextEdit("Edit this text")
        layout.addWidget(text_edit)

        # 중앙 위젯 설정
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 버튼 클릭 이벤트 핸들러 설정
        button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        print("Button was clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
