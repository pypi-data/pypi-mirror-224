# from multiprocessing import Pool, cpu_count, freeze_support, Lock
from multiprocessing import Pool, freeze_support, Lock
import time
from contextlib import closing
import sys
from psutil import cpu_count, virtual_memory
from .misc import cprint

def multithread(func,input,progressbar=None,threads=None,status=None):
        #~ freeze_support()
        if threads is None:
                # threads=int(cpu_count())+1
                # Modified 10/8/23 to prevent memory errors on machines with ++CPU cores and --RAM.
                minimum_memory_per_thread = 256  # specify this in MB
                available_memory = (virtual_memory().available)//(1024*1024)
                max_threads_mem = available_memory//minimum_memory_per_thread
                max_threads_cpu = int(cpu_count())+1
                if max_threads_mem<max_threads_cpu:
                        cprint("INFO: Threads limited by available RAM")
                        cprint("INFO: Minimum {} MB RAM per thread".format(available_memory//max_threads_mem))
                        threads=max_threads_mem
                else:
                        cprint("INFO: Threads limited by available CPU cores")
                        cprint("INFO: Minimum {} MB RAM per thread".format(available_memory//max_threads_cpu))
                        threads=max_threads_cpu
        pool = Pool(threads)
        cprint("INFO: Running on {} threads".format(threads))
        result = pool.map_async(func,input,chunksize=1)
        while not result.ready():
                if not progressbar is None:
                        progress = (float(len(input))-float(result._number_left))/float(len(input))*100.
                        #~ print "PROGRESS", progress
                        progressbar(progress,update=False)
                if not status is None:
                        jobnumber = len(input)-result._number_left + 1
                        status('Reading file: '+'/'.join([str(jobnumber),str(len(input))]))
                #~ print("num left: {}".format(result._number_left))
                # time.sleep(0.1)
        if not progressbar is None:
                progressbar(0.)
        if not status is None:
                status('')
        # print("Closing multiprocessing pool")
        pool.close()
        # print("Joining pool")
        pool.join()
        # print("Fetching pool results")
        return result.get()
