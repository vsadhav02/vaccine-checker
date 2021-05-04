from send_alert import send_alert
import requests
import urllib3
from datetime import date
import os


def notify_me():
    # supress warning due to self signed certificates for devlopment environment.
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    pincode = os.environ['PINCODE']
    mobiles = os.environ['MOBILES']
    today = date.today().strftime('%d-%m-%Y')

    # get next 7 days vaccine slots near to your area pincode
    url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pincode}&date={today}"

    # always verify signature in production environment
    response = requests.get(url, verify=False)
    output = response.json()

    for center in output['centers']:
        for session in center['sessions']:
            message = f"Center: {center['name']}, Date: {session['date']}, Slots: {session['available_capacity']}"

            # sms me when 1 or more slots are free
            if session['available_capacity'] > 0:
                print('Hurrey!! you have found free slot. Go ahead and book fast!!')
                send_alert(mobiles=mobiles, message=message)
            else:
                print(message)


if __name__ == '__main__':
    notify_me()
