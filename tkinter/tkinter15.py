import tkinter as tk
from tkinter import ttk

GENDERS = [ '남성', '여성', '기타' ]
COLORS = [ 'red', 'yellow', 'purple' ]

# 사용자 정의 함수부
def buildGUI():
    text_label = ttk.Label(win, text='당신의 성별은? ')
    text_label.pack()

    global gender           # 이벤트 핸들러에서 접근 위해
    gender = tk.IntVar()    # 체크 상태 저장 위해
    for i in range(3):
        radio_btn = ttk.Radiobutton(win,
                      text=GENDERS[i],
                      value=i,
                      variable=gender,
                      command=radio_btn_hadler
        )
        radio_btn.pack()

    gender.set(-1)          # 라디오 버튼 선택 지우기

def radio_btn_hadler():
    choice = gender.get()
    win.configure(background=COLORS[choice])

# 주 프로그램부
win = tk.Tk()               # 기본 윈도우 객체 반환
win.title('버튼 위젯 예')
buildGUI()                  # 화면 구성
win.mainloop()              # 윈도우에서 다양한 이벤트 처리 시작을 지시
