import sounddevice as sd
import numpy as np
import soundfile as sf
import pyAudioKits.audio as ak
import pyAudioKits.analyse as aly
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
    aly.FFT(output_audio.framing()).plot(freq_scale="mel", plot_type="dB",imgPath="Img_result\PNG\change_fft.png")
    PNG2GIF()
    output_audio.sound()

def estimate_echo_path(input_signal, delay, decay):
    """
    估计回声路径。
    
    :param input_signal: 输入信号（主信号+回声）
    :param delay: 回声的延迟时间（以采样点数表示）
    :param decay: 回声的衰减系数
    :return: 估计的回声信号
    """
    # 创建一个自适应滤波器
    filter_length = 512  # 滤波器长度
    mu = 0.01  # 步长
    
    # 初始化滤波器权重
    w = np.zeros(filter_length)
    
    # 初始化输出信号
    echo_signal = np.zeros_like(input_signal)
    
    # 自适应滤波器迭代
    for n in range(filter_length, len(input_signal)):
        # 计算滤波器的输出
        x = np.flipud(input_signal[n - filter_length:n])
        y = np.dot(w, x)
        
        # 计算误差
        e = input_signal[n] - y
        
        # 更新滤波器权重
        w += mu * e * x
        
        # 存储输出信号
        echo_signal[n] = y
    
    # 裁剪估计的回声信号以匹配延迟
    echo_signal = echo_signal[delay:]
    
    # 应用衰减
    echo_signal *= decay

        # 确保 echo_signal 长度与 input_signal 相同
    if len(echo_signal) < len(input_signal):
        echo_signal = np.pad(echo_signal, (0, len(input_signal) - len(echo_signal)), mode='constant')
    elif len(echo_signal) > len(input_signal):
        echo_signal = echo_signal[:len(input_signal)]
    return echo_signal

def remove_echo(input_path, delay=100, decay=0.5):
    """
    使用自适应滤波器去除回声。
    
    :param input_signal: 输入信号（主信号+回声）
    :param delay: 回声的延迟时间（以采样点数表示）
    :param decay: 回声的衰减系数
    :return: 去除回声后的信号
    """
    # 估计回声信号
    # 读取音频文件
    input_signal, sr = sf.read(input_path)  # 主信号+回声
    print("are")
    echo_signal = estimate_echo_path(input_signal, delay, decay)
    print("let")
    # 从原始信号中减去估计的回声信号
    clean_signal = input_signal - echo_signal
    print("yes")
    output_audio = ak.Audio(clean_signal, sr)
    print("no")
    output_audio.save(direction = "library\output_clean.wav")
    print("haha")
    output_audio.plot(imgPath="Img_result\PNG\change.png")
    aly.FFT(output_audio.framing()).plot(freq_scale="mel", plot_type="dB",imgPath="Img_result\PNG\change_fft.png")
    PNG2GIF()
    output_audio.sound()

