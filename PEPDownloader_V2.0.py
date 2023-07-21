# Ver 2.0 下载指定科目、年级的所有课本
import os
import requests
import argparse
from tqdm import tqdm
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

# 引入 playWright 包
from playwright.sync_api import sync_playwright

Version = "2.0"


def click_element_by_text(page, text):
    page.evaluate(
        """(text) => {
        const elements = document.querySelectorAll('li.item');
        for (const element of elements) {
            if (element.textContent.trim() === text) {
                element.click();
                break;
            }
        }
    }""",
        text,
    )


def QueryCatalogPage(major="语文", grade="六年级", school="小学", keywords=""):
    base_url = "http://jc.pep.com.cn/"
    # 用 playWright 读取电子教材目录页
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=False,
            executable_path=r"chrome-win\chrome.exe",
        )
        context = browser.new_context()
        page = context.new_page()

        page.goto(base_url)
        # 点击小学
        click_element_by_text(page, school)
        # 点击科目
        click_element_by_text(page, major)
        # 点击年级
        click_element_by_text(page, grade)
        # 选取指定科目的所有课本
        elements = page.query_selector_all("a.read")

        # 提取href和title属性，并保存为元组的数组
        results = []
        for element in elements:
            bookUrl = element.get_attribute("href")
            bookName = element.get_attribute("title")
            if keywords != "":
                # 拆分 keywords 为数组
                keys = keywords.split(" ")
                # 同时包含所有关键字
                if all(key in bookName for key in keys):
                    results.append((bookUrl, bookName))
            elif keywords == "":
                results.append((bookUrl, bookName))
        # input("按回车键继续……")
        browser.close()

    # 返回课本列表
    return results


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
    print(f"| 开始下载教材高清图片：《{bookName}》\t{bookId}\t{bookUrl}")
    for i in tqdm(
        range(1, total),
        desc="| 下载图片进度",
        bar_format="| 第{n}页/预估不超过{total_fmt}页 [耗时{elapsed}秒, {rate_fmt}]",
        unit="页",
    ):
        padded_number = str(i).zfill(3)
        url = f"{bookUrl}{i}.jpg"

        response = requests.get(url)

        if response.status_code == 404:
            # print(f"图片 {i}.jpg 不存在，停止抓取")
            break

        file_path = os.path.join(folder_name, f"{padded_number}.jpg")
        with open(file_path, "wb") as file:
            file.write(response.content)

    print(f"| 下载完成，共 {i - 1} 页。\r\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=f"人教版教材电子版下载工具 V{Version}")
    parser.add_argument("major", help="学科，如 语文、数学、英语")
    parser.add_argument("grade", help="年级，如：一年级、二年级、三年级")
    parser.add_argument("school", help="学段，如：小学、初中、高中")
    parser.add_argument(
        "keywords", nargs="?", help='标题必须包含关键字，如 "上册"、"三年级起点"，多个关键字之间用空格分隔'
    )

    args = parser.parse_args()

major = args.major
grade = args.grade
school = args.school
if args.keywords:
    keywords = args.keywords
else:
    keywords = ""
bookList = QueryCatalogPage(major=major, grade=grade, school=school, keywords=keywords)

# for book in bookList:
#    print(book)

i = 0
total = bookList.__len__()
for book in bookList:
    # 下载书的图片
    bookId = book[0].split("/")[3]
    bookName = book[1]
    i += 1
    print(f"\r\n☆ {i}/{total} ☆ 下载教材：《{bookName}》\t{bookId}")
    downloadBookImages(bookId, bookName)
    # 合并为 PDF 文件
    merge_images_to_pdf(bookName)
