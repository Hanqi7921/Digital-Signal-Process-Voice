import pyAudioKits.audio as ak
import numpy as np
import pyAudioKits.analyse as aly
import pyAudioKits.algorithm as alg
from tool.png2gif import PNG2GIF

#https://github.com/HarmoniaLeo/pyAudioKits/blob/main/6.%20Endpoint%20Detection%20and%20Speech%20Recognition.ipynb
def Speech_Endpoint(detect_audio):
    vad_result = alg.VAD(detect_audio, 0.05, 0.5, 400)    
    # '''
    # Endpoint detection for the recording, 
    # setting a lower short-time energy threshold of 0.05, 
    # a higher short-time energy threshold of 0.5, 
    # and a short-time over-zero rate threshold of 400
    # '''
    vad_result.plot(imgPath="Img_result\PNG\change.png")
    aly.FFT(vad_result.framing()).plot(freq_scale="mel", plot_type="dB",imgPath="Img_result\PNG\change_fft.png")
    PNG2GIF()