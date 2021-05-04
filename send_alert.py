import os
from twilio.rest import Client


def send_alert(mobiles, message):
    # Your Account Sid and Auth Token from twilio.com/console
    # and set the environment variables. See http://twil.io/secure

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    twilio_phone = os.environ['TWILIO_PHONE']
    client = Client(account_sid, auth_token)
    mobile_list = mobiles.split(',')

    # get one phone number at a time. phone numbers should be comma seperated.
    for mobile in mobile_list:
        message = client.messages \
            .create(
                body=message,
                from_=twilio_phone,
                to=mobile
            )


if __name__ == '__main__':
    send_alert(mobiles='your_mobile', message='demo message')
