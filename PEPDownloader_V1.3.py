# Ver 1.0 下载六年级上学期英语（三起）课本的图片，并合并为 PDF 文件
# Ver 1.1 下载六年级上学期语文、数学、英语
# Ver 1.2 改为命令行参数方式：传入课本地址和课本名称
# Ver 1.3 显示下载进度、合并 PDF 文件进度
# Ver 2.0 TODO: 下载指定科目、年级的所有课本——目前来看采用了加密，虽然简单加密但略麻烦，需要换种方式实现
import os
import requests
import argparse
from tqdm import tqdm
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

Version = "1.3"


def merge_images_to_pdf(bookName):
    # 获取目录名作为 PDF 文件名
    pdf_file = f"{bookName}.pdf"

    # 创建一个新的 PDF 文件
    c = canvas.Canvas(pdf_file, pagesize=A4)

    # 遍历目录中的所有文件
    image_files = []
    for file in os.listdir(bookName):
        file_path = os.path.join(bookName, file)
        if os.path.isfile(file_path) and file.lower().endswith(
            (".png", ".jpg", ".jpeg")
        ):
            image_files.append(file_path)

    # 按文件名排序图片文件列表
    image_files.sort()

    print("| 开始合并教材高清图片为 PDF：")
    # 遍历图片文件列表，并将每张图片添加到 PDF 中
    for image_file in tqdm(image_files, desc="| 合并图片进度"):
        # 打开图片文件
        img = ImageReader(image_file)
        width, height = img.getSize()
        aspect_ratio = width / float(height)
        page_width, page_height = A4

        # 调整图像大小以填满页面
        if aspect_ratio < 1:
            img_width = page_width
            img_height = img_width / aspect_ratio
        else:
            img_height = page_height
            img_width = img_height * aspect_ratio

        # 将图像居中放置在页面上
        x = (page_width - img_width) / 2
        y = (page_height - img_height) / 2

        # 将图片添加到 PDF 页面中
        c.drawImage(image_file, 0, 0, width=img_width, height=img_height)
        c.showPage()

        # print("添加图片", image_file, width, height, img_width, img_height, end="")

    # 保存 PDF 文件
    c.save()

    print(f"| 教材 PDF 合并完毕：{pdf_file}\r\n")


def downloadBookImages(bookId, bookName):
    folder_name = bookName
    bookUrl = f"https://book.pep.com.cn/{bookId}/files/mobile/"

    # 创建文件夹
    os.makedirs(folder_name, exist_ok=True)

    # 遍历图片编号
    total = 201
    # progressbar = ProgressBar(max_value=total-1, prefix='下载进度：', suffix='第%(index)d页/预计总%(max_value)d页')

    print(f"| 开始下载教材高清图片：《{bookName}》\t{bookId}\t{bookUrl}")
    for i in tqdm(range(1, total), desc="| 下载图片进度", bar_format='| 第{n}页/预估不超过{total_fmt}页 [耗时{elapsed}秒, {rate_fmt}]', unit='页'):
        padded_number = str(i).zfill(3)
        url = f"{bookUrl}{i}.jpg"

        response = requests.get(url)

        if response.status_code == 404:
            # print(f"图片 {i}.jpg 不存在，停止抓取")
            break

        file_path = os.path.join(folder_name, f"{padded_number}.jpg")
        with open(file_path, "wb") as file:
            file.write(response.content)
            # 进度条显示下载进度
            # progressbar.next()
            # print(f"图片 {i}.jpg 已保存          ", end="")

    print(f"| 下载完成，共 {i - 1} 页。\r\n")
    # progressbar.finish()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=f"人教版教材电子版下载工具 V{Version}")
    parser.add_argument(
        "url", help='要下载的教材地址，如："https://book.pep.com.cn/1221001601141/"'
    )
    parser.add_argument("name", help='书名，如："人教版小学数学-六年级-上"')
    parser.add_argument("id", nargs="?", help='要下载的教材的ID，如："1221001601141"')

    args = parser.parse_args()

"""{ bookId = "1212001602145"
bookName = "人教版小学英语（三年级起点）六年级-上"

bookId = "1211001601191"
bookName = "人教版小学语文六年级-上"

bookId = "1221001601141"
bookName = "人教版小学数学六年级-上"
"""

# 如果传入的参数为 ID，则直接下载，否则从 URL 中提取 ID
if args.id:
    bookId = args.id
else:
    bookId = args.url.split("/")[-2]

bookName = args.name
# 下载书的图片
downloadBookImages(bookId, bookName)
# 合并为 PDF 文件
merge_images_to_pdf(bookName)
