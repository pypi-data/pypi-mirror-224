#
#  Created by IntelliJ IDEA.
#  User: jahazielaa
#  Date: 07/12/2022
#  Time: 01:37 p.m.
"""Threads manager

This file allows the user to call functions n times per second.

This file requires the following imports: 'time'.

This file contains the following functions:
    * start_threads - starts threads for requested functions
"""
import time

from curt.repeated_timer import RepeatedTimer


def start_threads(time_length: 'int',
                  functions: 'list',
                  threads_number: 'int'):
    """
    Calls a function threads_number times per second during time_length seconds.
    Parameters
    ----------
    time_length : int
        Process length in seconds
    functions : list
        Functions names list
    threads_number : int
        Number of threads per second

    Returns
    -------
    None
    """
    print('starting threads')
    threads = []
    for i in range(threads_number):
        for function in functions:
            threads.append(RepeatedTimer(1, function))
        time.sleep(1 / threads_number)
    try:
        time.sleep(time_length - 1)
    finally:
        for thread in threads:
            thread.stop()
    print('threads stopped')
