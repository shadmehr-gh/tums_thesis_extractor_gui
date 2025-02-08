from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
import time
import os
from os.path import isfile, isdir
import shutil

click_count = 0


def folder_preparator():
    downloads_path = str(Path.home() / "Desktop")
    files_path = downloads_path + "/lib.tums.ac.ir"
    if isdir(files_path + "/extracted_pages"):
        shutil.rmtree(files_path + "/extracted_pages")
    if not isdir(files_path):
        os.mkdir(files_path)
    if not isdir(files_path + "/extracted_pages"):
        os.mkdir(files_path + "/extracted_pages")


def downloader(web_link, biblioId, page_count, wait_time):
    downloads_path = str(Path.home() / "Desktop")
    files_path = downloads_path + "/lib.tums.ac.ir"

    geckodriver = "geko_driver/"
    # print(os.path.abspath(geckodriver))
    os.environ["firefox selenium driver"] = geckodriver

    driver = webdriver.Firefox()

    driver.get(web_link)

    #print("Extracting Thesis Pages...")

    for p in range(int(page_count)):
        #url = f"https://lib.tums.ac.ir/exImageDraw?startPage={p+1}&endPage={p+1}&scale=100&language=fa&multimediaId={str(multimediaId)}&biblioId={str(biblioId)}"
        pages_path = files_path + "/extracted_pages"
        page_path = f"{pages_path}/exImageDraw{p+1}.png"

        #print(page_path)
        #print(url)

        image_box = driver.find_element(By.ID, 'showhide-setwidth')
        #attribute_1 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "org"))).get_attribute("attribute_name")
        #print(image_box.get_attribute("height"))
        #driver.execute_script("arguments[0].setAttribute('value',arguments[1])", "style", "margin: auto; width: 700px; height: 1000px;")
        #driver.execute_script("arguments[0].setAttribute('height',arguments[1])", image_box, "1000px")
        driver.execute_script("arguments[0].setAttribute('style',arguments[1])", image_box, "margin: auto; width: 700px; height: 1000px;")

        image_viewer = driver.find_element(By.NAME, 'imageViewer')
        """
        src = image_viewer.get_attribute('src')
        image_viewer = requests.get(src)
        with open('image.jpg', 'wb') as writer:
            writer.write(image_viewer.content)
        """

        screenshot_as_bytes = image_viewer.screenshot_as_png
        with open(page_path, 'wb') as f:
            f.write(screenshot_as_bytes)

        userid = driver.find_element(By.NAME, 'curPageNumber')
        userid.clear()
        userid.send_keys(str(p + 2))
        submit = driver.find_element(By.NAME, 'gotopage')
        submit.click()

        time.sleep(int(wait_time))

    driver.close()

    return "Pass"
