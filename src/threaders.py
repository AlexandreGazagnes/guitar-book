import logging, threading, time


class ThreadManager:
    def __init__(self, funct, timeout, **kwargs) -> None:
        # assert callable(funct)
        # logging.info(funct)
        self.funct = funct
        self.timeout = timeout
        self.kwargs = kwargs
        self.t0 = None
        self.results = None

    def perform(self):
        results = self.funct(**self.kwargs)
        self.results = results

    def start(self):
        self.t0 = threading.Thread(target=self.perform, args=())
        self.t0.start()

    def wait(self):
        for i in range(self.timeout + 2):
            logging.debug(f"round {i}")
            if self.results:
                logging.info(f"{self.t0._is_stopped}")
                return self.results
            time.sleep(1)

        raise TimeoutError(f"error from ThreadManager -> googlesearch run in infinite")

    def run(self):
        self.start()
        return self.wait()
