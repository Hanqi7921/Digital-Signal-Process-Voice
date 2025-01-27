import tkinter as tk
import time  
import threading
from tkinter import PhotoImage, Button, Label, messagebox
from tkinter import filedialog,ttk
from function.audio_record import Audio
from function.Speech_Enhancement import Spectral_subtraction
from function.Speech_Endpoint import Speech_Endpoint
from function.Speech_Echo import add_echo
from function.Speech_Echo import remove_echo


new_image_path_1 = "Image/PNG/original.png"
new_image_path_2 = "Image/PNG/change.png"
new_image_path_3 = "Image/PNG/original_fft.png"
new_image_path_4 = "Image/PNG/change_fft.png"

max_width_up = 575
max_height_up = 350
max_width_down = 650
max_height_down = 380

class RecordingDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("录制音频")
        self.geometry("300x200")
        self.stop_thread = False  # 停止标志
        self.recording_thread = None
        # Center the dialog on the screen
        self.center_on_screen()
        self.transient(parent)
        self.grab_set()
        
        self.duration_var = tk.IntVar(value=5)  # Default duration is 5 seconds

        # Create and layout widgets
        tk.Label(self, text="录音时长(秒)").pack(pady=10)
        self.duration_entry = tk.Entry(self, textvariable=self.duration_var)
        self.duration_entry.pack(pady=5)

        self.start_button = tk.Button(self, text="开始录音", command=self.start_recording)
        self.start_button.pack(pady=10)

        # Add timer and progress bar
        self.timer_label = tk.Label(self, text="00:00", font=("Helvetica", 12))
        self.timer_label.pack(pady=5)

        self.progress_bar = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate")
        self.progress_bar.pack(pady=5)
     
        self.recording = False
        
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def start_recording(self):
      
        duration = self.duration_var.get()
        if duration <= 0:
            messagebox.showerror("错误", "录音时长必须大于0秒。")
            return
        
        self.recording = True
        self.start_button.config(state="disabled")
        self.progress_bar["maximum"] = duration

        self.start_time = time.time()
        self.update_timer()
        
        # Start recording in a separate thread
        self.recording_thread = threading.Thread(target=self.record_audio, args=(duration,))
        self.recording_thread.start()
            
    def record_audio(self, duration):
        audio_object = audio.record(44100, duration)
        audio.object = audio_object
        audio.samples = audio_object.samples
        audio.duration = audio_object.getDuration()
        audio.samples_counts = len(audio_object)
        audio.sr = audio_object.sr
        
        audio_object.save(direction="Wav/tmp.wav")
        self.master.choice_path = "Wav/tmp.wav"
        
        self.recording = False
        print(111)
        self.master.after(0, lambda: messagebox.showinfo("提示", "录制完成,请查看Wav/tmp.wav!"))
        self.clear_progress()
        return#录制完成
            
            
    def update_timer(self):
        if self.recording:
            elapsed_time = int(time.time() - self.start_time)
            minutes, seconds = divmod(elapsed_time, 60)
            self.timer_label.config(text=f"{minutes:02}:{seconds:02}")

            # Update progress bar
            self.progress_bar["value"] = elapsed_time

            # Check if recording should stop
            duration = self.duration_var.get()
            if elapsed_time >= duration:
                self.recording = False
                self.start_button.config(state="normal")
                if self.recording_thread is not None:
                    self.recording_thread.join()  # 等待线程结束
            else:
            # Update timer every second
                self.after(1000, self.update_timer)
            
    def clear_progress(self):
        self.timer_label.config(text="00:00")
        self.progress_bar["value"] = 0
                   
    def center_on_screen(self):
    # Get screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Get dialog dimensions
        dialog_width = 300
        dialog_height = 200

        # Calculate the position of the dialog
        x = (screen_width - dialog_width) // 2
        y = (screen_height - dialog_height) // 2

        # Set the dialog geometry
        self.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")
        
    def on_closing(self):
        self.recording = False
        self.start_button.config(state="normal")
        if self.recording_thread is not None:
            self.recording_thread.join()  # 等待线程结束
        self.master.grab_set(None)
        self.destroy()
        self.master.update_image(self.master.img1, new_image_path_1)
        self.master.update_image(self.master.img3, new_image_path_3)
        
