import os
import subprocess
import sys
from tqdm import tqdm

# 转换 FLV 文件为 MP4 文件
def convert_flv_to_mp4(source_folder, skip_existing=True, delete_flv=False):
    flv_files = []
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith(".flv"):
                flv_files.append(os.path.join(root, file))

    progress_bar = tqdm(total=len(flv_files), desc="Converting FLV to MP4", unit="file")
    for flv_file in flv_files:
        destination_file = os.path.splitext(flv_file)[0] + ".mp4"
        command = ["ffmpeg", "-y", "-i", flv_file, "-c:v", "copy", "-c:a", "copy", "-v", "quiet", destination_file]
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        if skip_existing and os.path.exists(destination_file):  # 判断是否跳过已存在的文件
            with open("log.txt", "a", encoding="utf-8") as log_file:
                log_file.write("⨳⨳⨳ Skipping conversion, destination file already exists:" + destination_file)
        else:
            with open("log.txt", "a") as log_file:
                log_file.write(output.decode("utf-8"))
            #subprocess.call(["ffmpeg", "-y", "-i", flv_file, "-c:v", "copy", "-c:a", "copy", destination_file], stdout=subprocess.DEVNULL)
        progress_bar.update(1)
        if delete_flv:
            os.remove(flv_file)
    progress_bar.close()

# 
if __name__ == "__main__":  # 判断是否为主程序
    if len(sys.argv) < 2:  # 判断传入参数数量是否小于2
        print("Usage: python convert_flv.py <source_folder> [delete_flv]")  # 打印用法信息
        sys.exit(1)  # 退出程序并返回状态码1

    source_folder = sys.argv[1]  # 将第二个参数赋值给 source_folder 变量
    skip_existing = True  # 初始化 skip_existing 变量为 True
    if len(sys.argv) >= 3 and sys.argv[2].lower() in ["false", "no", "n"]:  # 判断第三个参数是否存在且为否定
        skip_existing = False  # 如果是，则将 skip_existing 变量设置为 False
    delete_flv = False  # 初始化 delete_flv 变量为 False
    if len(sys.argv) >= 4 and sys.argv[3].lower() in ["true", "yes", "y"]:  # 判断第三个参数是否存在且为"true"、"yes"或"y"
        delete_flv = True  # 如果是，则将 delete_flv 变量设置为 True

    convert_flv_to_mp4(source_folder, skip_existing, delete_flv)  # 调用convert_flv_to_mp4函数，传入source_folder和delete_flv变量作为参数
