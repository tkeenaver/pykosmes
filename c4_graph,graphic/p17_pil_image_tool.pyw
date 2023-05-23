from PIL import Image, ImageTk, ImageFilter  
import tkinter as tk
from tkinter import filedialog as fd

im = None
tk_img = None

def open( ):		# “열기” 메뉴 
    global im, tk_img
    fname = fd.askopenfilename( )
    im = Image.open(fname)
    tk_img = ImageTk.PhotoImage(im)
    canvas.create_image(250, 250, image=tk_img)
    window.update( )

def quit( ):		# “종료” 메뉴 
    window.quit( )

def image_rotate( ):
    global im, tk_img
    out = im.rotate(45) 
    tk_img = ImageTk.PhotoImage(out)
    canvas.create_image(250, 250, image=tk_img)
    window.update( )

def image_blur( ):
    global im, tk_img
    out = im.filter(ImageFilter.BLUR)
    tk_img = ImageTk.PhotoImage(out)
    canvas.create_image(250, 250, image=tk_img)
    window.update( )

window = tk.Tk( )	# 윈도우를 생성합니다. 
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack( )

menubar = tk.Menu(window) 	# 메뉴를 생성합니다.
filemenu = tk.Menu(menubar)
ipmenu = tk.Menu(menubar)

filemenu.add_command(label="열기", command=open)	#파일 메뉴
filemenu.add_command(label="종료", command=quit)

ipmenu.add_command(label="영상회전", command=image_rotate)		#영상처리 메뉴
ipmenu.add_command(label="영상흐리게", command=image_blur)

menubar.add_cascade(label="파일", menu=filemenu)
menubar.add_cascade(label="영상처리", menu=ipmenu)

window.config(menu=menubar)
window.mainloop( )
