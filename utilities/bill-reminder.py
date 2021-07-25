# import libs

from datetime import date
from twilio.rest import Client

client = Client("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx ")


# dictionary of all bills
# Bill key pair ex "name of bill" : "day bill is due"
Bills = {
    "Internet" : "01",
    "Spotify" : "10",
    "Car-Insurance" : "12",
    "Hulu" : "26",
    "Netflix" : "30",
}

# get todays date
today = time.strftime('%d')

# for loop to match the value stored in Bills with today's date
for value in Bills.values():
    if value == today:
        if value == "01":
            client.messages.create(to="+15555555555",from_="+15555555555",body="Internet, Mortgage, Studen Loan, and Cell phone paid")

        elif value == "10":
            client.messages.createto="+15555555555",from_="+15555555555",body="Spotify paid")

        elif value == "12":
            client.messages.create(to="+15555555555",from_="+15555555555",body="Car insurance paid")

        elif value == "26":
            client.messages.create(to="+15555555555",from_="+15555555555",body="Hulu paid")

        elif value == "30":
            client.messages.create(to="+15555555555",from_="+15555555555",body="Netflix paid")
