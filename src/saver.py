import time, threading, sys, pickle
import logging

import config

class save_thread(threading.Thread):
    def __init__(self, conv_handler, dp):
        threading.Thread.__init__(self)
        self.name = "SaverThread"
        self.conv_handler = conv_handler
        self.dp = dp
        self.kill_received = False

    def run(self):
        while True:
            for i in range(60):
                if self.kill_received:
                    self.saveData()
                    return
                time.sleep(1)
            self.saveData()

    def saveData(self):
        # Before pickling
        resolved = dict()
        for k, v in self.conv_handler.conversations.items():
            if isinstance(v, tuple) and len(v) is 2 and isinstance(v[1], Promise):
                try:
                    new_state = v[1].result()  # Result of async function
                except:
                    new_state = v[0]  # In case async function raised an error, fallback to old state
                resolved[k] = new_state
            else:
                resolved[k] = v
        try:
            f = open(config.CONVERSATIONS_FILE, 'wb+')
            pickle.dump(resolved, f)
            f.close()
            f = open(config.USERDATA_FILE, 'wb+')
            pickle.dump(self.dp.user_data, f)
            f.close()
            logging.info('Current state saved')
        except:
            logging.error(sys.exc_info()[0])

def loadData(conv_handler, dp):
    try:
        f = open(config.CONVERSATIONS_FILE, 'rb')
        conv_handler.conversations = pickle.load(f)
        f.close()
        f = open(config.USERDATA_FILE, 'rb')
        dp.user_data = pickle.load(f)
        f.close()
        logging.info('Data loaded')
    except FileNotFoundError:
        logging.error("Data file not found")
    except:
        logging.error(sys.exc_info()[0])