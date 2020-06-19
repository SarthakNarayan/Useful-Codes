"Converting seconds to HH:MM:SS"

import time
from time import strftime, gmtime

start_time = time.time()
time.sleep(2)
delay = time.time() - start_time
print(strftime("%H:%M:%S", gmtime(delay)))