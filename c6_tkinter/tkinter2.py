import tkinter as tk

# 키보드 이벤트 핸들러 함수
def on_key_press(event):
    print(f"Key pressed: {event.keysym}")

# 마우스 이벤트 핸들러 함수
def on_mouse_click(event):
    print(f"Mouse clicked at ({event.x}, {event.y})")

# 루트 윈도우 생성
root = tk.Tk()
root.title("Event Handling Example")
root.geometry("300x200")

# 키보드 이벤트 바인딩
root.bind("<KeyPress>", on_key_press)

# 마우스 이벤트 바인딩
root.bind("<Button-1>", on_mouse_click)

# 이벤트 루프 실행
root.mainloop()
