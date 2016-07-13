from core.page_downloader_manager import *
from settings.settings import *
from threading import Thread
from progress_thread import ProgressThread
import json
import time

custom_logger = CustomLogger()

"""
Main method that run logic
"""
def run_logic(args):

    progressThread = ProgressThread()
    threads = []
    with open(CONFIG_JSON_FILES_FILE) as data_file:
        data = json.load(data_file)
        for file_url in data:
                t = Thread(target=process_file, args=(file_url, progressThread))
                threads.append(t)

    for x in threads:
        time.sleep(1)
        x.start()

    time.sleep(0.1)
    progressThread.start_thread()

    for x in threads:
        x.join()

    progressThread.join_thread()


def process_file(file_url, progressThread):
    pageDownloaderManager = PageDownloaderManager()
    progressThread.add_downloader(pageDownloaderManager)
    #data = pageDownloaderManager.get_page(file_url)
    data = ("files/Polska_na_Euro_2016_video_w_cda_pl.mp4?" + str(time.time()),"http://vrbx157.cda.pl/SJiaMWsJN3knuG7_4ruWVA/1467920459/vlb050fe1b727cd864dd2834828a6dcb2b.mp4")
    if data:
        custom_logger.log("Wynikowa nazwa pliku " + data[0])
        custom_logger.log("Url do wideo " + data[1])
        pageDownloaderManager.download_file(data[0], data[1])
    else:
        custom_logger.log("Blad pobieranie danych")
