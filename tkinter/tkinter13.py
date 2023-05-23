import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
# 사용자 정의 함수부
def buildGUI():
    global text_area
    text_area = scrolledtext.ScrolledText(win,
                            width=30, height=5, wrap=tk.WORD)
    
    input_btn = ttk.Button(win, text='출력',
                                  command=input_btn_handler)
    
    text_area.pack()
    input_btn.pack()

def input_btn_handler():    # 이벤트 핸들러 함수
    print(text_area.get(0.0, tk.END))
    text_area.delete(0.0, tk.END)

# 주 프로그램부
win = tk.Tk()               # 기본 윈도우 객체 반환
win.title('버튼 위젯 예')
buildGUI()                  # 화면 구성
win.mainloop()              # 윈도우에서 다양한 이벤트 처리 시작을 지시
