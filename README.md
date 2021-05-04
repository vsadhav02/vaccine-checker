# Vaccine availability tracker - India

## Introduction

This app will send you sms alert when there is covid-19 vaccine shot available based on your area pin code in India.This app checks availability for next 7 days and you can send sms to multiple phone numbers seperated by comma.

**I have humble request to not run this app too frequently to avoid load on Government API and help fellow citizens to get shots as well.**

## Getting started guide - for local development in linux

1. Create your python virtual environment.

```
python3 -m venv venv
```

2. Activate your virtual environment.

```
source venv/bin/activate
```

3. Install all dependancies.

```
pip install -r requirements.txt
```

4. Load your environment variables saved in .env file as mentioned in next section.

```
source .env
```

5. Run your app.

```
python app.py
```

## Environment Variables for local devlopment in linux

You can save below variables in .env file and then run below command to get them loaded.
You can save multiple mobile numbers like below
"+911234567890,+912345678901"

```
source .env
```

-   export TWILIO_ACCOUNT_SID='your_acc_seed'
-   export TWILIO_AUTH_TOKEN='your_auth_token'
-   TWILIO_PHONE='twilio_prchased_phone'
-   export PINCODE='your_location_pin'
-   export MOBILES='mobile_numbers'
-   export FREQUENCY='10'

## Docker commands

In below examples change "your_repo" word with your docker repository name.

```
docker login
```

```
docker build -t your_repo/cowin-app:v1.0 .
```

```
docker run -it \
-e TWILIO_ACCOUNT_SID='your_acc_seed' \
-e TWILIO_AUTH_TOKEN='your_auth_token' \
-e TWILIO_PHONE='twilio_prchased_phone' \
-e PINCODE='your_location_pin' \
-e MOBILES='mobile_numbers' \
-e FREQUENCY='10' \
--name my-app your_repo/cowin-app:v1.0
```

```
docker push your_repo/cowin-app:v1.0
```

## Few things to remember

1. You have to create free account with Twilio where you get 15$ credit.
2. Purchase a mobile number for 1$ and save it in your `TWILIO_PHONE` environment variable.
3. For free acount you have to verify mobile numbers which you will be sending sms to.
   you have to go to Phone Numbers -> Verified Caller IDs -> Add your mobile number.
4. Got to settings -> General -> API credentials and copy your account SID and Auth Token into environment variables.
5. Update `PINCODE with your location pin code`. If you dont get slots, try changing to nearby pincodes or explore APIsetu link mentioned in references.

## References

-   [Cowin API](https://apisetu.gov.in/public/marketplace/api/cowin/cowin-public-v2)
-   [Python Scheduler](https://stackoverflow.com/questions/22715086/scheduling-python-script-to-run-every-hour-accurately)
-   [Twilio SMS](https://www.twilio.com/docs/sms/quickstart/python)
