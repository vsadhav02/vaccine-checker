from apscheduler.schedulers.blocking import BlockingScheduler
from notify_me import notify_me
from datetime import datetime
import os
import json

sched = BlockingScheduler()
frequency = int(os.environ['FREQUENCY'])
user_data = json.loads(os.environ['USER_DATA'])
user_dict = dict(user_data)

print(f"You will see vaccine information in next {frequency} minutes...")

# Run cron like scheduler every 10 minutes or so
@sched.scheduled_job('interval', minutes=frequency)
def timed_job():
    print(datetime.now(),
          f': Checking available vaccine slots every {frequency} minutes ....')

    for pincode, mobiles in user_dict.items():
        print('-'*35)
        notify_me(pincode=pincode, mobiles=mobiles)
        print('-'*35, '\n')


sched.start()
