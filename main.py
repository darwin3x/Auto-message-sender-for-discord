import requests
import time

MESSAGE_CONTENT = "Type your message here, use '\n' for new line"

TOKEN = "Paste your discord token here"

CHANNEL_IDS = ['channel id 1', 'channel id2 ', 'channel id 3']

url = 'https://discord.com/api/v9'

headers = {
    'authorization': f'{TOKEN}',
    'content-type': 'application/json'
}

while True:
    for channel_id in CHANNEL_IDS:
        # Url constructor
        channel_url = f'{url}/channels/{channel_id}/messages'

        data = {
            'content': MESSAGE_CONTENT
        }

        # Request sender
        response = requests.post(channel_url, headers=headers, json=data)

        # Print logs
        if response.status_code == 200:
            print(f'Message sent successfully to channel {channel_id}!')
        else:
            print(f'Failed to send message to channel {channel_id}: {response.content}')

    # Wait 60 seconds before sending other message
    time.sleep(60)