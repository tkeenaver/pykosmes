import tkinter as tk
from tkinter import ttk

# 사용자 정의 함수부
def buildGUI():
    global text_label
    text_label = ttk.Label(win, text='안녕하세요')

    global name                 # 이벤트 핸들러에서 접근 위해
    name = tk.StringVar()       # 엔트리 위젯에서 문자열 저장 위해
    input_entry = ttk.Entry(win, textvariable=name)
    
    input_btn = ttk.Button(win, text='입력',
                                command=input_btn_handler)
    quit_btn = ttk.Button(win, text='종료',
                                command=win.destroy)
    
    text_label.pack()
    input_entry.pack()
    input_btn.pack()
    quit_btn.pack()

def input_btn_handler():        # 버튼 클릭에 대한 이벤트 핸들러 함수
    text_label.configure(text='반가워요, ' + name.get())
    name.set('')                # 작은따옴표 두 개로 빈문자열을 인수로 지정

# 주 프로그램부
win = tk.Tk()                   # 기본 윈도우 객체 반환
win.title('버튼 위젯 예')
buildGUI()                      # 화면 구성
win.mainloop()                  # 윈도우에서 다양한 이벤트 처리 시작을 지시
