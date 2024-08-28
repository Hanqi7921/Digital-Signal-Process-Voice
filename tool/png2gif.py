import os
from PIL import Image

# 指定包含PNG图片的目录
source_dir = 'Img_result\PNG'
# 指定转换后的GIF图片存放的目录
output_dir = 'Img_result\GIF'

def PNG2GIF():
    # 遍历指定目录下的所有PNG文件
    for filename in os.listdir(source_dir):
        if filename.endswith('.png'):
            # 完整的PNG文件路径
            png_file_path = os.path.join(source_dir, filename)
            # 打开PNG图片
            png_image = Image.open(png_file_path)
            # 创建GIF文件名和路径
            gif_filename = filename[:-4] + '.gif'
            gif_file_path = os.path.join(output_dir, gif_filename)
            # 将PNG图片转换为GIF并保存到输出目录
            png_image.save(gif_file_path, 'GIF')
            print(f'Converted {filename} to {gif_filename}')
