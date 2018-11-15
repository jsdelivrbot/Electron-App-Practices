import threading
import time
from database import Database


class ThreadingExample(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, subDB, interval=20):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval
        self.subDB = subDB

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:
            # Do something
            for db in self.subDB:
                res = db.insert_row(
                    'product', {"name": "temp", "type": "tempType"})

                print(res)
            time.sleep(self.interval)
