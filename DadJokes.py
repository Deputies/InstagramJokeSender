from instagrapi import Client
import requests
import time

# Set your Instagram username and password
username = "your_instagram_username"
password = "your_instagram_password"

# Set up the Instagrapi client
client = Client()
client.login(username, password)

# Get the user input for joke count and username
joke_count = int(input("Enter the number of jokes you want to send: "))
recipient_username = input("Enter the username of the recipient: ")
send_all_at_once = input("Send all jokes at once? (Y/N)").lower() == "y"

# Get the jokes from the API
jokes = []
for i in range(joke_count):
    response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
    joke = response.json()['joke']
    jokes.append(joke)

# Get the user ID of the recipient
recipient_id = client.user_id_from_username(recipient_username)

# Send the jokes to the recipient
if send_all_at_once:
    client.direct_send('\n\n'.join(jokes), user_ids=[recipient_id])
else:
    delay = int(input("Enter delay between messages (in seconds): "))
    for joke in jokes:
        client.direct_send(joke, user_ids=[recipient_id])
        time.sleep(delay)

# Log out of Instagram
client.logout()
