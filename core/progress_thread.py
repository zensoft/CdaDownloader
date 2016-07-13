__author__ = 'tomek'
from utils.utils_functions import *
from threading import Thread
import time
import sys

class ProgressThread():

    def __init__(self):
        self.downloaders = []
        self.thread = None

    def add_downloader(self, downloader):
        self.downloaders.append(downloader)

    def start(self):
        lines = len(self.downloaders) * 2
        sys.stdout.write("\n" * lines) #miejsce na puste linie
        while True:
            self._sleep_one_sec()
            sys.stdout.write(u"\u001b[1000D")
            sys.stdout.write(u"\u001b[" + str(lines) + "A")
            for downloader in self.downloaders:
                lns = self._get_print_lines(downloader)
                for l in lns:
                    print(l)
            if not self._is_any_download():
                break

    def _get_print_lines(self, downloader):
        p = 80
        line_1 = "{0}".format(downloader.file,)
        done = 1
        if downloader.total_size != 0:
            done = int(p * int(downloader.total_download) / int(downloader.total_size))
        line_2 = "[{0}{1}] {2}".format('=' * done, ' ' * (p-done), sizeof_fmt(int(downloader.total_size)))
        return line_1, line_2

    def _is_any_download(self):
        count_ended = 0
        for downloader in self.downloaders:
            if not self._is_download_end(downloader):
                return True
        return False

    def _is_download_end(self, downloader):
        download = int(downloader.total_download)
        total = int(downloader.total_size)
        if total == 0:
            return False
        return download >= total

    def _sleep_one_sec(self):
        time.sleep(1)

    def start_thread(self):
        self.thread = Thread(target=self.start, args=())
        self.thread.start()

    def join_thread(self):
        self.thread.join()
