# 数字信号处理

## 文件说明

### function--功能函数

audio_record 录音功能，为简化代码而封装起来（后面发现用不着）
Speech_Echo 添加回声、去掉回声
Speech_Endpoint 语音端点检测
Speech_Enhancement 语音增强（好像又名语音去噪）

### Image--图片位置

GIF .gif 格式的图片（输入、输出音频时域图像、fft 图像）
PNG .png 格式的图片（输入、输出音频时域图像、fft 图像）
注：项目 demo 用的 tkinter 作为 ui，只接受 gif

### Wav--音频位置

output_clean.wav 消除回声后的文件
output_echo.wav 添加回声后的文件
SHU.wav 录音结束后保存至该文件
tmp.wav 系统运行产生的中间文件，用户无需关注（我还没搞懂怎么把它隐藏）
test.wav 网上下载用来测试的文件，是一段人声英文

## 程序入口

    运行main.py
