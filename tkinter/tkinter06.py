import tkinter as tk        # tk라는 별명으로 tkinter 모듈 임포트
from tkinter import ttk     # tkinter에서 ttk 모듈 임포트

# 사용자 정의 함수부
def buildGUI():
    text_label1 = ttk.Label(win, text='안녕하세요')
    text_label1.pack()

# 주 프로그램부
win = tk.Tk()               # 기본 윈도우 객체 반환
win.title('라벨 위젯 예1')
buildGUI()                  # 화면 구성
win.mainloop()              # 윈도우에서 다양한 이벤트 처리 시작을 지시
