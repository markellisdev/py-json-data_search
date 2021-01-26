import socket
import sys, logging, json
import requests


from unittest.main import main

log = logging.getLogger(__name__)
url = 'https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix'

class IPAddress:

    def __init__(self) -> None:
        pass

    # Function to validate if IP is an actual address    
    def validateIP(ipaddr):
        try:
            socket.inet_aton(ipaddr)
        except socket.error:
            return False
        return True

    # Get json response from url
    def getResponse(url):
        operUrl = requests.get(url)
        if(operUrl.status_code==200):
            # Convert to dictionary
            data = operUrl.json()
            with open('data.txt', 'w') as outfile:
                json.dump(data, outfile)

        else:
            print("Error receiving data", operUrl.getcode())
        return data
    
    def searchResponse(response, addy):
        foundIPAddress = response['data']['resources']['ipv4']
        for address in foundIPAddress:
            if address.split('/')[0] == addy:
                print("It's in here: %s" % addy)
            else:
                pass


# Get user input IP address from sys argv
userInput = sys.argv[1] 

# Is IP address valid? If so, search dict for it
if not IPAddress.validateIP(userInput):
    print('Not a valid ip: %s', userInput)
else:
    IPAddress.searchResponse(IPAddress.getResponse(url), userInput)

print('Hello, ' + userInput)




if __name__ == '__main__':
    main

# Function to confirm I can actually test. Still need to write actual tests for real functions, not math function.
# def madd(x,y):
#     return x + y