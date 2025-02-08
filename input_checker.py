import os
import platform
import tarfile
import zipfile

click_count = 0

def id_checker(web_link_get):
    biblioId = ""
    multimediaId = ""
    web_link = web_link_get
    biblioId = web_link[47:53]
    multimediaId = web_link[54:]

    try:
        biblioId_int = int(biblioId)
        multimediaId_int = int(multimediaId)
    except:
        return "Incorrect Thesis Link!"

    if(biblioId_int > 99999 and biblioId_int <= 999999 and multimediaId_int > 9999999 and multimediaId_int <= 999999999):
        return "Pass"
    else:
        return "Incorrect Thesis Link!"


def page_count_checker(page_count_get):
    page_count = page_count_get

    try:
        page_count_int = int(page_count)
    except:
        return "Incorrect Thesis Page Numbers!"

    if(page_count_int >= 1):
        return "Pass"
    else:
        return "Incorrect Thesis Page Numbers!"


def wait_time_checker(wait_time_get):
    wait_time = wait_time_get

    try:
        wait_time_int = int(wait_time)
    except:
        return "Incorrect Wait Time Number!"

    if (wait_time_int >= 1):
        return "Pass"
    else:
        return "Incorrect Wait Time Number!"


def os_checker():
    os_name = platform.system()
    os_arch = platform.machine()
    return os_based_geko_driver_setter(os_name, os_arch)


def os_based_geko_driver_setter(os_name, os_arch):
    if os.path.exists("geko_driver/geckodriver.exe"):
        os.remove("geko_driver/geckodriver.exe")
    elif os.path.exists("geko_driver/geckodriver"):
        os.remove("geko_driver/geckodriver")

    if os_name == "Windows":
        with zipfile.ZipFile('geko_driver/geckodriver-v0.35.0-win32.zip', 'r') as zip_ref:
            zip_ref.extractall('geko_driver')
        return "Pass"
    elif os_name == "Linux" and (os_arch == "AMD64" or os_arch == "x86_64"):
        with tarfile.open('geko_driver/geckodriver-v0.35.0-linux64.tar.gz', 'r') as tar_ref:
            tar_ref.extractall('geko_driver', filter="data")
        return "Pass"
    elif os_name == "Linux" and os_arch == "i386":
        with tarfile.open('geko_driver/geckodriver-v0.35.0-linux32.tar.gz', 'r') as tar_ref:
            tar_ref.extractall('geko_driver', filter="data")
        return "Pass"
    elif os_name == "Linux" and (os_arch == "aarch64"):
        with tarfile.open('geko_driver/geckodriver-v0.35.0-linux-aarch64.tar.gz', 'r') as tar_ref:
            tar_ref.extractall('geko_driver', filter="data")
        return "Pass"
    elif os_name == "Darwin":
        with tarfile.open('geko_driver/geckodriver-v0.35.0-macos.tar.gz', 'r') as tar_ref:
            tar_ref.extractall('geko_driver', filter="data")
        return "Pass"
    else:
        return "Your OS is Not Compatible!"
