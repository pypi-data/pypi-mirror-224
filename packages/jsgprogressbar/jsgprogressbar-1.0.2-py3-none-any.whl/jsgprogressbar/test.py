from progressbar import progressbar
from time import sleep

for i in progressbar(range(0,10),"Loading ",100):
    sleep(1)
