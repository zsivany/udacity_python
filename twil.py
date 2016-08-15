from twilio.rest import TwilioRestClient

account_sid = "AC8efe21f827eb0bb0902ef57173abaab4" # Your Account SID from www.twilio.com/console
auth_token  = "69b3f0a2633959b75fb7860841a1348e"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+36307095691",    # Replace with your phone number
    from_="+12019039817") # Replace with your Twilio number

print(message.sid)
