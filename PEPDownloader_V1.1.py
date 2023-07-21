# Ver 1.0 下载六年级上学期英语（三起）课本的图片，并合并为 PDF 文件
# Ver 1.1 下载六年级上学期语文、数学、英语
# Ver 2.0 TODO: 下载指定科目、年级的所有课本——目前来看采用了加密，虽然简单加密但略麻烦，需要换种方式实现
import os
import requests
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

def merge_images_to_pdf(bookName):
    # 获取目录名作为 PDF 文件名
    pdf_file = f"{bookName}.pdf"
    
    # 创建一个新的 PDF 文件
    c = canvas.Canvas(pdf_file, pagesize=A4)
    
    # 遍历目录中的所有文件
    image_files = []
    for file in os.listdir(bookName):
        file_path = os.path.join(bookName, file)
        if os.path.isfile(file_path) and file.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_files.append(file_path)
    
    # 按文件名排序图片文件列表
    image_files.sort()
    
    # 遍历图片文件列表，并将每张图片添加到 PDF 中
    for image_file in image_files:
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

    
        print("添加图片", image_file, width, height, img_width, img_height)
        # 将图片添加到 PDF 页面中
        c.drawImage(image_file, 0, 0, width=img_width, height=img_height)
        c.showPage()
    
    # 保存 PDF 文件
    c.save()
    
    print(f"PDF 文件 {pdf_file} 已创建完毕！")

def downloadBookImages(bookId, bookName):
    folder_name = bookName
    base_url =  "https://book.pep.com.cn/{0}/files/mobile/".format(bookId)
    
    # 创建文件夹
    os.makedirs(folder_name, exist_ok=True)

    # 遍历图片编号
    for i in range(1, 201):
        padded_number = str(i).zfill(3)
        url = f"{base_url}{i}.jpg"
        response = requests.get(url)
        
        if response.status_code == 404:
            print(f"图片 {i}.jpg 不存在，停止抓取")
            break
        
        file_path = os.path.join(folder_name, f"{padded_number}.jpg")
        with open(file_path, "wb") as file:
            file.write(response.content)
            print(f"图片 {i}.jpg 已保存")




bookId = "1212001602145"
bookName = "人教版小学英语（三年级起点）六年级-上"

bookId = "1211001601191"
bookName = "人教版小学语文六年级-上"

bookId = "1221001601141"
bookName = "人教版小学数学六年级-上"

# 下载书的图片
downloadBookImages(bookId, bookName)
# 合并为 PDF 文件
merge_images_to_pdf(bookName)