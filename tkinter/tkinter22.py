import tkinter as tk
from tkinter import ttk

# 사용자 정의 함수부
def buildGUI():
    btn1 = ttk.Button(win, text='버튼1')
    btn2 = ttk.Button(win, text='매우 긴~~~ 너비와 높이를 갖는\n버\n튼\n2')
    btn3 = ttk.Button(win, text='버튼3')
    btn4 = ttk.Button(win, text='버튼4')
    btn5 = ttk.Button(win, text='버튼5')

    btn1.grid(row=0, column=0, sticky='se')
    btn2.grid(row=0, column=1, columnspan=2)
    btn3.grid(row=1, column=1, sticky='w')
    btn4.grid(row=1, column=2)
    btn5.grid(row=2, column=0)

# 주 프로그램부
win = tk.Tk()               # 기본 윈도우 객체 반환
win.title('grid 배치의 예')
win.geometry('300x200')
buildGUI()                  # 화면 구성
win.mainloop()              # 윈도우에서 다양한 이벤트 처리 시작을 지시
