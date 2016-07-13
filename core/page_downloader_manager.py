# -*- coding: utf-8 -*-
import time
import urllib
import requests
import re
import sys
from utils.custom_logger import *
from utils.utils_functions import *
from settings.settings import *
from selenium import webdriver
from urlparse import urlparse
from threading import Thread

reload(sys)
sys.setdefaultencoding("utf-8")

custom_logger = CustomLogger()


class PageDownloaderManager:

    def __init__(self):
        self.tmp_mp4_file = ""
        self.total_download = 0
        self.total_size = 0
        self.file = ""

    def get_page(self, url):
        try:
            custom_logger.log("Pobieranie pliku z {0}".format(url))
            browser = webdriver.Chrome(CHROMEDRIVER_PATH)
            browser.get(url)
            html_source = browser.page_source
            browser.close()
            self._store_tmp_mp4_file(html_source)

            return self._load_data_from_html(html_source)
        except Exception as e:
            print(e)
            custom_logger.log("Nie mozna pobrac pliku {0}".format(url))
            return None

    def _store_tmp_mp4_file(self, html_source):
        flashvars = get_substring(html_source, "<param name=\"flashvars\"", "/")
        flashvarsvalue = get_substring(flashvars, "value=\"", "\"")
        mp4_url = [m.replace("file=", "") for m in flashvarsvalue.split("&amp;") if m.endswith(".mp4")]
        if len(mp4_url) > 0:
            mp4_url = mp4_url[0]
        else:
            mp4_url = [m.replace("file=", "") for m in flashvarsvalue.split("&amp;") if ".flv" in m][0]
        self.tmp_mp4_file = urllib.unquote(mp4_url)

    def _load_data_from_html(self, html_source):
        html_source = html_source.split("\n")
        title = self._get_tilte_from_file(html_source)
        mp4_file = self._get_mp4_file(html_source)
        if title:
            title = "files/" + self._parse_title(title)
        parsed_url = urlparse(mp4_file)
        if not bool(parsed_url.scheme):
            mp4_file = self.tmp_mp4_file
        return title, mp4_file

    def _get_tilte_from_file(self, content):
        for line in content:
            titles = re.findall(TITLE_REGEX, line)
            if len(titles) > 0:
                return titles[0]
        return None

    def _get_mp4_file(self, content):
        for line in content:
            mp4_files = re.findall(MP4_FILE_EXTENSION, line)
            if len(mp4_files) > 0:
                mp4_file = re.findall(MP4_FILE_REGEX, line)
                if len(mp4_file) > 0:
                    return mp4_file[0]
        return None

    def _parse_title(self, title):
        return decode_and_replace_polish_chars(title)\
                   .replace("/","")\
                   .replace(" ", "_")\
                   .replace("_-_", "_")\
                   .replace(".", "_") + MP4_FILE_EXTENSION

    def download_file(self, file_name, link):
        self.file = file_name
        if is_file_exists(file_name):
            custom_logger.log("Plik {0} jest pobrany".format(file_name))
            return
        try:
            if ".flv" in link:
                file_name = file_name.replace(".mp4", ".flv")
            with open(file_name, "wb") as f:
                response = requests.get(link, stream=True, headers=HEADERS)
                total_length = response.headers.get('content-length')
                custom_logger.log("total_length " + str(total_length))
                custom_logger.log("Rozmiar pliku {0}".format(sizeof_fmt(int(total_length))))

                #t = self._start_printing_progress(total_length)

                self.total_size = total_length

                if total_length is None:
                    f.write(response.content)
                else:
                    total_length = int(total_length)
                    buffer_size = 2048
                    for data in response.iter_content(chunk_size=buffer_size):
                        self.total_download += len(data)
                        f.write(data)
                        """
                        done = int(200 * self.total_download / total_length)
                        sys.stdout.write("\r[%s%s] %s" %
                                         (
                                           '=' * done,
                                           ' ' * (200-done),
                                           str(self.total_download)
                                          )
                                         )
                        sys.stdout.flush()
                        """
                        #time.sleep(0.001)
                #t.join()
            custom_logger.log("\nUkonczono pobieranie {0}".format(file_name))
            delete_file(file_name)
        except KeyboardInterrupt:
            custom_logger.log("\nKeyboardInterrupt")
            delete_file(file_name)
        except Exception as e:
            delete_file(file_name)
            custom_logger.log("Error: {0}".format(e))
            custom_logger.log("Blad pobierania pliku {0}".format(file_name))

    def _start_printing_progress(self, total_length):
        t = Thread(target=self._process_progress, args=(total_length, ))
        t.start()
        return t

    def _process_progress(self, total_length):
        download = int(self.total_download)
        total = int(total_length)
        _sum = 0
        while True:
            diff = int(self.total_download) - download
            _sum += diff
            #sys.stdout.write("\r" + str(diff / float(1000000)) + " " + str(total) + "\n")
            #sys.stdout.flush()

            done = int(200 * int(self.total_download) / int(total_length))
            speed_val = diff / float(1000000)
            speed = str(round(speed_val, 1)) + " Mb/s"
            sys.stdout.write("\r[%s%s] %s" %
                             (
                               '=' * done,
                               ' ' * (200-done),
                               speed
                              )
                             )
            sys.stdout.flush()

            download = int(self.total_download)
            time.sleep(1)
            if download >= total:
                break
        #print("sum " + str(_sum) + " of " + str(total_length))