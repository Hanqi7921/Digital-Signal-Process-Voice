import tkinter as tk
from tkinter import PhotoImage, Button, Label, messagebox
from tkinter import filedialog
from function.audio_record import Audio
from function.Speech_Enhancement import Spectral_subtraction
from function.Speech_Endpoint import Speech_Endpoint
from function.Speech_Echo import add_echo
from function.Speech_Echo import remove_echo

new_image_path_1 = "Img_result\PNG\original.png"
new_image_path_2 = "Img_result\PNG\change.png"
class Application(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.master = root
        self.grid(sticky="nsew")
        self.create_widgets()
        self.choice_path = None

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
        self.photo1 = PhotoImage(file="Img_result/GIF/original.gif")
        self.photo2 = PhotoImage(file="Img_result/GIF/change.gif")
        self.photo3 = PhotoImage(file="Img_result/GIF/original.gif")
        self.photo4 = PhotoImage(file="Img_result/GIF/original.gif")
        
        # Resize images if needed
        max_width = 450
        max_height = 250
        self.photo1 = self.photo1.subsample(max(self.photo1.width() // max_width, 1),
                                            max(self.photo1.height() // max_height, 1))
        self.photo2 = self.photo2.subsample(max(self.photo2.width() // max_width, 1),
                                            max(self.photo2.height() // max_height, 1))
        self.photo3 = self.photo3.subsample(max(self.photo3.width() // max_width, 1),
                                            max(self.photo3.height() // max_height, 1))
        self.photo4 = self.photo4.subsample(max(self.photo4.width() // max_width, 1),
                                            max(self.photo4.height() // max_height, 1))
        
        # Create image labels
        self.img1 = Label(self.left_frame, image=self.photo1)
        self.img1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        self.img2 = Label(self.left_frame, image=self.photo2)
        self.img2.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        
        self.img3 = Label(self.left_frame, image=self.photo3)
        self.img3.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        
        self.img4 = Label(self.left_frame, image=self.photo4)
        self.img4.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

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

        self.btn_endRecog = Button(self.right_frame, text="端点检测", width=12, height=2, command=self.Callback_Detection)
        self.btn_endRecog.grid(row=5, column=0, pady=5)
        
        self.btn_play = Button(self.right_frame, text="播放音频", width=12, height=2, command=self.Callback_Play)
        self.btn_play.grid(row=6, column=0, pady=5)

    def Callback_Openfile(self):
        #finish
        file_path= filedialog.askopenfilename()
        # global audio_object
        self.choice_path=file_path
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
        messagebox.showinfo("提示", "导入文件成功！")
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
        audio_object.save(direction = "library\SHU.wav")
        self.choice_path="library\SHU.wav"
        messagebox.showinfo("提示", "录制完成！")
        print("已完成保存音频")
        
    def Callback_Augmentation(self):
        Spectral_subtraction(audio.object)
        print("语音增强")

    def Callback_Echo(self):
        add_echo(self.choice_path, 'library\output_with_echo_mono.wav')  # 添加回声到单通道音频并保存
        self.update_image(self.img2, new_image_path_2)  # 更新第二张图片
        print("添加回声")

    def Callback_DelEcho(self):
        #那我直接播放原声好了？？
        #但是为了显示效果，我还是添加了消除回声的算法
        remove_echo(self.choice_path)
        self.update_image(self.img2, new_image_path_2)  # 更新第二张图片
        print("去除回声")

    def Callback_Detection(self):
        Speech_Endpoint(audio.object)
        self.update_image(self.img2, new_image_path_2)  # 更新第二张图片
        print("端点检测")

    def Callback_Play(self):
        #finish
        audio.play(audio.object)
        audio.plot(audio.object)
        print("播放音频")
        self.update_image(self.img1, new_image_path_1)  # 更新第一张图片

    
    def update_image(self, label, image_path):
        # 加载新图片并调整大小
        new_photo = PhotoImage(file=image_path)
        max_width = 450
        max_height = 250
        new_photo = new_photo.subsample(max(new_photo.width() // max_width, 1),
                                        max(new_photo.height() // max_height, 1))
        # 更新Label的图像
        label.config(image=new_photo)
        # 保存对新图片的引用，防止垃圾回收
        label.image = new_photo


if __name__ == "__main__":
    root = tk.Tk()
    root.title("数字信号处理")
    root.geometry("1200x700+100+100")
    app = Application(root)
    audio=Audio()
    root.mainloop()
