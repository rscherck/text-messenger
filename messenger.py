import os
import json
import requests


servicePlanId = os.environ['SERVICE_PLAN_ID']
apiToken = os.environ['API_TOKEN']
sinchNumber = os.environ['SINCH_NUMBER']
url = "https://us.sms.api.sinch.com/xms/v1/" + servicePlanId + "/batches"
message = "This is a test message from Automated Mass Messenger"
number_list = os.environ['TEXT_NUMBERS'].split(",")


def send_message():
    payload = {
        "from": sinchNumber,
        "to": number_list,
        "body": message
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + apiToken
    }

    response = requests.post(url, json=payload, headers=headers)

    data = response.json()
    print(data)


if __name__ == "__main__":
    try:
        print(f'Sending texts to the following: {number_list}')
        print(f'Message: {message}')
        send_message()

    except:
        print("We broke")
        exit(1)
