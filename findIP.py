import sys, logging, json
import requests
import ipaddress


from unittest.main import main

log = logging.getLogger(__name__)

class IPAddress:
    # moved url inside instead as attribute instead of passing it in, since it's static
    url = 'https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix'

    def __init__(self) -> None:
        pass

    # Function to validate if IP is an actual address    
    def validateIP(ipaddr):
        try:
            ip = ipaddress.ip_address(ipaddr)
        except ValueError:
            print('address/netmask is invalid: %s' % ipaddr)
            return False
        return True


    # Get response from url
    def getResponse(url):
        operUrl = requests.get(url)
        if(operUrl.status_code==200):
            # Convert to dictionary now it's own function below
            # data = operUrl.json()
            pass
        else:
            print("Error receiving data", operUrl.getcode())
        return operUrl

    # Convert to dict
    def convertResponseToJson(response):
        data = response.json()
        return data
    
    def searchResponse(response, addy):
        foundIPAddress = response['data']['resources']['ipv4']
        for address in foundIPAddress:
            # Since all addresses have '/22', split at '/' and test only first value which is ip
            if address.split('/')[0] == addy:
                # print("It's in here: %s" % addy)
                return True
            else:
                return False


# Get user input IP address from sys argv
userInput = sys.argv[1] 

# Is IP address is valid, search dict for it
if IPAddress.validateIP(userInput):
    IPAddress.searchResponse(IPAddress.convertResponseToJson(IPAddress.getResponse(IPAddress.url)), userInput)
    # IPAddress.searchResponse(IPAddress.getResponse(IPAddress.url), userInput)




if __name__ == '__main__':
    main

# Function to confirm I can actually test. Still need to write actual tests for real functions, not math function.
# def madd(x,y):
#     return x + y