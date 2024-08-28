import pyAudioKits.record
import pyAudioKits.audio as ak
import sounddevice as sd  
import numpy as np  
from tool.png2gif import PNG2GIF

class Audio:
    def __init__(self):
        self.object = None
        self.samples = None
        self.sr = None
        self.duration = None

    def play(self,audiopj):
        audiopj.sound()

    def record(self, sr, recordSeconds):
        print("开始录制...")  
        return pyAudioKits.record.record(sr,recordSeconds)

    def read(self, path):
        # print(self.read_Audio(path))
        return ak.read_Audio(path)

    def plot(self,audiopj):
        print("开始绘制波形图...")
        audiopj.plot(start=0, end=None, ylim=None, ax=None, imgPath="Img_result\PNG\original.png", xlabel="t/s")
        PNG2GIF()
        

