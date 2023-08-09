import logging

import threading

import time


def thread_function(name):
    logging.info("Thread %s: starting", name)

    time.sleep(2)

    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"

    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")

    x = threading.Thread(target=thread_function, args=(1,))

    logging.info("Main    : before running thread")

    x.start()

    logging.info("Main    : wait for the thread to finish")

    # x.join()

    logging.info("Main    : all done")


from googlesearch import search
import time


class ThreadManager:
    def __init__(self, query, sleep=15) -> None:
        self.query = query
        self.t0 = None
        self.t1 = None
        self.url_list = []
        self.sleep = sleep

        self.thread_list = []

    def requests(self, _query):
        if _query == "skip":
            return 1

        li = search(_query)
        res = [i for i in li]
        self.url_list = res

    def start(self):
        self.t0 = threading.Thread(target=self.requests, args=(self.query,))
        self.t0.start()

    def run(self):
        self.start()
        for i in range(self.sleep):
            logging.info(f"round {i}")
            if self.url_list:
                logging.info(f"{self.t0._is_closed}")
                return self.url_list

            time.sleep(1)
        return "None !!!"
