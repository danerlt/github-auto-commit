#!/usr/bin/env python
# -*- coding:utf-8 -*-

from main import main

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


if __name__ == '__main__':
    sched = BlockingScheduler()
    sched.add_job(main, 'interval', days=1, next_run_time=datetime.now())
    sched.start()
