import sys, json
import requests
import ipaddress


from unittest.main import main


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


    # Get response from url (expected json)
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
    def convertResponseToDict(response):
        data = response.json()
        return data

    # Function to search, takes dict and address to search for. Returns True or False   
    def searchResponse(response, addy):
        foundIPAddress = response['data']['resources']['ipv4']
        for address in foundIPAddress:
            # Since all addresses have '/22', split at '/' and test only first value which is ip
            if address.split('/')[0] == addy:
                # Print statements only for human readability/affirmation. I would remove to use in automation
                print("True: %s" % addy)
                return True
            else:
                print("False: %s" % addy)
                return False


if __name__ == '__main__':
    # Get user input IP address from sys argv
    userInput = sys.argv[1] 

    # If IP address is valid, search dict for it
    if IPAddress.validateIP(userInput):
        IPAddress.searchResponse(IPAddress.convertResponseToDict(IPAddress.getResponse(IPAddress.url)), userInput)

    main