class Application(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.master = root
        self.grid(sticky="nsew")
        self.create_widgets()
        self.choice_path = None
        # #动态调整窗口大小，暂时无法实现
        # for i in range(8):  # 假设有8行
        #     self.master.grid_rowconfigure(i, weight=1)
        # for i in range(2):  # 假设有2列
        #     self.master.grid_columnconfigure(i, weight=1)

    def create_widgets(self):
        
        # Create a top frame for the title label
        self.top_frame = tk.Frame(self)
        self.top_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        # Add the title label
        self.label01 = Label(self.top_frame, text="上海大学 数字信号处理", font=("楷体", 20))
        self.label01.pack()

        # Create a left frame for images
        self.left_frame = tk.Frame(self)
        self.left_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ns")

        # Load and display images
        self.photo1 = PhotoImage(file="Image\GIF\init.gif")
        self.photo2 = PhotoImage(file="Image\GIF\init.gif")
        self.photo3 = PhotoImage(file="Image\GIF\init_fft.gif")
        self.photo4 = PhotoImage(file="Image\GIF\init_fft.gif")
        
        # Resize images if needed
        self.photo1 = self.photo1.subsample(max(self.photo1.width() // max_width_up, 1),
                                            max(self.photo1.height() // max_height_up, 1))
        self.photo2 = self.photo2.subsample(max(self.photo2.width() // max_width_up, 1),
                                            max(self.photo2.height() // max_height_up, 1))
        self.photo3 = self.photo3.subsample(max(self.photo3.width() // max_width_down, 1),
                                            max(self.photo3.height() // max_height_down, 1))
        self.photo4 = self.photo4.subsample(max(self.photo4.width() // max_width_down, 1),
                                            max(self.photo4.height() // max_height_down, 1))
        
        # Create image labels
        self.img1_title = Label(self.left_frame,text="初始音频时域图像",font=("楷体", 16))
        self.img1_title.grid(row=0, column=0, sticky="nsew")
        self.img1 = Label(self.left_frame,image=self.photo1)
        self.img1.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        
        self.img2_title = Label(self.left_frame,text="变化音频时域图像",font=("楷体", 16))
        self.img2_title.grid(row=0, column=1, sticky="nsew")
        self.img2 = Label(self.left_frame, image=self.photo2)
        self.img2.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        
        self.img3_title = Label(self.left_frame,text="初始音频频谱",font=("楷体", 16))
        self.img3_title.grid(row=2, column=0, sticky="nsew")
        self.img3 = Label(self.left_frame, image=self.photo3)
        self.img3.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        
        self.img4_title = Label(self.left_frame,text="变化音频频谱",font=("楷体", 16))
        self.img4_title.grid(row=2, column=1, sticky="nsew")
        self.img4 = Label(self.left_frame, image=self.photo4)
        self.img4.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

        # Create a right frame for buttons
        self.right_frame = tk.Frame(self)
        self.right_frame.grid(row=1, column=1, padx=10, pady=10, sticky="ns")
        gap=20
        gapx=50
        # Button definitions and layout
        self.btn_openfile = Button(self.right_frame, text="打开文件", width=12, height=2, command=self.Callback_Openfile)
        self.btn_openfile.grid(row=0, column=0, pady=gap,padx=gapx)

        self.btn_record = Button(self.right_frame, text="录制音频", width=12, height=2, command=self.Callback_Record)
        self.btn_record.grid(row=1, column=0, pady=gap,padx=gapx)

        self.btn_adaugmentation = Button(self.right_frame, text="语音增强", width=12, height=2, command=self.Callback_Augmentation)
        self.btn_adaugmentation.grid(row=2, column=0, pady=gap,padx=gapx)

        self.btn_plusEcho = Button(self.right_frame, text="添加回声", width=12, height=2, command=self.Callback_Echo)
        self.btn_plusEcho.grid(row=3, column=0, pady=gap,padx=gapx)

        self.btn_delEcho = Button(self.right_frame, text="去除回声", width=12, height=2, command=self.Callback_DelEcho)
        self.btn_delEcho.grid(row=4, column=0, pady=gap,padx=gapx)

        self.btn_endRecog = Button(self.right_frame, text="端点检测", width=12, height=2, command=self.Callback_Detection)
        self.btn_endRecog.grid(row=5, column=0, pady=gap,padx=gapx)
        
        self.btn_play = Button(self.right_frame, text="播放音频", width=12, height=2, command=self.Callback_Play)
        self.btn_play.grid(row=6, column=0, pady=gap,padx=gapx)
        
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
        self.play_prep()

    def Callback_Record(self):
        #finish
        record_dialog = RecordingDialog(self)
        self.wait_window(record_dialog)  # Wait until the dialog is closed
        
    def Callback_Augmentation(self):
        allowin=self.check_audio()
        if allowin == True:
            Spectral_subtraction(audio.object)
            self.update_image(self.img2, new_image_path_2)  # 更新第一张图片
            self.update_image(self.img4, new_image_path_4)  # 更新第一张图片
            print("语音增强")

    def Callback_Echo(self):
        allowin=self.check_audio()
        if allowin == True:
            add_echo(self.choice_path)  # 添加回声到单通道音频并保存
            self.update_image(self.img2, new_image_path_2)  # 更新第二张图片
            self.update_image(self.img4, new_image_path_4)  # 更新第一张图片
            print("添加回声")

    def Callback_DelEcho(self):
        allowin=self.check_audio()
        if allowin == True:
        #那我直接播放原声好了？？
        #但是为了显示效果，我还是添加了消除回声的算法
            remove_echo(self.choice_path)
            self.update_image(self.img2, new_image_path_2)  # 更新第二张图片
            self.update_image(self.img4, new_image_path_4)  # 更新第一张图片
            print("去除回声")

    def Callback_Detection(self):
        allowin=self.check_audio()
        if allowin == True:
            Speech_Endpoint(audio.object)
            self.update_image(self.img2, new_image_path_2)  # 更新第二张图片
            new_image_path_4=new_image_path_3
            self.update_image(self.img4, new_image_path_4)  # 更新第一张图片
            print("端点检测")

    def Callback_Play(self):
        allowin=self.check_audio()
        if allowin == True:
            self.play_prep()
            

    def play_prep(self):
        audio.play()
        audio.plot()
        print("播放音频")
        self.update_image(self.img1, new_image_path_1)  # 更新第一张图片
        self.update_image(self.img3, new_image_path_3)  # 更新第一张图片
        return True
        
    def update_image(self, label, image_path):
        # 加载新图片并调整大小
        new_photo = PhotoImage(file=image_path)
        if image_path==new_image_path_1 or new_image_path_2:
            max_width=max_width_up
            max_height=max_height_up
        else:
            max_width=max_width_down
            max_height=max_height_down
                
        new_photo = new_photo.subsample(max(new_photo.width() // max_width, 1),
                                        max(new_photo.height() // max_height, 1))
            
        # 更新Label的图像
        label.config(image=new_photo)
        # 保存对新图片的引用，防止垃圾回收
        label.image = new_photo
        
    def check_audio(self):
        if audio.object==None:
            messagebox.showinfo("提示", "请打开音频或者录制音频！")
            return False
        else:
            return True


if __name__ == "__main__":
    root = tk.Tk()
    root.title("数字信号处理")
    # 获取屏幕宽度和高度
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 设置窗口大小
    root.geometry("{}x{}".format(screen_width, screen_height))

    # root.geometry("1150x800+100+100")
    app = Application(root)
    audio = Audio()
    root.mainloop()
