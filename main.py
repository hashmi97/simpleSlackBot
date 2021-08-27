import slack
import os
from dotenv import load_dotenv

env_path = os.path.join('.', '.env')
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])


while True:
    mode = input("To enter text mode type t. To exit type e.\n")
    if mode == 't':
        message = input("Please type the message you want to send:\n")
        if message == '':
            print("You cannot send an empty message!")
            continue
        client.chat_postMessage(channel="#bots", text=message)
    elif mode == 'e':
        print("Thank you for using the application!")
        exit()
    else:
        print("This was not a valid choice! Please try again.")
