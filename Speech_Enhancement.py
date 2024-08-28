import pyAudioKits.audio as ak
import pyAudioKits.analyse as aly
import pyAudioKits.filters as flt
import pyAudioKits.algorithm as alg


#Spectral subtraction:https://github.com/HarmoniaLeo/pyAudioKits/blob/main/7.%20Speech%20enhancement:%20spectral%20subtraction%2C%20Wiener%20and%20Kalman.ipynb
def Spectral_subtraction(before_audio):
    after_audio=alg.specSubstract(before_audio,before_audio[before_audio.getDuration()-0.8:])
    after_audio.sound()
