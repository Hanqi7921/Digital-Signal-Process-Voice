import sounddevice as sd
import numpy as np
import soundfile as sf
import pyAudioKits.audio as ak
from tool.png2gif import PNG2GIF

def add_echo(input_path, output_path, delay_seconds=0.3, decay=0.5):
    """
    给音频添加回声效果（单通道）
    :param input_path: 输入音频文件的路径
    :param output_path: 输出音频文件的路径
    :param delay_seconds: 回声的延迟时间（秒）
    :param decay: 回声的衰减系数
    """
    # 读取音频文件
    samples, sr = sf.read(input_path)
    # 确保音频是单通道的
    if samples.ndim > 1 and samples.shape[1] > 1:
        raise ValueError("Audio is not single-channel")
    
    # 如果是双通道，取其中一个通道
    if samples.ndim > 1:
        samples = samples[:, 0]
 
    # 计算延迟的样本数
    delay_samples = int(delay_seconds * sr)
    # 创建一个空的数组来存储带有回声的音频
    echo_samples = np.zeros(len(samples) + delay_samples)
    # 添加原始音频
    echo_samples[delay_samples:] = samples
    # 添加延迟和衰减的音频
    echo_samples[:delay_samples] = decay * samples[-delay_samples:]
    # 将带有回声的音频数据叠加到原始音频上
    echo_samples[delay_samples:] += decay * echo_samples[:len(samples)]
    # 写入带有回声的音频到新的WAV文件
    output_audio = ak.Audio(echo_samples, sr)
    output_audio.save(direction = "library\output_echo.wav")
    output_audio.plot(imgPath="Img_result\PNG\change.png")
    PNG2GIF()
    output_audio.sound()
