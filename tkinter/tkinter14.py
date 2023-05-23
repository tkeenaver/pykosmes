import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# 사용자 정의 함수부
def buildGUI():
    global check            # 이벤트 핸들러에서 접근 위해
    check = tk.IntVar()     # 체크 상태 저장 위해
    check_btn = ttk.Checkbutton(win, text='옵션을 선택하세요',
                      variable=check,
                      command=open_dialog_box)
    
    check_btn.pack()

def open_dialog_box():
    if check.get() == 1:
        messagebox.showinfo('확인', '옵션 선택')
    else:
        messagebox.showinfo('확인', '옵션 해제')

# 주 프로그램부
win = tk.Tk()               # 기본 윈도우 객체 반환
win.title('버튼 위젯 예')
buildGUI()                  # 화면 구성
win.mainloop()              # 윈도우에서 다양한 이벤트 처리 시작을 지시
