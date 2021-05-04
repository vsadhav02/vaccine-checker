from apscheduler.schedulers.blocking import BlockingScheduler
from notify_me import notify_me
from datetime import datetime
import os

sched = BlockingScheduler()
frequency = int(os.environ['FREQUENCY'])

# Run cron like scheduler every 10 minutes or so
@sched.scheduled_job('interval', minutes=frequency)
def timed_job():
    print('-'*35)
    print(datetime.now(),
          f': Checking available vaccine slots every {frequency} minutes ....')
    notify_me()
    print('-'*35, '\n')


sched.start()
