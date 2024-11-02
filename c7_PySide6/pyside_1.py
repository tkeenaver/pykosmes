import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

# 주 윈도우 클래스 정의
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 윈도우 설정
        self.setWindowTitle("PySide6 Basic App")
        self.setGeometry(100, 100, 300, 200)

        # 버튼 생성 및 설정
        self.button = QPushButton("Click Me", self)
        self.button.setGeometry(100, 80, 100, 40)
        self.button.clicked.connect(self.show_message)

    def show_message(self):
        QMessageBox.information(self, "Message", "Hello, PySide6!")

# QApplication 객체 생성
app = QApplication(sys.argv)

# 주 윈도우 객체 생성 및 표시
main_window = MainWindow()
main_window.show()

# 이벤트 루프 실행
sys.exit(app.exec())
