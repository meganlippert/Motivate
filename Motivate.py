from twilio.rest import Client

def get_motivational_quote():
    


if __name__ == '__main__':
    accountSID ='AC98b0f70df613bce42e6915c98e264114'
    authToken = '9cf086d3db2a928e60192741c4ab572e'

    # twilioCli = Client(accountSID, authToken)

    myTwilioNumber = '+15172368488'
    myCellPhone = '+15173882089'

    motivation = get_motivational_quote()

    # message = twilioCli.messages.create(body=motivation, from_=myTwilioNumber, to=myCellPhone)
