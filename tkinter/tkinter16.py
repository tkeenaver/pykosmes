import tkinter as tk
from tkinter import ttk

# 사용자 정의 함수부
def buildGUI():
    btn1 = ttk.Button(win, text='버튼1')
    btn2 = ttk.Button(win, text='버튼2')
    btn3 = ttk.Button(win, text='버튼3')
    btn4 = ttk.Button(win, text='버튼4')
    btn5 = ttk.Button(win, text='버튼5')

    btn1.pack()             # btn1.pack(side=tk.TOP)과 동일
    btn2.pack()
    btn3.pack()
    btn4.pack()
    btn5.pack()

# 주 프로그램부
win = tk.Tk()               # 기본 윈도우 객체 반환
win.title('pack() 배치의 예')
win.geometry('300x200')
buildGUI()                  # 화면 구성
win.mainloop()              # 윈도우에서 다양한 이벤트 처리 시작을 지시
