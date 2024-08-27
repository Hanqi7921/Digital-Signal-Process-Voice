import tkinter as tk
from tkinter import PhotoImage, Button, Label, messagebox

class Application(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.master = root
        self.grid(sticky="nsew")
        self.create_widgets()

    def create_widgets(self):
        # Create a top frame for the title label
        self.top_frame = tk.Frame(self)
        self.top_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        # Add the title label
        self.label01 = Label(self.top_frame, text="上海大学 数字信号处理", font=("黑体", 20))
        self.label01.pack()

        # Create a left frame for images
        self.left_frame = tk.Frame(self)
        self.left_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ns")

        # Load and display images
        self.photo1 = PhotoImage(file="123.gif")
        self.original_img = Label(self.left_frame, image=self.photo1)
        self.original_img.grid(row=0, column=0)

        self.photo2 = PhotoImage(file="123.gif")
        self.change_img = Label(self.left_frame, image=self.photo2)
        self.change_img.grid(row=0, column=1, padx=(10, 0))  # Add some padding between images

        # Create a right frame for buttons
        self.right_frame = tk.Frame(self)
        self.right_frame.grid(row=1, column=1, padx=10, pady=10, sticky="ns")

        # Button definitions and layout
        self.btn_openfile = Button(self.right_frame, text="打开文件", width=12, height=2, command=self.Openfile)
        self.btn_openfile.grid(row=0, column=0, pady=5)

        self.btn_quit = Button(self.right_frame, text="录制音频", width=12, height=2, command=root.destroy)
        self.btn_quit.grid(row=1, column=0, pady=5)

        self.btn_adaugmentation = Button(self.right_frame, text="语音增强", width=12, height=2, command=self.Callback_Augmentation)
        self.btn_adaugmentation.grid(row=2, column=0, pady=5)

        self.btn_plusEcho = Button(self.right_frame, text="添加回声", width=12, height=2, command=self.Callback_Echo)
        self.btn_plusEcho.grid(row=3, column=0, pady=5)

        self.btn_delEcho = Button(self.right_frame, text="去除回声", width=12, height=2, command=self.Callback_DelEcho)
        self.btn_delEcho.grid(row=4, column=0, pady=5)

        self.btn_endRecog = Button(self.right_frame, text="端点检测", width=12, height=2, command=self.Callback_Recognition)
        self.btn_endRecog.grid(row=5, column=0, pady=5)
        
        self.btn_play = Button(self.right_frame, text="播放音频", width=12, height=2, command=self.Callback_Play)
        self.btn_play.grid(row=6, column=0, pady=5)

    def Openfile(self):
        messagebox.showinfo("提示", "打开文件")
        print("打开文件")

    def Callback_Augmentation(self):
        messagebox.showinfo("提示", "语音增强")
        print("语音增强")

    def Callback_Echo(self):
        messagebox.showinfo("提示", "添加回声")
        print("添加回声")

    def Callback_DelEcho(self):
        messagebox.showinfo("提示", "去除回声")
        print("去除回声")

    def Callback_Recognition(self):
        messagebox.showinfo("提示", "端点检测")
        print("端点检测")

    def Callback_Play(self):
        messagebox.showinfo("提示", "播放音频")
        print("播放音频")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("数字信号处理")
    root.geometry("1000x600+100+100")
    app = Application(root)
    root.mainloop()
