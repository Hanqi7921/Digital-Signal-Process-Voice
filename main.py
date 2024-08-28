import tkinter as tk
from tkinter import PhotoImage, Button, Label, messagebox
from audio_record import Audio
from tkinter import filedialog
from Speech_Enhancement import Spectral_subtraction

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
        self.photo1 = PhotoImage(file="Img_result\GIF\original.gif")
        # 设置图片的最大宽度和高度
        max_width = 420  # 例如，最大宽度为200像素
        max_height = 350  # 例如，最大高度为200像素
        self.photo1 = self.photo1.subsample(max(self.photo1.width() // max_width, 1),
                                            max(self.photo1.height() // max_height, 1))
        self.original_img = Label(self.left_frame, image=self.photo1)
        self.original_img.grid(row=0, column=0)

        self.photo2 = PhotoImage(file="Img_result\GIF\original.gif")
        # 同样设置第二张图片的大小
        self.photo2 = self.photo2.subsample(max(self.photo2.width() // max_width, 1),
                                            max(self.photo2.height() // max_height, 1))
        self.change_img = Label(self.left_frame, image=self.photo2)
        self.change_img.grid(row=0, column=1, padx=(10, 0))  # Add some padding between

        # Create a right frame for buttons
        self.right_frame = tk.Frame(self)
        self.right_frame.grid(row=1, column=1, padx=10, pady=10, sticky="ns")

        # Button definitions and layout
        self.btn_openfile = Button(self.right_frame, text="打开文件", width=12, height=2, command=self.Callback_Openfile)
        self.btn_openfile.grid(row=0, column=0, pady=5)

        self.btn_record = Button(self.right_frame, text="录制音频", width=12, height=2, command=self.Callback_Record)
        self.btn_record.grid(row=1, column=0, pady=5)

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

    def Callback_Openfile(self):
        #finish
        file_path= filedialog.askopenfilename()
        # global audio_object
        audio_object=audio.read(file_path) # 返回的是Audio object
        audio.object = audio_object
        audio.samples=audio_object.samples # 获取音频中的所有样本
        audio.duration=audio_object.getDuration # 获取音频的持续时间 （秒）
        audio.samples_counts=len(audio_object) # 获取音频的样本计数。
        audio.sr=audio_object.sr # 获取音频的采样率。
        print("audio.samples:",audio.samples)
        print("audio.duration:",audio.duration)
        print("audio.samples_counts:",audio.samples_counts)
        print("audio.sr:",audio.sr)
        print("已完成打开文件")

    def Callback_Record(self):
        #finish
        # global audio_object
        audio_object=audio.record(44100,5)
        audio.object = audio_object
        audio.samples=audio_object.samples # 获取音频中的所有样本
        audio.duration=audio_object.getDuration
        audio.samples_counts=len(audio_object)
        audio.sr=audio_object.sr       
        print("已完成录制音频")
        audio_object.save(direction = "SHU.wav")
        print("已完成保存音频")
        
    def Callback_Augmentation(self):
        Spectral_subtraction(audio.object)
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
        #finish
        audio.play(audio.object)
        audio.plot(audio.object)
        print("播放音频")
        new_image_path = "Img_result\PNG\original.png"
        self.update_image(self.original_img, new_image_path)  # 更新第一张图片
        self.update_image(self.change_img, new_image_path)  # 更新第二张图片
    
    def update_image(self, label, image_path):
        # 加载新图片并调整大小
        new_photo = PhotoImage(file=image_path)
        max_width = 420
        max_height = 350
        new_photo = new_photo.subsample(max(new_photo.width() // max_width, 1),
                                        max(new_photo.height() // max_height, 1))
        # 更新Label的图像
        label.config(image=new_photo)
        # 保存对新图片的引用，防止垃圾回收
        label.image = new_photo


if __name__ == "__main__":
    root = tk.Tk()
    root.title("数字信号处理")
    root.geometry("1200x500+100+100")
    app = Application(root)
    audio=Audio()
    root.mainloop()
