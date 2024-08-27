import tkinter as tk
from tkinter import *
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.master = root
        self.grid(row=0,column=0)
        self.left_intWind()
        self.right_intWind()


    def left_intWind(self):
        global photo1
        photo1=PhotoImage(file="123.gif")
        self.original_img=Label(self,image=photo1)
        self.original_img.grid(row=0,column=0)

        global photo2
        photo2=PhotoImage(file="123.gif")
        self.change_img=Label(self,image=photo2)
        self.change_img.grid(row=0,column=1)

    def right_intWind(self):
        self.btn_openfile=Button(root, text="打开文件",width=12,height=2,command=self.Openfile)
        self.btn_openfile.grid(row=0,column=0)
        
        self.btn_quit=Button(root, text="录制音频",width=12,height=2,command=root.destroy)
        self.btn_quit.grid(row=70,column=200)

        self.btn_adaugmentation=Button(root, text="语音增强",width=12,height=2,command=self.Callback_Augmentation)
        self.btn_adaugmentation.grid(row=70,column=100)

        self.btn_plusEcho=Button(root, text="添加回声",width=12,height=2,command=self.Callback_Echo)
        self.btn_plusEcho.grid(row=90,column=100)

        self.btn_delEcho=Button(root, text="去除回声",width=12,height=2,command=self.Callback_DelEcho)
        self.btn_delEcho.grid(row=110,column=100)

        self.btn_endRecog=Button(root, text="端点检测",width=12,height=2,command=self.Callback_Recognition)
        self.btn_endRecog.grid(row=130,column=100)

        self.label01=Label(self,text="上海大学 数字信号处理",font=("黑体",20))
        self.label01.grid(row=50,column=60)

        self.label02=Label(self,text="上海大学 数字信号处理")
        self.label02.grid(row=80,column=30)

        

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

    

if __name__ == "__main__":
    root = tk.Tk()
    root.title("数字信号处理")
    root.geometry("1000x600+100+100")
    app=Application(root)
    root.mainloop()







