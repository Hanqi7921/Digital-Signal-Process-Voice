import pyAudioKits.record
import pyAudioKits.audio as ak
import pyAudioKits.analyse as aly
import sounddevice as sd  
import numpy as np  
from tool.png2gif import PNG2GIF

class Audio:
    def __init__(self):
        self.object = None
        self.samples = None
        self.sr = None
        self.duration = None

    def play(self):
        type(self.object)
        self.object.sound()

    def record(self, sr, recordSeconds):
        print("开始录制...")  
        return pyAudioKits.record.record(sr,recordSeconds)

    def read(self, path):
        # print(self.read_Audio(path))
        self.object = ak.read_Audio(path)
        return self.object 

    def plot(self):
        print("开始绘制波形图...")
        self.object.plot(imgPath="Image\PNG\original.png")
        aly.FFT(self.object.framing()).plot(freq_scale="mel", plot_type="dB",imgPath="Image\PNG\original_fft.png")
        PNG2GIF()
        

