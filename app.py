from apscheduler.schedulers.blocking import BlockingScheduler
from notify_me import notify_me
from datetime import datetime
import os

sched = BlockingScheduler()
frequency = int(os.environ['FREQUENCY'])
pincodes = os.environ['PINCODES'].split(',')
mobiles = os.environ['MOBILES'].split(',')
print(f"You will see vaccine information in next {frequency} minutes...")

# Run cron like scheduler every 10 minutes or so
@sched.scheduled_job('interval', minutes=frequency)
def timed_job():
    print(datetime.now(),
          f': Checking available vaccine slots every {frequency} minutes ....')

    for pincode in pincodes:
        print('-'*35)
        notify_me(mobiles=mobiles, pincode=pincode)
        print('-'*35, '\n')


sched.start()
