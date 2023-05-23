import tkinter as tk            # tk라는 별명으로 tkinter 모듈 임포트
from tkinter import ttk         # tkinter에서 ttk 모듈 임포트

# 사용자 정의 함수부
def buildGUI():
    global text_label           # 이벤트 핸들러에서 접근 위해
    text_label = ttk.Label(win, text='안녕하세요')

    input_btn = ttk.Button(win, text='입력',
                                  command=input_btn_handler)
    quit_btn = ttk.Button(win, text='종료',
                                  command=win.destroy)

    text_label.pack()
    input_btn.pack()
    quit_btn.pack()

def input_btn_handler():        # 버튼 클릭에 대한 이벤트 핸들러 함수
    text_label.configure(text='반가워요')

# 주 프로그램부
win = tk.Tk()                   # 기본 윈도우 객체 반환
win.title('버튼 위젯 예')
buildGUI()                      # 화면 구성
win.mainloop()                  # 윈도우에서 다양한 이벤트 처리 시작을 지시
