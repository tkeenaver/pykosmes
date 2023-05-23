import tkinter as tk
from tkinter import ttk

# 사용자 정의 함수부
def buildGUI():
    btn1 = ttk.Button(win, text='버튼1')
    btn2 = ttk.Button(win, text='버튼2')
    btn3 = ttk.Button(win, text='버튼3')
    btn4 = ttk.Button(win, text='버튼4')
    btn5 = ttk.Button(win, text='버튼5')

    btn1.pack()
    btn2.pack(ipadx=10, ipady=10)
    btn3.pack(padx=10, pady=10)
    btn4.pack(fill=tk.X)
    btn5.pack(fill=tk.X, padx=10, pady=10, ipadx=10, ipady=10)

# 주 프로그램부
win = tk.Tk()               # 기본 윈도우 객체 반환
win.title('pack() 배치의 예')
win.geometry('300x200')
buildGUI()                  # 화면 구성
win.mainloop()              # 윈도우에서 다양한 이벤트 처리 시작을 지시
