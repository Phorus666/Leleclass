import ctypes
import tkinter as tk
from tkinter import ttk, messagebox  # 导入messagebox模块
import webbrowser

current_video_number = 0

def preview_image():
    global current_video_number
    video_number = entry.get()
    if video_number:
        image_url = f"http://v.leleketang.com/dat/hs/ph/k/thumb/{video_number}.jpg"
        webbrowser.open(image_url)
        current_video_number = int(video_number)
    else:
        messagebox.showwarning("警告", "请输入视频编号")

def play_video():
    global current_video_number
    video_number = entry.get()
    if video_number:
        video_url = f"http://v.leleketang.com/dat/hs/ph/k/video/{video_number}.mp4"
        webbrowser.open(video_url)
        current_video_number = int(video_number)
    else:
        messagebox.showwarning("警告", "请输入视频编号")

def play_next_video():
    global current_video_number
    next_video_number = current_video_number + 1
    video_url = f"http://v.leleketang.com/dat/hs/ph/k/video/{next_video_number}.mp4"
    webbrowser.open(video_url)
    current_video_number = next_video_number

root = tk.Tk()
root.title("LePlayer by YuZX")
root.geometry("380x250")  # 设置窗口大小
root.resizable(False, False)  # 禁止调整大小
#调用api设置成由应用程序缩放
ctypes.windll.shcore.SetProcessDpiAwareness(1)
#调用api获得当前的缩放因子
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
#设置缩放因子
root.tk.call('tk', 'scaling', ScaleFactor/75)

# Make the window stay on top
root.attributes("-topmost", True)

style = ttk.Style()
style.theme_use("clam")

label = ttk.Label(root, text="请输入视频编号:")
label.pack(pady=10)

entry = ttk.Entry(root)
entry.pack()

preview_button = ttk.Button(root, text="预览图片", command=preview_image)
preview_button.pack(pady=5)

play_button = ttk.Button(root, text="播放视频", command=play_video)
play_button.pack(pady=5)

next_button = ttk.Button(root, text="播放下一个视频", command=play_next_video)
next_button.pack(pady=5)

root.mainloop()
