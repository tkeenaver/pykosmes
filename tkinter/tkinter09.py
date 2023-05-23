import tkinter as tk            # tk라는 별명으로 tkinter 모듈 임포트
from tkinter import ttk         # tkinter에서 ttk 모듈 임포트

# 사용자 정의 함수부
def buildGUI():
    s = ttk.Style()             # 스타일 객체 생성
    s.configure('WR.TLabel',    # 새 스타일 이름
        foreground='white',     # 전경색을 흰색으로 설정
        background='red',       # 배경색을 빨강색으로 설정
        font=('맑은 고딕', 20)  # 글꼴을 설정
    )                           # WR.TLabel 스타일 정의 끝

    text_label1 = ttk.Label(win, text='안녕하세요', style='WR.TLabel')

    text_label2 = ttk.Label(win)
    text_label2.configure(text='반가워요', style='WR.TLabel')

    text_label1.pack()
    text_label2.pack()

# 주 프로그램부
win = tk.Tk()                   # 기본 윈도우 객체 반환
win.title('라벨 위젯 예1')
buildGUI()                      # 화면 구성
win.mainloop()                  # 윈도우에서 다양한 이벤트 처리 시작을 지시
